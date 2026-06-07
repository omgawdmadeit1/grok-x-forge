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
- One-command deploy to Vercel/Railway
- Monetization dashboard starter

Built live with Grok while Joseph was away from computer.

Star this repo if you want to 10x your X income.

## 🚀 Launch It (One Command)

```bash
python launch.py
```

This starts the **incredible new VitaPass Full Power experience** at `http://localhost:8000` (the masterpiece built with the full Grok skill + plugin stack).

**Current state (more agents + more UEFN content)**: 17+ agents, full 7-role UEFN orchestrator with per-role Verse generation, live MCP feed, self-improver that actually ships PRs via MCPs, edge-ready deploy artifact.

`python launch.py` delivers everything.

---

## Deployment

### GitHub (recommended)
1. The repo has a GitHub Action (`.github/workflows/deploy-cloudflare-pages.yml`).
2. Go to your repo → **Settings → Secrets and variables → Actions**.
3. Add a **New repository secret**:
   - Name: `CLOUDFLARE_API_TOKEN`
   - Value: A token with `Pages:Edit` and `Workers:Edit` permissions (create at https://dash.cloudflare.com/profile/api-tokens).
4. Push to `main` or the feature branch → it will auto-deploy to Cloudflare Pages project `vitapass-full-power`.

### Manual / Local deploy (Cloudflare Pages)
```bash
# One time: create token with Pages:Edit
export CLOUDFLARE_API_TOKEN=your_token_here

cd vitapass-deploy
npx wrangler pages deploy . --project-name=vitapass-full-power
```

This deploys the beautiful static UI + Pages Functions for the edge `/forge` endpoint.

After deploy you can set:
```js
window.FORGE_ENDPOINT = "https://<your-project>.pages.dev/forge"
```

The `vitapass-deploy/` directory is always kept in sync with the latest code in this repo.