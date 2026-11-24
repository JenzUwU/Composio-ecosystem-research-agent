"""Ground truth for the 30-app verification sample (independent of the Groq outputs).

    python verification/build_ground_truth.py  -> verification/ground_truth.json

How it was built: the reviewer re-read the official pages the crawler fetched
(verification/inspect_app.py), and checked vendor MCP repos/packages/endpoints for
existence (GitHub API, npm registry, HTTP status). This was done blind to Groq's
answers for these apps. `None` = not settled from official evidence -> excluded from scoring.
Reviewer: prepared with LLM assistance, blind to Groq's answers. NOT yet re-checked by a person.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SS_FREE, SS_TRIAL, SS_PAID = "Self-serve (free)", "Self-serve (free trial / sandbox)", "Self-serve (paid plan required)"
REVIEW, ENT, PART = "Admin approval / app review", "Enterprise-only", "Partnership / contact-sales gated"
R, L, O, N, I = ("Ready to build", "Buildable with limitations", "Requires outreach / partnership",
                 "Not currently feasible", "Insufficient evidence")

# (id, app, auth_methods, api_type, credential_access, mcp_available, verdict, evidence_urls, notes)
GT = [
    (3, "Pipedrive", ["OAuth2", "API Key"], ["REST"], SS_TRIAL, "Official", R,
     ["https://developers.pipedrive.com/docs/api/v1", "https://developers.pipedrive.com/docs/api/v1/Oauth", "https://pipedrive.com", "https://www.pipedrive.com/en/features/mcp-server"],
     "API token 'can be obtained manually from the Pipedrive app'; OAuth 2.0 for marketplace apps; 14-day free trial plus developer sandbox account; vendor MCP page."),
    (4, "Attio", ["OAuth2", "API Key"], ["REST"], SS_FREE, "Official", R,
     ["https://docs.attio.com/rest-api/guides/authentication", "https://attio.com", "https://docs.attio.com/mcp/overview"],
     "Auth guide lists OAuth 2.0 and API key; 'Start for free'; Attio MCP is a hosted vendor server. GraphQL only inside the App SDK, not a public API."),
    (10, "DealCloud", ["OAuth2", "API Key"], ["REST"], ENT, "Official", O,
     ["https://api.docs.dealcloud.com/docs/apikeys", "https://api.docs.dealcloud.com/docs/token", "https://api.docs.dealcloud.com/mcp/authentication"],
     "API key (client id/secret) exchanged via client_credentials; keys issued inside a customer's DealCloud tenant (Intapp enterprise product); vendor MCP docs."),
    (13, "Freshdesk", ["API Key"], ["REST"], SS_FREE, "Official", R,
     ["https://developers.freshdesk.com/api/", "https://freshdesk.com"],
     "API key (sent via HTTP basic); 'Freshdesk Free' plan tier; homepage 'Explore Freshdesk MCP'."),
    (15, "Pylon", ["API Key"], ["REST"], PART, "Official", O,
     ["https://docs.usepylon.com/pylon-docs/developer/api/authentication", "https://usepylon.com"],
     "Bearer API token generated in the dashboard (static token = key class); product is demo/sales-led; Pylon MCP in docs nav."),
    (16, "LiveAgent", ["API Key"], ["REST"], SS_TRIAL, "None found", R,
     ["https://support.liveagent.com/840770-Complete-API-reference", "https://www.liveagent.com/pricing/"],
     "API key auth; '30-day free trial, no credit card'; no vendor or registry MCP found."),
    (22, "Twilio", ["Basic", "API Key", "OAuth2"], ["REST"], SS_TRIAL, "Official", R,
     ["https://www.twilio.com/docs/usage/api-security-reference-guide/secure-auth", "https://www.twilio.com/docs/iam/api-keys", "https://github.com/twilio-labs/mcp"],
     "Account SID + Auth Token or API key via Basic; docs: 'Authenticate with OAuth 2.0, Basic, or Digest'; trial account; twilio-labs/mcp exists (GitHub API 200)."),
    (29, "Aircall", ["OAuth2", "Basic"], ["REST"], SS_PAID, "Third-party/community", L,
     ["https://developers.aircall.io/api-references/"],
     "'Authentication can be done through OAuth or Basic Auth' (OAuth for Technology Partners, Basic for Aircall customers); paid product; only community MCP servers."),
    (30, "Vonage", ["API Key", "Basic", "Other"], ["REST"], SS_TRIAL, "Official", R,
     ["https://developer.vonage.com/en/getting-started/concepts/authentication", "https://www.vonage.com/communications-apis/pricing"],
     "API key+secret (Basic) and JWT; 'Try it free'; io.github.Vonage/vonage-documentation-mcp is vendor-published but documentation-only."),
    (34, "GoHighLevel", ["OAuth2", "Personal Access Token"], ["REST"], None, "Official", L,
     ["https://marketplace.gohighlevel.com/docs/", "https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc"],
     "'OAuth 2.0 or Private Integration Token'; marketplace apps go through App Review; docs list an MCP Server page. Credential access (trial vs paid) not settled -> not scored."),
    (35, "Mailchimp", ["API Key", "OAuth2"], ["REST"], SS_FREE, "Official", R,
     ["https://mailchimp.com/developer/marketing/api-concepts/authentication", "https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/"],
     "'Authenticate with an API key or OAuth 2 token'; free plan; developer nav lists 'MCP server'."),
    (38, "Pinterest", ["OAuth2"], ["REST"], REVIEW, "None found", L,
     ["https://developers.pinterest.com/docs/getting-started/set-up-app/", "https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/", "https://developers.pinterest.com"],
     "Apps must request trial access, which Pinterest reviews; OAuth (Basic only for the client-credential token exchange); homepage says the Pinterest MCP is 'on the way' = not available yet."),
    (41, "Shopify", ["OAuth2", "Personal Access Token"], ["GraphQL", "REST"], SS_TRIAL, "Official", R,
     ["https://shopify.dev/docs/apps/build/authentication-authorization", "https://shopify.dev/docs/api/admin-graphql", "https://www.npmjs.com/package/@shopify/dev-mcp"],
     "OAuth for apps, Admin API access token for custom apps; free Partner account + development stores; Admin GraphQL primary, REST legacy; @shopify/dev-mcp on npm (200)."),
    (44, "Salesforce Commerce Cloud", ["OAuth2"], ["REST"], ENT, "Official", O,
     ["https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-admin-apis.html", "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-shopper-apis.html", "https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/quick-start-landing-page.html"],
     "SLAS / Account Manager API clients on a B2C Commerce instance (enterprise customers); 'Agentic MCP Shopper Tools (Pilot)'."),
    (49, "Amazon Selling Partner", ["OAuth2"], ["REST"], REVIEW, "None found", L,
     ["https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer", "https://developer-docs.amazon.com/sp-api/docs/welcome"],
     "Login with Amazon OAuth; a reviewed Developer Profile is required before registering an app; no vendor MCP found."),
    (51, "DataForSEO", ["Basic"], ["REST"], SS_TRIAL, "Official", R,
     ["https://docs.dataforseo.com/v3/auth/", "https://github.com/dataforseo/mcp-server-typescript"],
     "HTTP Basic (login + API password); trial credit on signup; dataforseo/mcp-server-typescript (GitHub 200)."),
    (57, "Bright Data", ["API Key"], ["REST"], SS_TRIAL, "Official", R,
     ["https://docs.brightdata.com/api-reference/authentication", "https://brightdata.com", "https://docs.brightdata.com/mcp-server/overview"],
     "API key as Bearer; 'Start free trial'; vendor MCP docs + brightdata/brightdata-mcp repo."),
    (60, "Clay", None, ["REST"], ENT, "Official", O,
     ["https://university.clay.com/docs/http-api-integration-overview", "https://www.clay.com/pricing"],
     "The 'HTTP API' doc is Clay calling external APIs, not a public Clay API; programmatic access is enterprise-tier; Clay MCP documented. Auth model not settled -> not scored."),
    (61, "GitHub", ["OAuth2", "Personal Access Token", "Other"], ["REST", "GraphQL"], SS_FREE, "Official", R,
     ["https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api", "https://docs.github.com/en/graphql", "https://github.com/github/github-mcp-server"],
     "OAuth apps, PATs, GitHub App (JWT / installation token); REST + GraphQL; github/github-mcp-server (GitHub 200)."),
    (62, "Vercel", ["Personal Access Token", "OAuth2"], ["REST"], SS_FREE, "Official", R,
     ["https://vercel.com/docs/rest-api/reference/welcome", "https://vercel.com/docs/mcp"],
     "'Vercel Access Tokens are required'; OAuth for integrations; free Hobby plan; official MCP docs, mcp.vercel.com answers 401 (live, auth-protected)."),
    (64, "Cloudflare", ["API Key", "Personal Access Token"], ["REST", "GraphQL"], SS_FREE, "Official", R,
     ["https://developers.cloudflare.com/fundamentals/api/get-started/create-token/", "https://developers.cloudflare.com/api/", "https://github.com/cloudflare/mcp-server-cloudflare"],
     "API tokens (and legacy global API key); REST + GraphQL Analytics API; free plan; cloudflare/mcp-server-cloudflare + registry com.cloudflare.mcp."),
    (71, "Notion", ["OAuth2", "Personal Access Token"], ["REST"], SS_FREE, "Official", R,
     ["https://developers.notion.com/docs/authorization", "https://developers.notion.com/reference/authentication", "https://github.com/makenotion/notion-mcp-server"],
     "Internal integration token + OAuth for public integrations; free plan; makenotion/notion-mcp-server."),
    (73, "Linear", ["OAuth2", "API Key"], ["GraphQL"], SS_FREE, "Official", R,
     ["https://linear.app/developers/graphql", "https://linear.app/developers/oauth-2-0-authentication", "https://linear.app/docs/mcp"],
     "GraphQL only; OAuth 2.0 + personal API keys; free plan; registry app.linear/linear + MCP docs page."),
    (77, "ClickUp", ["OAuth2", "Personal Access Token"], ["REST"], SS_FREE, "Official", R,
     ["https://developer.clickup.com/docs/authentication", "https://clickup.com/api"],
     "Personal API token + OAuth; Free Forever plan; 'Connect your AI with ClickUp using our MCP Server'."),
    (84, "Paygent Connect", [], [], "Unclear", "None found", I,
     ["https://docs.nmi.com/llms.txt"],
     "No Paygent Connect developer docs found by crawler or web search. NMI (stated underlying gateway) has docs, but the Paygent-NMI relationship is unverified, so nothing about Paygent's own API can be confirmed."),
    (87, "Xero", ["OAuth2"], ["REST"], SS_FREE, "Official", R,
     ["https://developer.xero.com/documentation/guides/oauth2/overview/", "https://developer.xero.com/documentation/getting-started-guide/", "https://github.com/XeroAPI/xero-mcp-server"],
     "OAuth 2.0 only; free developer account + demo company (partner program only beyond 25 connections); XeroAPI/xero-mcp-server."),
    (89, "Ramp", ["OAuth2"], ["REST"], REVIEW, "Official", L,
     ["https://docs.ramp.com/llms.txt", "https://github.com/ramp-public/ramp-mcp"],
     "OAuth (client credentials / auth code) via a developer app created by an admin of an approved Ramp business account; ramp-public/ramp-mcp (301 = renamed, exists)."),
    (91, "NotebookLM", ["OAuth2", "Other"], ["REST"], None, "Third-party/community", None,
     ["https://cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks"],
     "NotebookLM Enterprise API on Google Cloud (OAuth / service-account credentials) needs an enterprise license; consumer NotebookLM has no API. Access and verdict not settled -> not scored. Only community MCP servers."),
    (92, "Otter AI", [], [], None, "Official", None,
     ["https://help.otter.ai/", "https://mcp.otter.ai/mcp"],
     "No public REST API documented in the fetched help center; official hosted MCP endpoint mcp.otter.ai answers 401 (live, OAuth). Access and verdict not scored."),
    (95, "Reducto", ["API Key"], ["REST"], SS_FREE, "Official", R,
     ["https://docs.reducto.ai/quickstart", "https://docs.reducto.ai/"],
     "'Create a Reducto account / Get your API key'; docs list a 'Reducto MCP server'."),
]

FIELDS = ["auth_methods", "api_type", "credential_access", "mcp_available", "buildability_verdict"]

if __name__ == "__main__":
    sample = json.loads((ROOT / "verification/verification_sample.json").read_text(encoding="utf-8"))["app_ids"]
    assert sorted(g[0] for g in GT) == sorted(sample), "ground truth must match the drawn sample"
    apps = [dict(zip(["id", "app_name"] + FIELDS + ["evidence_urls", "notes"], g)) for g in GT]
    meta = {"method": __doc__.strip(), "reviewer": "LLM-assisted, built from the fetched official pages blind to Groq's answers; not yet re-checked by a person",
            "date": "2026-11-24", "null_means": "not settled from official evidence; excluded from scoring"}
    (ROOT / "verification/ground_truth.json").write_text(json.dumps({"meta": meta, "apps": apps}, indent=1), encoding="utf-8")
    scorable = sum(1 for a in apps for f in FIELDS if a[f] is not None)
    print(f"ground truth: {len(apps)} apps, {scorable} scorable claims, {len(apps) * 5 - scorable} excluded")
