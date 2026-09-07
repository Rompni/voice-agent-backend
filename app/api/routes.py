from uuid import uuid4

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

from app.agent.orchestrator import AgentOrchestrator

router = APIRouter(prefix="/v1")
orchestrator = AgentOrchestrator()
_sessions: dict[str, dict] = {}


class SessionRequest(BaseModel):
    user_id: str = Field(..., min_length=1)


class SessionResponse(BaseModel):
    session_id: str
    user_id: str


@router.post("/sessions", response_model=SessionResponse)
async def create_session(body: SessionRequest) -> SessionResponse:
    session_id = str(uuid4())
    _sessions[session_id] = {"user_id": body.user_id}
    return SessionResponse(session_id=session_id, user_id=body.user_id)


@router.websocket("/sessions/{session_id}/ws")
async def session_ws(websocket: WebSocket, session_id: str) -> None:
    if session_id not in _sessions:
        await websocket.close(code=4404)
        return

    await websocket.accept()
    try:
        while True:
            payload = await websocket.receive_json()
            text = str(payload.get("text") or "").strip()
            result = await orchestrator.handle_turn(session_id=session_id, user_text=text)
            await websocket.send_json(result)
    except WebSocketDisconnect:
        return
