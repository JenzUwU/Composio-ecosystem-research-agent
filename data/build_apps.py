"""Builds data/apps.json — the 100-app research set from the Composio brief.

Each app gets: id, name, category, the website/hint exactly as given in the brief,
and `seed_urls`: candidate official developer-doc URLs that the research agent
starts from. Seed URLs are only *candidates*; the agent records the HTTP status of
every fetch, so a wrong or dead seed is visible in the output rather than hidden.
"""
import json
from pathlib import Path

C = {
    1: "CRM and Sales", 2: "Support and Helpdesk", 3: "Communications and Messaging",
    4: "Marketing, Ads, Email and Social", 5: "Ecommerce", 6: "Data, SEO and Scraping",
    7: "Developer, Infra and Data platforms", 8: "Productivity and Project Management",
    9: "Finance and Fintech", 10: "AI, Research and Media-native",
}

# (name, hint from brief, [seed urls])
APPS = [
    # 1 CRM and Sales
    ("Salesforce", "salesforce.com", ["https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm", "https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm"]),
    ("HubSpot", "hubspot.com", ["https://developers.hubspot.com/docs/api/overview", "https://developers.hubspot.com/docs/api/oauth-quickstart-guide", "https://developers.hubspot.com/docs/api/private-apps"]),
    ("Pipedrive", "pipedrive.com", ["https://developers.pipedrive.com/docs/api/v1", "https://pipedrive.readme.io/docs/core-api-concepts-authentication"]),
    ("Attio", "attio.com", ["https://docs.attio.com/rest-api/overview", "https://docs.attio.com/rest-api/guides/authentication"]),
    ("Twenty", "twenty.com (open-source CRM)", ["https://twenty.com/developers", "https://twenty.com/developers/section/api-and-webhooks/api"]),
    ("Podio", "podio.com", ["https://developers.podio.com/", "https://developers.podio.com/authentication"]),
    ("Zoho CRM", "zoho.com/crm", ["https://www.zoho.com/crm/developer/docs/api/v8/", "https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html"]),
    ("Close", "close.com", ["https://developer.close.com/", "https://developer.close.com/topics/authentication/"]),
    ("Copper", "copper.com", ["https://developer.copper.com/"]),
    ("DealCloud", "api.docs.dealcloud.com", ["https://api.docs.dealcloud.com/"]),
    # 2 Support and Helpdesk
    ("Zendesk", "zendesk.com", ["https://developer.zendesk.com/api-reference/", "https://developer.zendesk.com/api-reference/introduction/security-and-auth/"]),
    ("Intercom", "intercom.com", ["https://developers.intercom.com/docs", "https://developers.intercom.com/docs/build-an-integration/learn-more/authentication"]),
    ("Freshdesk", "freshdesk.com", ["https://developers.freshdesk.com/api/"]),
    ("Front", "front.com", ["https://dev.frontapp.com/docs/welcome", "https://dev.frontapp.com/docs/authentication"]),
    ("Pylon", "usepylon.com", ["https://docs.usepylon.com/pylon-docs/developer/api", "https://docs.usepylon.com/pylon-docs/developer/api/authentication"]),
    ("LiveAgent", "liveagent.com", ["https://www.liveagent.com/api/"]),
    ("Plain", "plain.com", ["https://www.plain.com/docs/api-reference/graphql", "https://www.plain.com/docs/api-reference/graphql/authentication"]),
    ("Help Scout", "helpscout.com", ["https://developer.helpscout.com/mailbox-api/", "https://developer.helpscout.com/mailbox-api/overview/authentication/"]),
    ("Gorgias", "gorgias.com", ["https://developers.gorgias.com/reference/introduction", "https://developers.gorgias.com/docs/authentication"]),
    ("Gladly", "gladly.com", ["https://developer.gladly.com/rest/"]),
    # 3 Communications and Messaging
    ("Slack", "slack.com", ["https://api.slack.com/docs", "https://api.slack.com/authentication/oauth-v2", "https://api.slack.com/authentication/token-types"]),
    ("Twilio", "twilio.com", ["https://www.twilio.com/docs/usage/api", "https://www.twilio.com/docs/iam/api-keys"]),
    ("Zoho Cliq", "zoho.com/cliq", ["https://www.zoho.com/cliq/help/restapi/v2/"]),
    ("Lark (Larksuite)", "open.larksuite.com", ["https://open.larksuite.com/document/home/index", "https://open.larksuite.com/document/server-docs/api-call-guide/calling-process/get-access-token"]),
    ("Pumble", "pumble.com", ["https://pumble.com/help/integrations/add-pumble-apps/pumble-api-keys-integration/"]),
    ("Discord", "discord.com", ["https://discord.com/developers/docs/reference", "https://discord.com/developers/docs/topics/oauth2"]),
    ("Telegram", "core.telegram.org", ["https://core.telegram.org/bots/api", "https://core.telegram.org/api"]),
    ("WhatsApp Business", "developers.facebook.com/docs/whatsapp", ["https://developers.facebook.com/docs/whatsapp/cloud-api", "https://developers.facebook.com/docs/whatsapp/business-management-api/get-started"]),
    ("Aircall", "aircall.io", ["https://developer.aircall.io/api-references/", "https://developer.aircall.io/tutorials/basic-authentication/"]),
    ("Vonage", "developer.vonage.com", ["https://developer.vonage.com/en/getting-started/concepts/authentication"]),
    # 4 Marketing, Ads, Email and Social
    ("Google Ads", "developers.google.com/google-ads", ["https://developers.google.com/google-ads/api/docs/start", "https://developers.google.com/google-ads/api/docs/api-policy/developer-token", "https://developers.google.com/google-ads/api/docs/api-policy/access-levels"]),
    ("Meta Ads", "developers.facebook.com/docs/marketing-apis", ["https://developers.facebook.com/docs/marketing-apis", "https://developers.facebook.com/docs/marketing-api/overview/authorization"]),
    ("LinkedIn Ads", "learn.microsoft.com/linkedin/marketing", ["https://learn.microsoft.com/en-us/linkedin/marketing/", "https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access", "https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication"]),
    ("GoHighLevel", "highlevel.stoplight.io", ["https://highlevel.stoplight.io/docs/integrations", "https://marketplace.gohighlevel.com/docs/"]),
    ("Mailchimp", "mailchimp.com/developer", ["https://mailchimp.com/developer/marketing/docs/fundamentals/", "https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/"]),
    ("Klaviyo", "developers.klaviyo.com", ["https://developers.klaviyo.com/en/docs/authenticate_", "https://developers.klaviyo.com/en/reference/api_overview"]),
    ("systeme.io", "systeme.io (funnel builder)", ["https://developer.systeme.io/reference/api", "https://help.systeme.io/article/2323-how-to-create-a-public-api-key-on-systeme-io"]),
    ("Pinterest", "developers.pinterest.com", ["https://developers.pinterest.com/docs/getting-started/set-up-app/", "https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/"]),
    ("Threads (Meta)", "developers.facebook.com/docs/threads", ["https://developers.facebook.com/docs/threads", "https://developers.facebook.com/docs/threads/get-started"]),
    ("SendGrid", "sendgrid.com", ["https://www.twilio.com/docs/sendgrid/api-reference", "https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys"]),
    # 5 Ecommerce
    ("Shopify", "shopify.dev", ["https://shopify.dev/docs/api/admin-graphql", "https://shopify.dev/docs/apps/build/authentication-authorization"]),
    ("WooCommerce", "woocommerce.com/document/woocommerce-rest-api", ["https://woocommerce.com/document/woocommerce-rest-api/", "https://woocommerce.github.io/woocommerce-rest-api-docs/"]),
    ("BigCommerce", "developer.bigcommerce.com", ["https://developer.bigcommerce.com/docs/start/authentication", "https://developer.bigcommerce.com/docs/start/authentication/api-accounts"]),
    ("Salesforce Commerce Cloud", "developer.salesforce.com/docs/commerce", ["https://developer.salesforce.com/docs/commerce/commerce-api/overview", "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-shopper-apis.html"]),
    ("Magento (Adobe Commerce)", "developer.adobe.com/commerce", ["https://developer.adobe.com/commerce/webapi/get-started/authentication/", "https://developer.adobe.com/commerce/webapi/rest/"]),
    ("Squarespace", "developers.squarespace.com", ["https://developers.squarespace.com/commerce-apis/overview", "https://developers.squarespace.com/commerce-apis/authentication-and-permissions"]),
    ("Ecwid", "api-docs.ecwid.com", ["https://api-docs.ecwid.com/reference/overview", "https://api-docs.ecwid.com/docs/get-access-token"]),
    ("Gumroad", "gumroad.com/api", ["https://gumroad.com/api", "https://app.gumroad.com/api"]),
    ("Amazon Selling Partner", "developer-docs.amazon.com/sp-api", ["https://developer-docs.amazon.com/sp-api/docs/welcome", "https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer"]),
    ("fanbasis", "fanbasis.com", ["https://www.fanbasis.com/"]),
    # 6 Data, SEO and Scraping
    ("DataForSEO", "docs.dataforseo.com", ["https://docs.dataforseo.com/v3/", "https://docs.dataforseo.com/v3/auth/"]),
    ("SE Ranking", "seranking.com/api", ["https://seranking.com/api.html"]),
    ("Ahrefs", "ahrefs.com/api", ["https://ahrefs.com/api", "https://docs.ahrefs.com/docs/api/reference/introduction"]),
    ("MrScraper", "docs.mrscraper.com", ["https://docs.mrscraper.com/"]),
    ("Apify", "docs.apify.com", ["https://docs.apify.com/api/v2", "https://docs.apify.com/platform/integrations/api"]),
    ("Firecrawl", "firecrawl.dev", ["https://docs.firecrawl.dev/introduction", "https://docs.firecrawl.dev/mcp-server"]),
    ("Bright Data", "brightdata.com", ["https://docs.brightdata.com/api-reference/introduction", "https://docs.brightdata.com/mcp-server/overview"]),
    ("Sherlock", "github.com/sherlock-project/sherlock", ["https://github.com/sherlock-project/sherlock"]),
    ("Waterfall.io", "waterfall.io (contact/company intel)", ["https://waterfall.io/"]),
    ("Clay", "clay.com", ["https://www.clay.com/", "https://university.clay.com/docs/http-api-integration-overview"]),
    # 7 Developer, Infra and Data platforms
    ("GitHub", "docs.github.com/rest", ["https://docs.github.com/en/rest", "https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api", "https://docs.github.com/en/graphql"]),
    ("Vercel", "vercel.com/docs/rest-api", ["https://vercel.com/docs/rest-api", "https://vercel.com/docs/rest-api/reference/welcome"]),
    ("Netlify", "docs.netlify.com/api", ["https://docs.netlify.com/api/get-started/"]),
    ("Cloudflare", "developers.cloudflare.com/api", ["https://developers.cloudflare.com/api/", "https://developers.cloudflare.com/fundamentals/api/get-started/create-token/"]),
    ("Supabase", "supabase.com/docs", ["https://supabase.com/docs/reference/api/introduction", "https://supabase.com/docs/guides/api/api-keys", "https://supabase.com/docs/guides/getting-started/mcp"]),
    ("Neo4j", "neo4j.com/docs/api", ["https://neo4j.com/docs/api/", "https://neo4j.com/docs/aura/platform/api/overview/", "https://neo4j.com/docs/query-api/current/"]),
    ("Snowflake", "docs.snowflake.com", ["https://docs.snowflake.com/en/developer-guide/sql-api/index", "https://docs.snowflake.com/en/developer-guide/sql-api/authenticating"]),
    ("MongoDB Atlas", "mongodb.com/docs/atlas/api", ["https://www.mongodb.com/docs/atlas/api/", "https://www.mongodb.com/docs/atlas/configure-api-access/"]),
    ("Datadog", "docs.datadoghq.com/api", ["https://docs.datadoghq.com/api/latest/", "https://docs.datadoghq.com/account_management/api-app-keys/"]),
    ("Sentry", "docs.sentry.io/api", ["https://docs.sentry.io/api/", "https://docs.sentry.io/api/auth/"]),
    # 8 Productivity and Project Management
    ("Notion", "developers.notion.com", ["https://developers.notion.com/reference/intro", "https://developers.notion.com/docs/authorization"]),
    ("Airtable", "airtable.com/developers", ["https://airtable.com/developers/web/api/introduction", "https://airtable.com/developers/web/api/authentication"]),
    ("Linear", "developers.linear.app", ["https://linear.app/developers", "https://linear.app/developers/graphql"]),
    ("Jira", "developer.atlassian.com", ["https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/", "https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/"]),
    ("Asana", "developers.asana.com", ["https://developers.asana.com/docs/overview", "https://developers.asana.com/docs/authentication"]),
    ("Monday.com", "developer.monday.com", ["https://developer.monday.com/api-reference/docs", "https://developer.monday.com/api-reference/docs/authentication"]),
    ("ClickUp", "clickup.com/api", ["https://developer.clickup.com/docs/authentication", "https://clickup.com/api"]),
    ("Coda", "coda.io/developers", ["https://coda.io/developers/apis/v1"]),
    ("Smartsheet", "smartsheet.com/developers", ["https://developers.smartsheet.com/api/smartsheet/introduction"]),
    ("Harvest", "harvestapp.com (help.getharvest.com/api-v2)", ["https://help.getharvest.com/api-v2/", "https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/"]),
    # 9 Finance and Fintech
    ("Stripe", "stripe.com/docs/api", ["https://docs.stripe.com/api", "https://docs.stripe.com/api/authentication", "https://docs.stripe.com/mcp"]),
    ("Plaid", "plaid.com/docs", ["https://plaid.com/docs/api/", "https://plaid.com/docs/quickstart/"]),
    ("Binance", "binance-docs.github.io", ["https://developers.binance.com/docs/binance-spot-api-docs/rest-api", "https://binance-docs.github.io/apidocs/spot/en/"]),
    ("Paygent Connect", "paygent (NMI-powered)", ["https://docs.nmi.com/reference/introduction"]),
    ("iPayX", "ipayx.ai/docs", ["https://ipayx.ai/docs"]),
    ("QuickBooks", "developer.intuit.com", ["https://developer.intuit.com/app/developer/qbo/docs/get-started", "https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0"]),
    ("Xero", "developer.xero.com", ["https://developer.xero.com/documentation/getting-started-guide/", "https://developer.xero.com/documentation/guides/oauth2/overview/"]),
    ("Brex", "developer.brex.com", ["https://developer.brex.com/", "https://developer.brex.com/docs/authentication/"]),
    ("Ramp", "docs.ramp.com", ["https://docs.ramp.com/developer-api/v1/overview/introduction", "https://docs.ramp.com/developer-api/v1/authorization"]),
    ("PitchBook", "pitchbook.com (research API)", ["https://pitchbook.com/data/api", "https://pitchbook.com/data"]),
    # 10 AI, Research and Media-native
    ("NotebookLM", "cloud.google.com/gemini (Enterprise API)", ["https://cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks", "https://cloud.google.com/agentspace/notebooklm-enterprise/docs/overview"]),
    ("Otter AI", "help.otter.ai (MCP server)", ["https://help.otter.ai/"]),
    ("Fathom", "fathom.video", ["https://developers.fathom.ai/quickstart", "https://help.fathom.video/en/articles/8368641", "https://fathom.video/"]),
    ("Consensus", "consensus.app (OAuth requested)", ["https://consensus.app/", "https://docs.consensus.app/"]),
    ("Reducto", "reducto.ai (document parsing)", ["https://docs.reducto.ai/"]),
    ("Devin", "docs.devin.ai (MCP)", ["https://docs.devin.ai/api-reference/overview", "https://docs.devin.ai/work-with-devin/deepwiki-mcp"]),
    ("higgsfield", "higgsfield.ai/cli (content suite)", ["https://higgsfield.ai/cli", "https://docs.higgsfield.ai/quickstart", "https://docs.higgsfield.ai/docs/authentication.md"]),
    ("Mermaid CLI", "github.com/mermaid-js/mermaid-cli", ["https://github.com/mermaid-js/mermaid-cli"]),
    ("YouTube Transcript", "transcriptapi.com", ["https://transcriptapi.com/", "https://transcriptapi.com/docs"]),
    ("Grain", "grain.com (meeting notes)", ["https://grain.com/", "https://developers.grain.com/", "https://support.grain.com/en/articles/15507288-grain-api"]),
]

assert len(APPS) == 100, len(APPS)
names = [a[0] for a in APPS]
assert len(set(names)) == 100, "duplicate app names"

out = []
for i, (name, hint, seeds) in enumerate(APPS, start=1):
    out.append({
        "id": i,
        "name": name,
        "category": C[(i - 1) // 10 + 1],
        "hint": hint,
        "seed_urls": seeds,
    })

Path(__file__).with_name("apps.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print(f"wrote {len(out)} apps")
