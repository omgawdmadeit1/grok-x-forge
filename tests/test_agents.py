"""Import, activate, and generate from every landed agent."""

from doge_forge.agents import AGENT_SPECS, load_agent_class


def test_catalog_has_six_unique_agents() -> None:
    ids = [spec.agent_id for spec in AGENT_SPECS]
    assert len(ids) == 6
    assert len(set(ids)) == 6
    assert all(spec.price_doge > 0 for spec in AGENT_SPECS)


def test_every_agent_loads_and_requires_activation() -> None:
    for spec in AGENT_SPECS:
        agent_cls = load_agent_class(spec)
        agent = agent_cls(user_x_handle="@TestUser")
        assert agent.activated is False
        assert float(agent.price_doge) == spec.price_doge

        generate = getattr(agent, "generate_thread", None) or getattr(
            agent, "generate_viral_content"
        )
        blocked = generate("launch day")
        assert "Activate" in blocked or "activate" in blocked.lower()

        result = agent.activate("test-tx-hash")
        assert agent.activated is True
        assert isinstance(result, str) and result

        content = generate("launch day")
        assert isinstance(content, str)
        assert len(content) > 20
