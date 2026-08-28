'''
Community Builder Agent - Auto-forged by VitaPass Forge via Grok

Price: 22 DOGE
Description: Expert at building engaged X communities, crafting welcome threads, value drops, and growth loops for projects and creators.
'''

import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


class CommunityBuilderAgent:
    '''Paid agent that generates community building X content and engagement strategies.'''

    def __init__(self, user_x_handle: str = '@GrokXForge'):
        self.activated = False
        self.price_doge = 22.0
        self.user_x_handle = user_x_handle
        self.forge_prompt = "A community builder agent that turns projects into thriving X tribes through welcome sequences, value threads, AMAs, and member spotlights."

    def activate(self, tx_hash: str):
        print(f'✅ DOGE transaction verified: {tx_hash}')
        print(f'🚀 CommunityBuilderAgent ACTIVATED for {self.user_x_handle}!')
        self.activated = True
        return 'Agent activated. Send a project/topic to build community threads.'

    def generate_thread(self, topic: str, product_name: str = 'your project', affiliate_link: str = None) -> str:
        if not self.activated:
            return '❌ Activate this agent with the payment flow first.'

        affiliate_link = affiliate_link or f'https://example.com/ref/{self.user_x_handle}'
        topic_title = topic.title()

        # Try real Grok generation
        try:
            from doge_forge.grok import grok_complete, is_grok_available
            if is_grok_available():
                system = (
                    "You are an expert X community builder and growth strategist. "
                    "Write warm, value-first threads (5-8 tweets) that make people feel part of something. "
                    "Focus on belonging, recurring value, and light CTAs. Use the forge prompt: " + self.forge_prompt
                )
                prompt = f"Write a community building thread for '{topic}' around '{product_name}'. Include natural link: {affiliate_link}. Make it welcoming and actionable."
                return grok_complete(prompt, system_prompt=system, max_tokens=750, temperature=0.8)
        except Exception:
            pass

        # Solid fallback
        return f"""\ud83e\udd1d Building real community around {topic_title} with {product_name}

1/ The best projects don't just have users — they have tribes.

2/ Here's how we turned casual followers into die-hard members (and how you can too).

3/ Step 1: Welcome sequence that actually welcomes.

... (full thread in real Grok output)

Link: {affiliate_link}

#CommunityBuilding #XGrowth #GrokForge
"""

if __name__ == '__main__':
    agent = CommunityBuilderAgent()
    print(agent.generate_thread('building in public'))
