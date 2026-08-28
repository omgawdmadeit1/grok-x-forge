export default {
  async fetch(request) {
    const url = new URL(request.url);
    const payload = {
      name: "grok-x-forge",
      ok: true,
      agents: 6,
      docs: "https://github.com/omgawdmadeit1/grok-x-forge",
    };
    if (url.pathname === "/health") {
      return Response.json({ ok: true, service: "grok-x-forge" });
    }
    return Response.json(payload);
  },
};
