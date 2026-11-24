"""Central configuration for the research agent. Override via environment variables."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = DATA / "cache"
LOGS = ROOT / "logs"
VERIFY = ROOT / "verification"
DASH = ROOT / "dashboard"

USER_AGENT = os.getenv("RESEARCH_USER_AGENT", "app-research-agent/0.1 (+docs research; python-urllib)")
TIMEOUT = float(os.getenv("RESEARCH_TIMEOUT", "20"))
MAX_RETRIES = int(os.getenv("RESEARCH_MAX_RETRIES", "2"))
WORKERS = int(os.getenv("RESEARCH_WORKERS", "8"))           # parallel apps
PER_HOST_DELAY = float(os.getenv("RESEARCH_PER_HOST_DELAY", "1.0"))  # seconds between hits to one host
BATCH_SIZE = int(os.getenv("RESEARCH_BATCH_SIZE", "20"))
MAX_DISCOVERED_LINKS = int(os.getenv("RESEARCH_MAX_DISCOVERED", "6"))
MIN_USEFUL_TEXT = 800  # below this many chars we treat a page as JS-rendered / empty

# Rendering fallback for JS-heavy doc sites. r.jina.ai is a public reader that
# returns rendered page text; only public documentation URLs are sent to it.
RENDER_FALLBACK = os.getenv("RESEARCH_RENDER_FALLBACK", "1") == "1"
RENDER_PREFIX = "https://r.jina.ai/"

MCP_REGISTRY = "https://registry.modelcontextprotocol.io/v0/servers"

# Optional: Composio toolkit lookup (only runs when a key is present).
COMPOSIO_API_KEY = os.getenv("COMPOSIO_API_KEY", "")
# (Composio access goes through the official SDK in agent/composio_client.py)

for d in (DATA, CACHE, LOGS, VERIFY, DASH):
    d.mkdir(parents=True, exist_ok=True)
