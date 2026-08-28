"""Catalog CLI and FastAPI routes."""

from fastapi.testclient import TestClient

from launch import app, catalog_lines


def test_health_and_agents_routes() -> None:
    client = TestClient(app)
    health = client.get("/health")
    assert health.status_code == 200
    body = health.json()
    assert body["ok"] is True
    assert body["agents"] == 6

    agents = client.get("/agents")
    assert agents.status_code == 200
    payload = agents.json()
    assert payload["count"] == 6
    assert len(payload["agents"]) == 6


def test_index_lists_agents() -> None:
    client = TestClient(app)
    page = client.get("/")
    assert page.status_code == 200
    assert "community-builder" in page.text
    assert "uefn-verse-crafter" in page.text


def test_catalog_lines_include_all_ids() -> None:
    text = "\n".join(catalog_lines())
    for agent_id in (
        "x-doge-shiller",
        "community-builder",
        "doge-economy-analyst",
        "thread-optimizer",
        "mcp-activity-monitor",
        "uefn-verse-crafter",
    ):
        assert agent_id in text
