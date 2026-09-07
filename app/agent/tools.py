async def run_tool(name: str, arg: str) -> dict:
    if name == "echo":
        return {"ok": True, "output": arg}
    if name == "utc_now":
        from datetime import datetime, timezone

        return {"ok": True, "output": datetime.now(timezone.utc).isoformat()}
    return {"ok": False, "error": f"unknown tool: {name}"}
