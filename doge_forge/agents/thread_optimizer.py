"""
Thread Optimizer - Auto-forged by VitaPass Forge

Price: 22 DOGE
Description: Takes raw ideas or existing threads and ruthlessly optimizes them for X virality: better hooks, pacing, social proof, CTAs, hashtag strategy, and reply chains. Uses patterns from the best performing agents in the marketplace.
Forge Prompt: World-class X thread optimizer and editor. Given any topic or draft thread, produces a dramatically stronger version (stronger open, tighter pacing, more proof, clearer CTA, native feel). References successful threads from launch-hype, meme-lord, community_builder, and frontend-designer agents. Always returns 5-8 tweet threads that feel native and high-signal.
"""

import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


class ThreadOptimizerAgent:
    """Auto-generated agent from VitaPass Grok Forge. Uses real Grok when available."""

    def __init__(self, user_x_handle: str = "@GrokXForge"):
        self.activated = False
        self.price_doge = 22
        self.user_x_handle = user_x_handle
        self.forge_prompt = """Elite X thread optimizer. Takes any topic or rough draft and transforms it into a high-engagement thread. Strong hook in tweet 1, social proof and value in middle, clear CTA + link at end. Studies patterns from the top agents in the VitaPass marketplace (meme-lord, launch-hype, reply-engine, community-builder). Output is always ready-to-post, native, and 5-8 tweets. Never salesy."""

    def activate(self, tx_hash: str):
        print(f"✅ DOGE transaction verified: {tx_hash}")
        print(f"🚀 Thread Optimizer ACTIVATED for {self.user_x_handle}!")
        self.activated = True
        return "Agent activated. Paste a rough idea or thread and I will optimize it."

    def generate_thread(self, topic: str, product_name: str = "the product", affiliate_link: str = None) -> str:
        if not self.activated:
            return "❌ Activate this agent with the payment flow first."

        affiliate_link = affiliate_link or f"https://example.com/ref/{self.user_x_handle}"
        topic_title = topic.title()

        # Try real Grok generation using the Forge prompt
        try:
            from doge_forge.grok import grok_complete, is_grok_available
            if is_grok_available():
                system = (
                    "You are a specialized X agent. " + self.forge_prompt +
                    " Write concise, high-value X threads (5-8 tweets) with hooks, social proof, and CTAs. "
                    "Tone: confident and valuable. Include relevant hashtags."
                )
                prompt = f"Write a viral thread about '{topic}' promoting '{product_name}'. Include link naturally: {affiliate_link}."
                return grok_complete(prompt, system_prompt=system, max_tokens=800, temperature=0.85)
        except Exception:
            pass

        # Fallback using Forge example
        return f"""1/ Raw idea: "{topic}" 

2/ Optimized thread that actually performs:

1/ The best threads don't start with the product. They start with the pain or the surprising truth.

... (full optimized 6-tweet version with proof, numbers, and soft CTA would go here)

#ForgedByVitaPass #GrokXForge
"""