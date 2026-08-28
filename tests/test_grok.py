"""Grok helper validation (no live API calls)."""

import os

from doge_forge.grok import grok_complete, is_grok_available


def test_is_grok_available_false_without_key(monkeypatch) -> None:
    monkeypatch.delenv("XAI_API_KEY", raising=False)
    monkeypatch.delenv("GROK_API_KEY", raising=False)
    assert is_grok_available() is False


def test_grok_complete_validates_prompt() -> None:
    try:
        grok_complete("")
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "prompt" in str(exc)


def test_grok_complete_requires_key(monkeypatch) -> None:
    monkeypatch.delenv("XAI_API_KEY", raising=False)
    monkeypatch.delenv("GROK_API_KEY", raising=False)
    try:
        grok_complete("hello")
        assert False, "expected RuntimeError"
    except RuntimeError as exc:
        assert "not configured" in str(exc)


def test_is_grok_available_true_with_key(monkeypatch) -> None:
    monkeypatch.setenv("XAI_API_KEY", "test-key")
    assert is_grok_available() is True
    monkeypatch.delenv("XAI_API_KEY")
    assert os.getenv("XAI_API_KEY") is None
