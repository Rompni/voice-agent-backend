# voice-agent-backend

Small **voice-oriented agent backend** in Python: session API, WebSocket turns, tool hooks, and a pluggable retriever.

Not a full product — a clean starter you can run locally and extend.

## What it does

- `POST /v1/sessions` — create an agent session
- `WS /v1/sessions/{id}/ws` — send user text/audio-events, get agent replies
- Tool registry stubs (weather/echo style) for agent actions
- Optional RAG-style retriever interface (in-memory by default)

## Stack

- Python 3.11+
- FastAPI + Uvicorn
- Pydantic Settings
- WebSockets
- Docker Compose (optional Postgres if you wire a real store later)

## Quick start

```bash
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

```bash
curl -s localhost:8000/health
curl -s -X POST localhost:8000/v1/sessions -H 'content-type: application/json' -d '{"user_id":"demo"}'
```

## Layout

```
app/
  main.py
  api/routes.py
  agent/orchestrator.py
  agent/tools.py
  rag/retriever.py
  core/config.py
```

## License

MIT
