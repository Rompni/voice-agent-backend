from app.agent.tools import run_tool
from app.rag.retriever import Retriever


class AgentOrchestrator:
    def __init__(self) -> None:
        self.retriever = Retriever()

    async def handle_turn(self, session_id: str, user_text: str) -> dict:
        if user_text.startswith("/tool "):
            _, _, rest = user_text.partition(" ")
            name, _, arg = rest.partition(" ")
            return {
                "session_id": session_id,
                "type": "tool",
                "result": await run_tool(name.strip(), arg.strip()),
            }

        hits = await self.retriever.search(user_text) if user_text else []
        reply = self._stub_reply(user_text, hits)
        return {
            "session_id": session_id,
            "type": "message",
            "reply": reply,
            "context_hits": len(hits),
        }

    def _stub_reply(self, user_text: str, hits: list[dict]) -> str:
        if not user_text:
            return "Say something, or use /tool echo hi"
        if hits:
            return f"Got it: {user_text} (context: {hits[0]['text']})"
        return f"Got it: {user_text}"
