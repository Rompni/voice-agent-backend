class Retriever:
    """In-memory stand-in. Swap for your own index later."""

    def __init__(self) -> None:
        self._docs = [
            {"id": "1", "text": "Agents can call tools with /tool echo hi"},
            {"id": "2", "text": "Open a session with POST /v1/sessions then connect to the WS"},
        ]

    async def search(self, query: str, limit: int = 3) -> list[dict]:
        q = query.lower()
        scored = []
        for doc in self._docs:
            score = sum(1 for w in q.split() if w in doc["text"].lower())
            if score:
                scored.append({**doc, "score": float(score)})
        scored.sort(key=lambda d: d["score"], reverse=True)
        return scored[:limit]
