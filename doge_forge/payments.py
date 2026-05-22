import requests
import time
from typing import Dict, Optional

class DogePayments:
    '''Transparent DOGE payment handler for DogeForge agent ecosystem.
    Uses public BlockCypher API for on-chain verification.
    Platform fee: 0.75% (reasonable & documented).'''
    
    EXPLORER_API = "https://api.blockcypher.com/v1/doge/main"
    
    def __init__(self, treasury_address: str = "YOUR_PUBLIC_DOGE_TREASURY_ADDRESS"):
        self.treasury_address = treasury_address
        self.platform_fee_rate = 0.0075  # 0.75% - reasonable for ecosystem
    
    def create_payment_request(self, base_amount_doge: float, agent_id: str, user_x_handle: str) -> Dict:
        '''Generate payment details. User pays total (base + fee) to treasury.'''
        platform_fee = round(base_amount_doge * self.platform_fee_rate, 8)
        total_amount = round(base_amount_doge + platform_fee, 8)
        return {
            "pay_to": self.treasury_address,
            "total_amount_doge": total_amount,
            "base_amount": base_amount_doge,
            "platform_fee": platform_fee,
            "agent_id": agent_id,
            "user": user_x_handle,
            "note": f"DogeForge Agent {agent_id} for @{user_x_handle} - fully transparent on Dogecoin",
            "verify_on": "https://blockchair.com/dogecoin"
        }
    
    def verify_transaction(self, tx_hash: str, expected_amount: float, min_confirmations: int = 1) -> bool:
        '''Poll blockchain for transparent confirmation.'''
        url = f"{self.EXPLORER_API}/txs/{tx_hash}"
        for _ in range(30):  # poll for ~5 min
            try:
                resp = requests.get(url)
                if resp.status_code == 200:
                    data = resp.json()
                    if (data.get('total', 0) / 1e8 >= expected_amount and 
                        data.get('confirmations', 0) >= min_confirmations and
                        self.treasury_address in str(data.get('addresses', []))):
                        return True
            except:
                pass
            time.sleep(10)
        return False

# Example usage:
# payments = DogePayments()
# req = payments.create_payment_request(10.0, 'x-shiller-001', 'OmgawdMadeit')
# print(req)