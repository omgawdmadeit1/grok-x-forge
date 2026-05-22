from doge_forge.payments import DogePayments

class AgentMarketplace:
    '''DogeForge Agent Economy - register, pay, and activate Grok agents'''
    
    def __init__(self):
        self.payments = DogePayments()  # transparent DOGE handler
        self.agents = {}  # agent_id: details
    
    def register_agent(self, agent_id: str, description: str, price_doge: float):
        '''List an agent for sale in DOGE'''
        self.agents[agent_id] = {
            "description": description,
            "price": price_doge,
            "status": "available"
        }
        return self.agents[agent_id]
    
    def activate_agent(self, agent_id: str, user_x_handle: str, tx_hash: str):
        '''Pay in DOGE (verified on-chain) to activate agent'''
        if agent_id not in self.agents:
            return {"error": "Agent not found"}
        req = self.payments.create_payment_request(
            self.agents[agent_id]["price"], agent_id, user_x_handle
        )
        if self.payments.verify_transaction(tx_hash, req["total_amount_doge"]):
            self.agents[agent_id]["status"] = "active"
            return {"success": True, "agent_activated": agent_id, "tx_hash": tx_hash}
        return {"error": "Payment not verified on Dogecoin blockchain"}

# First X-integrated agent example (Grok-powered shiller)
# marketplace.register_agent('x-doge-shiller', 'Auto-posts viral DOGE memes on X', 5.0)