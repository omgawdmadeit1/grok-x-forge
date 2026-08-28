#!/usr/bin/env python3
"""Print the DogeForge catalog and serve it at http://localhost:8000."""

from __future__ import annotations

import argparse
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from doge_forge.agents import AGENT_SPECS, load_agent_class
from doge_forge.marketplace import AgentMarketplace, seed_default_agents

app = FastAPI(title="GrokX Forge", version="0.2.0")


def build_marketplace() -> AgentMarketplace:
    """Return a marketplace seeded with every landed agent."""
    return seed_default_agents(AgentMarketplace())


def catalog_lines() -> list[str]:
    """Human-readable catalog rows."""
    market = build_marketplace()
    lines = [
        "GrokX Forge / DogeForge — agent catalog",
        f"{len(market.agents)} agents registered:",
        "",
    ]
    for agent in market.list_agents():
        lines.append(
            f"  {agent['id']}: {agent['price']:g} DOGE — {agent['description']}"
        )
    return lines


@app.get("/health")
def health() -> dict:
    return {"ok": True, "service": "grok-x-forge", "agents": len(AGENT_SPECS)}


@app.get("/agents")
def agents() -> dict:
    market = build_marketplace()
    return {"count": len(market.agents), "agents": market.list_agents()}


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    rows = "".join(
        f"<tr><td><code>{agent['id']}</code></td>"
        f"<td>{agent['price']:g} DOGE</td>"
        f"<td>{agent['description']}</td></tr>"
        for agent in build_marketplace().list_agents()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>GrokX Forge</title>
  <style>
    body {{ font-family: ui-sans-serif, system-ui, sans-serif; margin: 2rem; background: #0b0f14; color: #e8eef5; }}
    a {{ color: #7dd3fc; }}
    table {{ border-collapse: collapse; width: 100%; max-width: 52rem; }}
    th, td {{ border-bottom: 1px solid #243040; padding: 0.6rem 0.5rem; text-align: left; }}
    code {{ color: #fbbf24; }}
  </style>
</head>
<body>
  <h1>GrokX Forge</h1>
  <p>Paid Grok agents in the DogeForge marketplace. JSON: <a href="/agents">/agents</a> · <a href="/health">/health</a></p>
  <table>
    <thead><tr><th>Agent</th><th>Price</th><th>Role</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</body>
</html>
"""


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Launch the GrokX Forge catalog")
    parser.add_argument("--catalog-only", action="store_true", help="Print catalog and exit")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host")
    parser.add_argument("--port", type=int, default=int(os.getenv("PORT", "8000")))
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.port <= 0:
        raise ValueError("port must be positive")

    for spec in AGENT_SPECS:
        load_agent_class(spec)

    print("\n".join(catalog_lines()))
    print("\nActivate via AgentMarketplace.activate_agent(...) after on-chain payment.")
    if args.catalog_only:
        return

    import uvicorn

    print(f"\nServing catalog at http://127.0.0.1:{args.port}")
    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
