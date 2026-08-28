"""Optional Grok completion helpers used by forged agents."""

from __future__ import annotations

import os


def is_grok_available() -> bool:
    """Return True when an xAI API key is configured."""
    return bool(os.getenv("XAI_API_KEY") or os.getenv("GROK_API_KEY"))


def grok_complete(
    prompt: str,
    system_prompt: str = "",
    max_tokens: int = 800,
    temperature: float = 0.8,
) -> str:
    """Call Grok when configured; raise if the SDK or key is missing."""
    if not prompt or not isinstance(prompt, str):
        raise ValueError("prompt must be a non-empty string")
    if max_tokens <= 0:
        raise ValueError("max_tokens must be positive")
    if not 0 <= temperature <= 2:
        raise ValueError("temperature must be between 0 and 2")
    if not is_grok_available():
        raise RuntimeError("Grok API key is not configured")

    from xai_sdk import Client

    client = Client()
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    response = client.chat.create(
        model="grok-3",
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return str(response)
