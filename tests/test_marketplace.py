"""Marketplace registration and payment-request helpers."""

from doge_forge.marketplace import AgentMarketplace, seed_default_agents
from doge_forge.payments import DogePayments


def test_seed_default_agents_registers_catalog() -> None:
    market = seed_default_agents(AgentMarketplace())
    listed = market.list_agents()
    assert len(listed) == 6
    assert {item["id"] for item in listed} == {
        "x-doge-shiller",
        "community-builder",
        "doge-economy-analyst",
        "thread-optimizer",
        "mcp-activity-monitor",
        "uefn-verse-crafter",
    }


def test_register_agent_rejects_invalid_price() -> None:
    market = AgentMarketplace()
    try:
        market.register_agent("bad", "nope", 0)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "price" in str(exc)


def test_activate_unknown_agent_returns_error() -> None:
    market = AgentMarketplace()
    result = market.activate_agent("missing", "@user", "tx")
    assert result["error"] == "Agent not found"


def test_payment_request_includes_platform_fee() -> None:
    payments = DogePayments(treasury_address="DTESTADDRESS")
    req = payments.create_payment_request(100.0, "x-doge-shiller", "OmgawdMadeit")
    assert req["pay_to"] == "DTESTADDRESS"
    assert req["base_amount"] == 100.0
    assert req["platform_fee"] == 0.75
    assert req["total_amount_doge"] == 100.75
    assert req["agent_id"] == "x-doge-shiller"


def test_seed_default_agents_rejects_wrong_type() -> None:
    try:
        seed_default_agents("nope")  # type: ignore[arg-type]
        assert False, "expected TypeError"
    except TypeError as exc:
        assert "AgentMarketplace" in str(exc)
