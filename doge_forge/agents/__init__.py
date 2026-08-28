"""Paid GrokX / DogeForge agents that shipped on the integration branch."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class AgentSpec:
    """Catalog entry for a paid agent."""

    agent_id: str
    description: str
    price_doge: float
    class_name: str
    module: str


AGENT_SPECS: tuple[AgentSpec, ...] = (
    AgentSpec(
        agent_id="x-doge-shiller",
        description="Auto-posts viral DOGE memes and shill threads on X",
        price_doge=42.0,
        class_name="DogeShillerAgent",
        module="doge_forge.agents.doge_shiller_agent",
    ),
    AgentSpec(
        agent_id="community-builder",
        description="Welcome sequences, value threads, AMAs, and member spotlights",
        price_doge=22.0,
        class_name="CommunityBuilderAgent",
        module="doge_forge.agents.community_builder",
    ),
    AgentSpec(
        agent_id="doge-economy-analyst",
        description="On-chain + marketplace economy intelligence",
        price_doge=27.0,
        class_name="DogeEconomyAnalystAgent",
        module="doge_forge.agents.doge_economy_analyst",
    ),
    AgentSpec(
        agent_id="thread-optimizer",
        description="Optimizes raw ideas into high-signal X threads",
        price_doge=22.0,
        class_name="ThreadOptimizerAgent",
        module="doge_forge.agents.thread_optimizer",
    ),
    AgentSpec(
        agent_id="mcp-activity-monitor",
        description="Watches Linear + GitHub MCP activity and turns it into alpha threads",
        price_doge=33.0,
        class_name="McpActivityMonitorAgent",
        module="doge_forge.agents.mcp_activity_monitor",
    ),
    AgentSpec(
        agent_id="uefn-verse-crafter",
        description="Elite Verse code generator for UEFN islands and devices",
        price_doge=55.0,
        class_name="UefnVerseCrafterAgent",
        module="doge_forge.agents.uefn_verse_crafter",
    ),
)


def load_agent_class(spec: AgentSpec) -> Callable:
    """Import and return the agent class for a catalog spec."""
    if not spec.module or not spec.class_name:
        raise ValueError("AgentSpec requires module and class_name")
    module = __import__(spec.module, fromlist=[spec.class_name])
    agent_cls = getattr(module, spec.class_name, None)
    if agent_cls is None:
        raise ImportError(f"{spec.class_name} not found in {spec.module}")
    return agent_cls
