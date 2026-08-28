# GrokX Forge

**Build, ship, and monetize X (Twitter) agents using Grok — entirely in chat.**

No laptop required. Conversational CI/CD pipeline powered by Grok.

## How to Make Money
- Sell premium X growth agents (viral thread generators, DM automators, trend sniper bots)
- Create agent marketplace (like your VitaPass idea)
- Offer SaaS: Hosted agents for creators & brands
- Affiliate revenue from xAI API + X Premium referrals

## Features
- Grok as your CI/CD brain
- Real-time X integration (trends, posting, analytics)
- One-command local catalog (`python launch.py`)
- Transparent $DOGE agent marketplace
- Cloudflare Pages + Workers deploy artifacts

Built live with Grok while Joseph was away from computer.

## Agent catalog (landed)

These paid agents are in `doge_forge/agents/` and auto-register on launch:

| Agent | Price | Role |
| --- | ---: | --- |
| `x-doge-shiller` | 42 DOGE | Viral Dogecoin / X shill threads |
| `community-builder` | 22 DOGE | Welcome sequences, value threads, AMAs |
| `doge-economy-analyst` | 27 DOGE | On-chain + marketplace economy intel |
| `thread-optimizer` | 22 DOGE | Raw ideas → high-signal X threads |
| `mcp-activity-monitor` | 33 DOGE | Linear / GitHub MCP activity → alpha threads |
| `uefn-verse-crafter` | 55 DOGE | UEFN Verse snippets and island mechanics |

## Launch it

```bash
python -m pip install -r requirements.txt
python launch.py
```

This prints the catalog and serves it at `http://localhost:8000` (`/`, `/health`, `/agents`).

## Deployment

### GitHub (recommended)
1. The repo has a GitHub Action (`.github/workflows/deploy-cloudflare-pages.yml`).
2. Go to the repo → **Settings → Secrets and variables → Actions**.
3. Add a **New repository secret**:
   - Name: `CLOUDFLARE_API_TOKEN`
   - Value: A token with `Pages:Edit` and `Workers:Edit` permissions (create at https://dash.cloudflare.com/profile/api-tokens).
4. Push to `main` → it deploys `vitapass-deploy/` to Cloudflare Pages project `vitapass-full-power`.
   The workflow skips cleanly when the token is missing (so PRs stay mergeable).

### Manual / local deploy (Cloudflare Pages)
```bash
export CLOUDFLARE_API_TOKEN=your_token_here
cd vitapass-deploy
npx wrangler pages deploy . --project-name=vitapass-full-power
```

After deploy you can set:
```js
window.FORGE_ENDPOINT = "https://<your-project>.pages.dev/forge"
```

## Integration notes

This tree consolidates the unique work from PRs #1–#4 onto latest `main`:

- **#1** CommunityBuilderAgent (`doge_forge/agents/community_builder.py`)
- **#2** Expansion notes (`VITAPASS_FULL_EXPANSION.md`) — vNext intent, not all listed files existed on the branch
- **#3** Self-improver README note (UEFN / MCP / edge stack intent)
- **#4** Four additional agents, Cloudflare Pages workflow, and `vitapass-deploy/wrangler.toml`

The original PR descriptions referenced `server.py`, `vitapass/index.html`, `uefn_forge/`, and 17 agents. Those files were never committed on any open branch. This integration keeps the real agent code and deploy config, and makes `python launch.py` work for the six agents that actually landed.

Made with Grok + omgawdmadeit1
