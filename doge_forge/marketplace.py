from __future__ import annotations

from typing import Dict, List

from doge_forge.agents import AGENT_SPECS
from doge_forge.payments import DogePayments


class AgentMarketplace:
    """DogeForge Agent Economy - register, pay, and activate Grok agents."""

    def __init__(self) -> None:
        self.payments = DogePayments()
        self.agents: Dict[str, Dict] = {}

    def register_agent(self, agent_id: str, description: str, price_doge: float) -> Dict:
        """List an agent for sale in DOGE."""
        if not agent_id or not isinstance(agent_id, str):
            raise ValueError("agent_id must be a non-empty string")
        if not description or not isinstance(description, str):
            raise ValueError("description must be a non-empty string")
        if not isinstance(price_doge, (int, float)) or price_doge <= 0:
            raise ValueError("price_doge must be a positive number")
        self.agents[agent_id] = {
            "id": agent_id,
            "description": description,
            "price": float(price_doge),
            "status": "available",
        }
        return self.agents[agent_id]

    def list_agents(self) -> List[Dict]:
        """Return registered agents sorted by id."""
        return [self.agents[key] for key in sorted(self.agents)]

    def activate_agent(self, agent_id: str, user_x_handle: str, tx_hash: str) -> Dict:
        """Pay in DOGE (verified on-chain) to activate agent."""
        if agent_id not in self.agents:
            return {"error": "Agent not found"}
        if not user_x_handle or not tx_hash:
            return {"error": "user_x_handle and tx_hash are required"}
        req = self.payments.create_payment_request(
            self.agents[agent_id]["price"], agent_id, user_x_handle
        )
        if self.payments.verify_transaction(tx_hash, req["total_amount_doge"]):
            self.agents[agent_id]["status"] = "active"
            return {"success": True, "agent_activated": agent_id, "tx_hash": tx_hash}
        return {"error": "Payment not verified on Dogecoin blockchain"}


def seed_default_agents(marketplace: AgentMarketplace) -> AgentMarketplace:
    """Register every shipped agent from the catalog."""
    if not isinstance(marketplace, AgentMarketplace):
        raise TypeError("marketplace must be an AgentMarketplace")
    for spec in AGENT_SPECS:
        marketplace.register_agent(spec.agent_id, spec.description, spec.price_doge)
    return marketplace
