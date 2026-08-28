"""Sanity-check the Cloudflare Worker module exists and is non-empty."""

from pathlib import Path


def test_worker_module_exports_fetch() -> None:
    source = Path("worker.js").read_text(encoding="utf-8")
    assert "export default" in source
    assert "async fetch" in source
    assert "grok-x-forge" in source
