
## [1] Salesforce — CRM and Sales
heuristic: auth=['OAuth2', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 2935c https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm
  page 200 render 681c https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm
  page 200 direct 48315c https://salesforce.com
  page 200 direct 3394c https://developer.salesforce.com/docs/platform/api-rest/guide/intro-oauth-and-connected-apps.html
  page 200 render 1726c https://iis.digital.salesforce.com/services/auth/login?client_id=BbJrTZE7ZEre8FIZJt1gWkJ8x5ps6wNWheOWdV1qKsaM6rlrygniAO2KQp0yZiwi0YebkVaRnS3fvJvY1nqKH&offerId=free-trial-00005820&offerType=free-trial&offerStatus=PUBLISHED&locale=EN_IN
  page 200 direct 36697c https://www.salesforce.com/in/agentforce/pricing/
  page 200 direct 27578c https://www.salesforce.com/in/sales/pricing/
  page 200 direct 47531c https://www.salesforce.com/in/service/pricing/
  page 200 direct 36097c https://www.salesforce.com/in/marketing/pricing/
  page 200 direct 547c https://developer.salesforce.com/llms.txt
  page 401 direct 0c https://help.salesforce.com/llms.txt ERR HTTP 401
  - auth_methods | Supports OAuth2 | https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm
      “I Architecture REST API follows the standard RESTful principles and characteristics. Authorization Through External Client Apps or Connected Apps and OAuth 2.0 For a client application to access REST API resources, it must be authorized as a safe visitor. To i”
  - auth_methods | Supports OAuth2 | https://developer.salesforce.com/docs/platform/api-rest/guide/intro-oauth-and-connected-apps.html
      “Authorization Through External Client Apps or Connected Apps and OAuth 2.0 For a client application to access REST API resources, it must be authorized as a safe visitor. To implement this authorization, use either an extern”
  - auth_methods | Supports Other | https://developer.salesforce.com/docs/platform/api-rest/guide/intro-oauth-and-connected-apps.html
      “API request must include these headers: Authorization: The DPoP-bound access token with the DPoP prefix instead of Bearer. DPoP: A signed DPoP proof JWT for this request. If a request sends a DPoP proof with an access token that isn’t DPoP-bound, Salesforce re”
  - api_type | REST API documented | https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm
      “Introduction to REST API REST API provides you with programmatic access to your data in Salesforce. The flexibility and scalability of REST API make it an excellent choice fo”
  - api_type | REST API documented | https://salesforce.com
      “nd hold times. Extend agents anywhere customers are: On the web, on the phone, or in apps. Let humans do what they do best, and let Agentforce do the rest. Watch demos See pricing details Learn more about the Agentforce Platform Agentforce Voice Agentforce Voi”
  - credential_access | Access signal: partner_gated | https://salesforce.com
      “pps & Experts Get the most out of Salesforce with partners, apps, solutions and consultants.About our partners AgentExchange Partner Apps Consultants Become a Partner Pricing Product Support See all products Discover the #1 AI CRM Humans with Agents drive cust”
  - credential_access | Access signal: partner_gated | https://developer.salesforce.com/docs/platform/api-rest/guide/intro-oauth-and-connected-apps.html
      “g connected apps during and after Spring ‘26. However, we recommend using external client apps instead. If you must continue creating connected apps, contact Salesforce Support. See New connected apps can no longer be created in Spring ‘26 for more details. Bo”
  - credential_access | Access signal: trial | https://salesforce.com
      “rce Academic Programs Discover free curriculum and resources for students and educators. Try Salesforce for Free Back Try Salesforce for Free Explore free trial offers for Salesforce data, analytics, and CRM products — for any size business, in any industry.Ge”
  - credential_access | Access signal: trial | https://www.salesforce.com/in/agentforce/pricing/
      “rce Academic Programs Discover free curriculum and resources for students and educators. Try Salesforce for Free Back Try Salesforce for Free Explore free trial offers for Salesforce data, analytics, and CRM products — for any size business, in any industry.Ge”
  - credential_access | Access signal: free | https://salesforce.com
      “re Report The Agentic Enterprise Index Learn more about Agentforce Learn more Report State of Agentic AI Learn more about Agentforce Learn more No credit card needed · No software to install Get a head start on building your Agentic Enterprise Experience the f”
  - credential_access | Access signal: free | https://www.salesforce.com/in/sales/pricing/
      “ion Limited Data Cloud features *Limited Flex Credits and Data 360 Credits included in Foundations. Additional credits available for purchase. *Slack Free plan; other Slack plans available for purchase. Estimate your return before you choose See potential reve”
  - credential_access | Access signal: enterprise | https://www.salesforce.com/in/agentforce/pricing/
      “ollar (AUD) British Pound (GBP) Euro (EUR) Japanese Yen (JPY) Swedish Krona (SEK) Salesforce Foundations Add key features to your existing CRM, available for Enterprise Edition and above. $ 0 $ 0 0 € AU$ 0 0 円 0 kr £ 0 Agentforce Builder Prompt Builder Agent S”
  - credential_access | Access signal: enterprise | https://www.salesforce.com/in/sales/pricing/
      “ck, Tableau, Data 360 and Premier Success are now included in every edition. How do the new editions compare to the ones I have today? Core replaces Enterprise Edition, Advanced replaces Unlimited Edition, and Max replaces Agentforce 1 Edition. Each new editio”
  - mcp_available | MCP mentioned in vendor docs | https://salesforce.com
      “sforce architecture. Explore Headless Toolkit Claudeforce Put Salesforce to work inside Claude. Salesforce in Claude combines a prebuilt Salesforce MCP server with 37 ready-to-use sales skills, from prospecting to pipeline hygiene — bringing Salesforce context”
  - mcp_available | MCP registry entry: ai.cirra/salesforce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=salesforce&limit=60
      “https://github.com/cirra-ai/mcp-server”
  - mcp_available | MCP registry entry: ai.cirra/salesforce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=salesforce&limit=60
      “”
  - mcp_available | MCP registry entry: ai.cirra/salesforce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=salesforce&limit=60
      “”

## [2] HubSpot — CRM and Sales
heuristic: auth=['OAuth2', 'Personal Access Token'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 2754c https://developers.hubspot.com/docs/api/overview
  page 200 direct 11628c https://developers.hubspot.com/docs/api/oauth-quickstart-guide
  page 200 direct 9844c https://developers.hubspot.com/docs/api/private-apps
  page 200 direct 14648c https://hubspot.com
  page 200 direct 13120c https://developers.hubspot.com/docs/api-reference/latest/authentication/manage-oauth-tokens
  page 200 direct 3229c https://developers.hubspot.com/docs/getting-started/introduction
  page 200 direct 4075c https://developers.hubspot.com/docs/apps/developer-platform/overview
  page 200 direct 12775c https://developers.hubspot.com/docs/cms/start-building/introduction/overview
  page 200 direct 2754c https://developers.hubspot.com/docs/api-reference/latest/overview
  page 200 direct 2256c https://developers.hubspot.com/docs/developer-tooling/overview
  page 404 direct 0c https://developers.hubspot.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://developers.hubspot.com/docs/api/overview
      “ling Account & Settings Account information Audit Logs Brands IP ranges Settings App Management App Uninstalls Feature Flags Authentication API Guide OAuth tokens Automation Email templates Sequences Workflow actions CMS Blogs Content audit Domains HubDB Media”
  - auth_methods | Supports OAuth2 | https://developers.hubspot.com/docs/api/oauth-quickstart-guide
      “in content HubSpot docs home page Legacy Search...⌘KAsk Assistant⌘I Changelog Log In Sign up Sign up Search... Navigation Authentication Working with OAuth | OAuth Quickstart Guide Home Get Started Apps CMS APIs Developer Tooling Build with AI Overview Public ”
  - auth_methods | Supports Personal Access Token | https://developers.hubspot.com/docs/api/private-apps
      “rking with OAuth Scopes Request validation English close On this pageBack to top Feature limitations Make API calls with your app’s access token View private app access token information Rotate your access token View API call logs Private app limits Delete a p”
  - auth_methods | Supports Personal Access Token | https://developers.hubspot.com/docs/apps/developer-platform/overview
      “ge of the latest app features, existing legacy private apps and public apps are still currently supported. All REST APIs are available to query via a private app access token or public app OAuth token. New legacy apps cannot be created. Learn more about the le”
  - api_type | REST API documented | https://developers.hubspot.com/docs/api/overview
      “the previous 2026-03 API version. All endpoints in this section follow the pattern: /api-name/2026-09/resource For example, to retrieve all contacts: GET /crm/objects/2026-09/contacts All APIs, whether legacy, new, or beta, use the same root path as before: ht”
  - api_type | REST API documented | https://developers.hubspot.com/docs/apps/developer-platform/overview
      “m is highly recommended to take advantage of the latest app features, existing legacy private apps and public apps are still currently supported. All REST APIs are available to query via a private app access token or public app OAuth token. New legacy apps can”
  - credential_access | Access signal: trial | https://developers.hubspot.com/docs/api/oauth-quickstart-guide
      “new developer platform, check out this article instead. Before you get started Before you can start using OAuth with HubSpot, you’ll need to have: A developer account An app associated with your developer account A HubSpot account to install your app in (you c”
  - credential_access | Access signal: trial | https://developers.hubspot.com/docs/apps/developer-platform/overview
      “oncept app that uses a boilerplate example project and schema definition. You can then upload the associated configuration files to a project in your developer account, and test out an install using a developer test account. The app creation article linked abo”
  - credential_access | Access signal: partner_gated | https://hubspot.com
      “Skip to content English Select a language 日本語 Deutsch English Español Português Français High Contrast Customer Support Contact Sales Close Search Log in About About About Us Careers Contact Us Investor Relations Management Team Back Get a demo of HubSpot's pr”
  - credential_access | Access signal: free | https://hubspot.com
      “ose Search Log in About About About Us Careers Contact Us Investor Relations Management Team Back Get a demo of HubSpot's premium software Get started free with HubSpot's free tools Menu Close Search Products Products The HubSpot Customer Platform All of HubSp”
  - credential_access | Access signal: free | https://developers.hubspot.com/docs/cms/start-building/introduction/overview
      “is expected. Getting started If you’re just getting started with developing on HubSpot’s CMS, it’s recommended to begin with the following: Create a free developer account, then create a test account within it. This will give you a testing environment to build”
  - mcp_available | MCP mentioned in vendor docs | https://developers.hubspot.com/docs/getting-started/introduction
      “iew Authenticate API requests to retrieve and manage HubSpot data. Platform overview Discover the features available on HubSpot’s developer platform. MCP server Install HubSpot’s local development MCP server for AI-assisted coding in your IDE. Other resources ”
  - mcp_available | MCP mentioned in vendor docs | https://developers.hubspot.com/docs/apps/developer-platform/overview
      “ooling Build with AI Overview Developer seats Build apps Authentication Create an app Migrate an app App configuration Manage apps in HubSpot HubSpot MCP server Add features UI extensions App events App objects Agent tools Serverless functions MCP server Beta ”
  - mcp_available | MCP registry entry: com.edgethirteen.www/hubspot-dbv | https://registry.modelcontextprotocol.io/v0/servers?search=hubspot&limit=60
      “”
  - mcp_available | MCP registry entry: com.pronovahq/pronova-sales-hubspot | https://registry.modelcontextprotocol.io/v0/servers?search=hubspot&limit=60
      “”
  - mcp_available | MCP registry entry: dev.wirecat/hubspot-cli | https://registry.modelcontextprotocol.io/v0/servers?search=hubspot&limit=60
      “https://github.com/WireCatLabs/hubspot-cli”

## [3] Pipedrive — CRM and Sales
heuristic: auth=['OAuth2', 'Personal Access Token'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 2784c https://developers.pipedrive.com/docs/api/v1
  page 200 direct 3610c https://pipedrive.readme.io/docs/core-api-concepts-authentication
  page 200 direct 15522c https://pipedrive.com
  page 200 direct 6307c https://developers.pipedrive.com/docs/api/v1/Oauth
  page 200 direct 10298c https://www.pipedrive.com/en/pricing
  page 200 render 7020c https://app.pipedrive.com/auth/login
  page 200 direct 7514c https://www.pipedrive.com/en/features/mcp-server
  page 200 direct 460c https://developers.pipedrive.com/llms.txt
  page 200 direct 6954c https://pipedrive.readme.io/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.pipedrive.com/docs/api/v1
      “lments Deal products Deals Files Filters Goals Item search Lead fields Lead labels Leads Lead sources Legacy teams Mailbox Meetings Note fields Notes OAuth 2.0 Organization fields Organization relationships Organizations Permission sets Person fields Persons P”
  - auth_methods | Supports OAuth2 | https://pipedrive.readme.io/docs/core-api-concepts-authentication
      “ing app extension Implementing messaging app extension Error codes and troubleshooting APP FUNCTIONALITIES App sharing: Adding apps to multiple users OAuth 2.0 OAuth 2.0 overview OAuth authorization Scopes and permission explanations State parameter Getting us”
  - auth_methods | Supports Personal Access Token | https://developers.pipedrive.com/docs/api/v1
      “mat for output and is capable of handling CORS (Cross-Origin Resource Sharing) requests. The API is stateless – all requests are validated against an API token. The API token can be obtained manually from the Pipedrive app. OpenAPI 3 You can click on the "Run ”
  - auth_methods | Supports Personal Access Token | https://pipedrive.readme.io/docs/core-api-concepts-authentication
      “Webhooks v2 Webhooks v2 migration guide Guide for Webhooks Guide for optimizing API usage Subscriptions API migration guide Tutorials How to find the API token How to get the company domain Enabling API for company users Hello World Tutorial Adding an Activity”
  - api_type | REST API documented | https://developers.pipedrive.com/docs/api/v1
      “jects Project templates Recents Roles Stages Tasks User connections Users User settings Webhooks API Reference This reference helps you implement the RESTful Pipedrive API. This API uses a JSON format for output and is capable of handling CORS (Cross-Origin Re”
  - api_type | REST API documented | https://developers.pipedrive.com/docs/api/v1/Oauth
      “lters Goals Item search Lead fields Lead labels Leads Lead sources Legacy teams Mailbox Meetings Note fields Notes OAuth 2.0 Requesting authorization GET /oauth/authorize Getting the tokens POST /oauth/token Refreshing the tokens POST /oauth/token Organization”
  - credential_access | Access signal: partner_gated | https://developers.pipedrive.com/docs/api/v1
      “als or spam, just developer news. PipedriveAboutPricingJobsBlogNewsroom ProductSales softwareFeaturesPrivacy and securityMarketplaceStatusAPI DiscoverPartner ProgramSales Pipeline CourseWhat is CRM?CRM ComparisonResources Help CenterKnowledge BaseAcademy Suppo”
  - credential_access | Access signal: partner_gated | https://pipedrive.com
      “nagersDesignersSee all roles Resources About usJobsNewsroomPartnerStatusContact supportOnboardingKnowledge baseBlogLearnCRM HubDevelopersDownloadable Contact sales Pricing All categoriesMarketplace appsBlogKnowledge BaseAcademy All results: 0 No results found.”
  - credential_access | Access signal: trial | https://developers.pipedrive.com/docs/api/v1
      “nd subscribe to our Changelog . To test your applications, we recommend creating a new, separate Pipedrive account for sandboxing purposes. Go to the Developer Sandbox Account page to learn more and request your own sandbox account. Developer Documentation See”
  - credential_access | Access signal: trial | https://pipedrive.readme.io/docs/core-api-concepts-authentication
      “ve Developer Documentation API ReferenceTutorialsChangelogDev CommunityBlog Pipedrive Developer Documentation Authentication Overview Getting started Developer sandbox account Pipedrive API in Postman or Insomnia Creating an app create-pipedrive-app CLI Tutori”
  - credential_access | Access signal: free | https://pipedrive.com
      “rack your sales pipeline, optimize leads, manage deals with AI and automate your entire sales process so you can focus on selling. 14-day free trial, no credit card required Trusted by over 100,000 companies 500+ integrations to boost workflows Built-in AI to ”
  - credential_access | Access signal: free | https://www.pipedrive.com/en/pricing
      “t meeting intelligence handle the admin US$14 One payment of US$ 168 per seat/year Per seat per month, billed annually Try it free Free 14-day trial. No credit card required. Key features View and manage leads, deals, contacts, calendar events and more in one ”
  - mcp_available | MCP mentioned in vendor docs | https://www.pipedrive.com/en/features/mcp-server
      “lands Norsk Polski Română Русский Suomi Svenska ภาษาไทย Türkçe Українська Chinese (繁體中文)Log inTry it free Connect your AI assistant to Pipedrive with MCP Empower AI assistants like ChatGPT and Claude to securely and reliably work with your Pipedrive data. Find”
  - mcp_available | MCP registry entry: io.github.Servosity/pipedrive-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pipedrive&limit=60
      “https://github.com/servosity/msp-skills”
  - mcp_available | MCP registry entry: io.github.Servosity/pipedrive-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pipedrive&limit=60
      “https://github.com/servosity/msp-skills”
  - mcp_available | MCP registry entry: io.github.Servosity/pipedrive-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pipedrive&limit=60
      “https://github.com/servosity/msp-skills”

## [4] Attio — CRM and Sales
heuristic: auth=['OAuth2', 'API Key', 'Basic', 'Personal Access Token', 'Other'] api=['REST', 'GraphQL'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 70510c https://docs.attio.com/rest-api/overview
  page 200 direct 104613c https://docs.attio.com/rest-api/guides/authentication
  page 200 direct 11657c https://attio.com
  page 200 direct 217938c https://docs.attio.com/rest-api/tutorials/connect-an-app-through-oauth
  page 200 direct 25152c https://docs.attio.com/docs/overview
  page 200 direct 41857c https://docs.attio.com/sdk/overview
  page 200 direct 92692c https://docs.attio.com/mcp/overview
  page 200 direct 27064c https://docs.attio.com/sql/overview
  page 200 direct 80970c https://docs.attio.com/rest-api/guides/rate-limiting
  page 200 direct 73597c https://docs.attio.com/llms.txt
  - auth_methods | Supports OAuth2 | https://docs.attio.com/rest-api/overview
      “and sorting Linking referenced records Paginating API results Configuring webhooks Working with activities Tutorials Connect an app to Attio through OAuth Attribute types Overview Actor reference Checkbox Currency Date Domain Email address Interaction Location”
  - auth_methods | Supports OAuth2 | https://docs.attio.com/rest-api/guides/authentication
      “and sorting Linking referenced records Paginating API results Configuring webhooks Working with activities Tutorials Connect an app to Attio through OAuth Attribute types Overview Actor reference Checkbox Currency Date Domain Email address Interaction Location”
  - auth_methods | Supports API Key | https://docs.attio.com/rest-api/guides/authentication
      “ontent events Record events Task events Workspace member events On this pageBack to top Generating access tokens OAuth 2.0 OAuth for unpublished apps API key Using tokens Scopes Token levels Choosing the token level in the OAuth flow Guides Authenticating requ”
  - auth_methods | Supports API Key | https://docs.attio.com/mcp/overview
      “sktop, Claude.ai, ChatGPT, Cursor, etc.) Connecting to Attio MCP Attio MCP uses OAuth authentication, so you simply log in with your Attio account—no API keys required. Add as a Custom Connector In your AI tool of choice, add the following URL as a custom MCP ”
  - auth_methods | Supports Basic | https://docs.attio.com/rest-api/guides/authentication
      “the same way. Pass the value of the token in the Authorization header of your requests like so. Authorization: Bearer <access_token> We also support HTTP Basic Authentication, where the username is the token and the password is left blank. However, we recommen”
  - auth_methods | Supports Personal Access Token | https://docs.attio.com/sdk/overview
      “gs.getSettings() Settings.setSettings() GraphQL GraphQL runQuery() useQuery() Data fetching useAsyncCache() React Query Server Server functions Attio API Token Environment Variables Available Globals Connections Events Webhooks KV Store timingSafeEqual System ”
  - auth_methods | Supports Other | https://docs.attio.com/rest-api/overview
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - auth_methods | Supports Other | https://docs.attio.com/rest-api/guides/authentication
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - api_type | REST API documented | https://docs.attio.com/rest-api/overview
      “erated using AI and may contain mistakes. Attio Docs home page Search...⌘KAsk Assistant⌘I Search... Navigation Introduction Overview Overview App SDK REST API MCP SQL Share Changelog Developer console Support Introduction Overview Guides Authenticating request”
  - api_type | REST API documented | https://docs.attio.com/rest-api/guides/authentication
      “ing AI and may contain mistakes. Attio Docs home page Search...⌘KAsk Assistant⌘I Search... Navigation Guides Authenticating requests Overview App SDK REST API MCP SQL Share Changelog Developer console Support Introduction Overview Guides Authenticating request”
  - api_type | GraphQL API documented | https://docs.attio.com/sdk/overview
      “ttings.defineWorkspaceSchema() Settings.defineWorkspacePage() Settings.useForm() Settings.useSettings() Settings.getSettings() Settings.setSettings() GraphQL GraphQL runQuery() useQuery() Data fetching useAsyncCache() React Query Server Server functions Attio ”
  - credential_access | Access signal: admin_approval | https://docs.attio.com/rest-api/guides/authentication
      “oken with the token_level query parameter on the authorize URL. It accepts workspace or user. If you leave it out, the token is workspace-level. Only workspace admins can grant a workspace-level token. Any workspace member can grant a user-level token, as long”
  - credential_access | Access signal: admin_approval | https://docs.attio.com/sdk/overview
      “tio Workflows builder: subscribe to external events or call external APIs as part of a workflow run. Workspace settings Provide a settings page where workspace admins can configure your app. Apps can also link between their surfaces and records, call the Attio”
  - credential_access | Access signal: partner_gated | https://attio.com
      “P Connect everywhere you work Developer Platform Extend and integrate with Attio Attio for Slack ChatGPT Claude Get started Attio 101 Startup program Talk to sales Hire an expert Resources Support Help Center Learn about Attio's features Academy Essential Atti”
  - credential_access | Access signal: enterprise | https://docs.attio.com/sql/overview
      “d what filters and reports allow — joining across objects and lists, aggregating, and running ad-hoc analytical queries. SQL is only available on the Enterprise plan. Ways to query There are several ways to run SQL against your workspace: REST API: send a quer”
  - mcp_available | MCP mentioned in vendor docs | https://docs.attio.com/rest-api/overview
      “ing AI and may contain mistakes. Attio Docs home page Search...⌘KAsk Assistant⌘I Search... Navigation Introduction Overview Overview App SDK REST API MCP SQL Share Changelog Developer console Support Introduction Overview Guides Authenticating requests Handlin”
  - mcp_available | MCP mentioned in vendor docs | https://docs.attio.com/rest-api/guides/authentication
      “d may contain mistakes. Attio Docs home page Search...⌘KAsk Assistant⌘I Search... Navigation Guides Authenticating requests Overview App SDK REST API MCP SQL Share Changelog Developer console Support Introduction Overview Guides Authenticating requests Handlin”
  - mcp_available | MCP registry entry: ai.smithery/kaszek-kaszek-attio-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=attio&limit=60
      “”
  - mcp_available | MCP registry entry: ai.smithery/kesslerio-attio-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=attio&limit=60
      “https://github.com/kesslerio/attio-mcp-server”
  - mcp_available | MCP registry entry: ai.smithery/kesslerio-attio-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=attio&limit=60
      “https://github.com/kesslerio/attio-mcp-server”

## [5] Twenty — CRM and Sales
heuristic: auth=['OAuth2', 'API Key', 'Other'] api=['REST', 'GraphQL'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 63624c https://twenty.com/developers
  page 200 direct 55200c https://twenty.com/developers/section/api-and-webhooks/api
  page 200 direct 11582c https://twenty.com
  page 200 direct 80729c https://docs.twenty.com/developers/extend/oauth
  page 200 direct 52850c https://docs.twenty.com/getting-started/introduction
  page 200 direct 74252c https://docs.twenty.com/user-guide/introduction
  page 200 direct 63620c https://docs.twenty.com/developers/introduction
  page 200 direct 55200c https://docs.twenty.com/developers/extend/api
  page 200 direct 7574c https://twenty.com/pricing
  page 200 direct 2561c https://twenty.com/llms.txt
  - auth_methods | Supports OAuth2 | https://twenty.com/developers
      “Developers Build on Twenty Search...⌘K Developers Developers Apps Getting Started Tutorial Config Data Logic Layout Operations API Overview Webhooks OAuth Self-Host Docker Compose Setup Securing your instance Upgrade guide Troubleshooting Contribute Local Setu”
  - auth_methods | Supports OAuth2 | https://twenty.com/developers/section/api-and-webhooks/api
      “arch... Navigation API APIs Search...⌘K Developers Developers Apps Getting Started Tutorial Config Data Logic Layout Operations API Overview Webhooks OAuth Self-Host Docker Compose Setup Securing your instance Upgrade guide Troubleshooting Contribute Local Set”
  - auth_methods | Supports API Key | https://twenty.com/developers/section/api-and-webhooks/api
      “and field names directly — no opaque IDs. Your workspace-specific API documentation is available under Settings → Developers → API after creating an API key. It includes an interactive playground where you can execute real calls against your data. Two APIs Cor”
  - auth_methods | Supports API Key | https://docs.twenty.com/developers/extend/oauth
      “Clients are registered dynamically via RFC 7591 — no manual setup in a dashboard. When to Use OAuth Scenario Auth Method Internal scripts, automation API Key External app acting on behalf of a user OAuth — Authorization Code Server-to-server, no user context O”
  - auth_methods | Supports Other | https://twenty.com/developers
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - auth_methods | Supports Other | https://twenty.com/developers/section/api-and-webhooks/api
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - api_type | REST API documented | https://twenty.com/developers
      “e UI library. Apps Build objects, logic, interfaces and AI agents as TypeScript apps, from quick start to publishing. API Read and write records over REST and GraphQL, get webhooks when records change, and connect apps with OAuth. Self-Host Run Twenty on your ”
  - api_type | REST API documented | https://twenty.com/developers/section/api-and-webhooks/api
      “ring your instance Upgrade guide Troubleshooting Contribute Local Setup Commands Style Guide UI Library Guides Primitives Components English API APIs REST and GraphQL APIs generated from your workspace schema. Schema-per-tenant APIs There is no static API refe”
  - api_type | GraphQL API documented | https://twenty.com/developers
      “ary. Apps Build objects, logic, interfaces and AI agents as TypeScript apps, from quick start to publishing. API Read and write records over REST and GraphQL, get webhooks when records change, and connect apps with OAuth. Self-Host Run Twenty on your own infra”
  - api_type | GraphQL API documented | https://twenty.com/developers/section/api-and-webhooks/api
      “instance Upgrade guide Troubleshooting Contribute Local Setup Commands Style Guide UI Library Guides Primitives Components English API APIs REST and GraphQL APIs generated from your workspace schema. Schema-per-tenant APIs There is no static API reference for ”
  - credential_access | Access signal: free | https://twenty.com/developers
      “s can bring conversations into Twenty’s messages, write to record timelines, and expose functions to workflows and AI agents. No ceiling. The core is open source and self-hostable. When an extension point is missing, change Twenty itself or contribute it back.”
  - credential_access | Access signal: free | https://twenty.com
      “imited customization using the AI coding tools you already love. Adapt your CRM to fit the way your business grows and wins. Stay in control with our open-source software Don't get locked into someone else's ecosystem. Twenty's developer experience looks like ”
  - credential_access | Access signal: partner_gated | https://twenty.com/pricing
      “ted support & SLA Security tailored to your ITVPN, your own AI providers and more Enterprise procurement supportSecurity reviews and custom contracts Talk to sales Need help with customization? Find the right partner to implement, customize, and tailor Twenty ”
  - credential_access | Access signal: trial | https://twenty.com/pricing
      “Product Resources Customers Pricing61.2K7.5K Log inGet started Get started Simple Pricing Start your free trial today without credit card. MonthlyYearly-25% Self-hosting Pro A custom agentic CRM for one team. $9/user/month Includes Emails and meetings log them”
  - mcp_available | MCP mentioned in vendor docs | https://twenty.com
      “on, all in TypeScript, deployable to any workspace. Does Twenty work with Claude, ChatGPT, and Cursor? Yes. Every Cloud workspace ships with a native MCP server. Connect your AI assistant via OAuth and it can read and write your CRM data in natural language. W”
  - mcp_available | MCP mentioned in vendor docs | https://docs.twenty.com/getting-started/introduction
      “platform you can build on, not a product you configure. Built for Agents Agents operate inside your data model with real permissions. Skills, Tools, MCP. Secured Extensibility The flexibility of vibe-coded tools on secured foundations. Modern Stack React, Type”
  - mcp_available | MCP registry entry: com.twentyclubs.mcp/premier-league | https://registry.modelcontextprotocol.io/v0/servers?search=twenty&limit=60
      “”
  - mcp_available | MCP registry entry: io.github.21-million-wall/twentyone-million | https://registry.modelcontextprotocol.io/v0/servers?search=twenty&limit=60
      “https://github.com/21-million-wall/twentyone-million”
  - mcp_available | MCP registry entry: io.github.h3692/eightytwenty | https://registry.modelcontextprotocol.io/v0/servers?search=twenty&limit=60
      “https://github.com/h3692/eightytwenty”

## [6] Podio — CRM and Sales
heuristic: auth=['OAuth2', 'API Key'] api=[] access=Unclear mcp=None found verdict=Insufficient evidence llms_txt=False
  page 200 direct 2239c https://developers.podio.com/
  page 200 direct 4844c https://developers.podio.com/authentication
  page 200 direct 7312c https://podio.com
  page 200 direct 859c https://developers.podio.com/api-key
  page 200 direct 2438c https://developers.podio.com/index/overview
  page 200 direct 2951c https://developers.podio.com/index/limits
  page 200 direct 4551c https://developers.podio.com/doc
  page 200 direct 5106c https://developers.podio.com/authentication/scopes
  page 200 direct 5964c https://developers.podio.com/authentication/server_side
  page 500 direct 0c https://developers.podio.com/llms.txt ERR HTTP 500
  - auth_methods | Supports OAuth2 | https://developers.podio.com/authentication
      “w API Reference Tutorials Client Libraries Developer Forums Partner Extensions Terms of Use How to authenticate with Podio API The Podio API uses the OAuth2 protocol for authentication. This allows external apps to request authorization to Podio without having”
  - auth_methods | Supports OAuth2 | https://developers.podio.com/doc
      “s Contacts Conversations Devices Email Embeds Files Flows Forms Friends Grants Hooks Importer Integrations Items Layout Linked Accounts Notifications OAuth authorization Organizations Questions Ratings Recurrence Reference Reminders Search Space members Spaces”
  - auth_methods | Supports API Key | https://developers.podio.com/
      “Pricing What people say Blog About App Market Log in Getting started The core concepts of Podio API conventions and structure Rate limits FAQ Get an API key Authentication API Reference Tutorials Client Libraries Developer Forums Partner Extensions Terms of Us”
  - auth_methods | Supports API Key | https://developers.podio.com/authentication
      “Podio Home Pricing What people say Blog About App Market Log in Getting started Get an API key Authentication Scopes & Permissions Server-side flow Client-side flow Username & password flow App authentication flow API Reference Tutorials Client”

## [7] Zoho CRM — CRM and Sales
heuristic: auth=['OAuth2'] api=[] access=Partnership / contact-sales gated mcp=Official verdict=Insufficient evidence llms_txt=True
  page 200 render 30930c https://www.zoho.com/crm/developer/docs/api/v8/
  page 200 direct 2681c https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html
  page 200 direct 5553c https://zoho.com/crm
  page 200 direct 4629c https://www.zoho.com/accounts/oneauth/?src=zGlobalAllProducts&category=securityanditmanagement
  page 200 direct 13809c https://www.zoho.com/mcp/?src=zGlobalAllProducts&category=developerplatforms
  page 200 direct 13809c https://www.zoho.com/mcp/?src=zGlobalAllProducts&category=ai-infra
  page 200 direct 17827c https://www.zoho.com/crm/zohocrm-pricing.html?source_from=crm_home
  page 200 direct 3697c https://www.zoho.com/crm/resources/guided-tour/zoho-crm-overview.html?source_from=crm_home
  page 200 direct 38670c https://www.zoho.com/llms.txt
  - auth_methods | Supports OAuth2 | https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html
      “OAuth 2.0 for V8 APIs - An Overview The Zoho CRM API uses the OAuth 2.0 protocol for authentication. OAuth 2.0 is an industry-standard protocol specification t”
  - auth_methods | Supports OAuth2 | https://www.zoho.com/mcp/?src=zGlobalAllProducts&category=developerplatforms
      “ace Consistent patterns across all Zoho applications. Drop-in compatible Works immediately with agent frameworks and tools. Secure, permission-scoped OAuth-based authorization ensures proper access control. How it works MCP provides a standardized way for AI A”
  - credential_access | Access signal: partner_gated | https://zoho.com/crm
      “happy to demonstrate Zoho CRM through a web-conference at your convenience. The demo is a one hour session. To schedule your personal session, please contact sales@zohocorp.com.”
  - credential_access | Access signal: partner_gated | https://www.zoho.com/crm/zohocrm-pricing.html?source_from=crm_home
      “happy to demonstrate Zoho CRM through a web-conference at your convenience. The demo is a one hour session. To schedule your personal session, please contact sales@zohocorp.com. Is my data safe? We’re fervent about keeping your data safe and secure. Our facili”
  - credential_access | Access signal: trial | https://zoho.com/crm
      “o get ahead without the overhead.GET STARTED Challenger in 2026 Magic Quadrant™ for CRM Sales Platforms Read more Get started with your flexible free trial Trusted by 350K+ businesses worldwide Supercharge your sales with Zia Agents Harness the power of a mult”
  - credential_access | Access signal: trial | https://www.zoho.com/crm/zohocrm-pricing.html?source_from=crm_home
      “available within team modules, but can only be accessed by fully licensed users Want to try team users? If you are a new user, you can sign up for a free trial of Zoho CRM and add team users from the Setup page. If you are an existing customer, or you're makin”
  - credential_access | Access signal: free | https://zoho.com/crm
      “solutions to learn more, and book a personalized demo to understand how Zoho CRM can be customized to meet your business needs. Does Zoho CRM have a free plan? Zoho CRM's freemium edition supports up to 3 users and comes with the essentials like leads, documen”
  - credential_access | Access signal: free | https://www.zoho.com/mcp/?src=zGlobalAllProducts&category=developerplatforms
      “Apps weren’t built for AI agentsuntil now.Sign Up for Free Just prompt—or don’t prompt—and watch work get done. For decades, business apps have made users click type toggle and chase That ends now Meet Zoho”
  - mcp_available | MCP mentioned in vendor docs | https://www.zoho.com/crm/developer/docs/api/v8/
      “ored for your needs. [Embedded BI](https://www.zoho.com/analytics/embedded-solutions.html?src=zGlobalAllProducts&category=developerplatforms) ##### MCP Make apps agent-ready, build agentic workflows, and get work done with prompts. [MCP](https://www.zoho.com/m”
  - mcp_available | MCP mentioned in vendor docs | https://www.zoho.com/mcp/?src=zGlobalAllProducts&category=developerplatforms
      “Just prompt—or don’t prompt—and watch work get done. For decades, business apps have made users click type toggle and chase That ends now Meet Zoho MCP (Model Context Protocol), which enables developers to instantly transform business apps into intelligent, ag”
  - mcp_available | MCP registry entry: com.devart/mcp-zohocrm | https://registry.modelcontextprotocol.io/v0/servers?search=zoho&limit=60
      “https://github.com/devart-ai-connectivity/devart-mcp-server-zoho-crm”
  - mcp_available | MCP registry entry: io.github.asklokesh/zoho-crm-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=zoho&limit=60
      “https://github.com/asklokesh/zoho-crm-mcp-server”
  - mcp_available | MCP registry entry: io.github.pipeworx-io/zoho_crm | https://registry.modelcontextprotocol.io/v0/servers?search=zoho&limit=60
      “https://github.com/pipeworx-io/mcp-zoho_crm”

## [8] Close — CRM and Sales
heuristic: auth=['OAuth2', 'API Key', 'Basic'] api=['REST'] access=Self-serve (paid plan required) mcp=Official verdict=Buildable with limitations llms_txt=True
  page 200 direct 2885c https://developer.close.com/
  page 200 direct 13763c https://developer.close.com/topics/authentication/
  page 200 direct 34444c https://close.com
  page 200 direct 13763c https://developer.close.com/api/overview/api-key-authentication
  page 200 direct 3092c https://developer.close.com/integrations/create-an-oauth-app
  page 200 direct 14310c https://developer.close.com/api/overview
  page 200 direct 8884c https://developer.close.com/mcp
  page 200 direct 14310c https://developer.close.com/api
  page 200 direct 3901c https://developer.close.com/integrations
  page 200 direct 62104c https://developer.close.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developer.close.com/
      “AI agents need. REST API Reference Full endpoint docs with schemas, examples, and an interactive API explorer. Authentication API keys for scripts or OAuth 2.0 for user-facing integrations. Webhooks & Events Real-time event notifications and a 30-day event log”
  - auth_methods | Supports OAuth2 | https://developer.close.com/topics/authentication/
      “ore actions API keys are best used for scripts and simple integrations that are internal to your organization. Alternatively, see Authentication with OAuth instead. Getting an API key API keys can be created and managed in your Close account under Settings → D”
  - auth_methods | Supports API Key | https://developer.close.com/
      “everything you or your AI agents need. REST API Reference Full endpoint docs with schemas, examples, and an interactive API explorer. Authentication API keys for scripts or OAuth 2.0 for user-facing integrations. Webhooks & Events Real-time event notifications”
  - auth_methods | Supports API Key | https://developer.close.com/topics/authentication/
      “n version of any page. Search /Ask AIHomepageProduct HelpLog inTry for Free Developers HomeAPI ReferenceMCPSkip to navigation On this page Getting an API key Perform API calls with API key cURL example Scroll to top Getting Started Authentication with API keys”
  - auth_methods | Supports Basic | https://developer.close.com/topics/authentication/
      “calls with API key cURL example Scroll to top Getting Started Authentication with API keys How to authenticate Close API requests using API keys with HTTP Basic Auth. Ask a question|Copy page|View as Markdown|More actions API keys are best used for scripts and”
  - auth_methods | Supports Basic | https://developer.close.com/api/overview/api-key-authentication
      “calls with API key cURL example Scroll to top Getting Started Authentication with API keys How to authenticate Close API requests using API keys with HTTP Basic Auth. Ask a question|Copy page|View as Markdown|More actions API keys are best used for scripts and”
  - api_type | REST API documented | https://developer.close.com/
      “ustomer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need. REST API Reference Full endpoint docs with schemas, examples, and an interactive API explorer. Authentication ”
  - api_type | REST API documented | https://developer.close.com/topics/authentication/
      “e.com/api/v1/me/ -u yourapikey: Notice the ’:’ at the end of the api key. This is used because the key is sent as the username with a blank password. GET /api/v1/me/ HTTP/1.1 Authorization: Basic eW91cmFwaWtleTo= Host: api.close.com This results in the header ”
  - credential_access | Access signal: free | https://developer.close.com/
      “ome Build an Integration Overview Create an OAuth App Publish External Links Integrations Directory Product Help Product Updates Making of Close Blog Open Source (GitHub) Developers Home Overview Create an OAuth App Publish Product OverviewCommunicationAutomat”
  - credential_access | Access signal: free | https://developer.close.com/integrations/create-an-oauth-app
      “ome Build an Integration Overview Create an OAuth App Publish External Links Integrations Directory Product Help Product Updates Making of Close Blog Open Source (GitHub) Developers Home Overview Create an OAuth App Publish Product OverviewCommunicationAutomat”
  - credential_access | Access signal: paid_plan | https://close.com
      “117 leads and 1.8k conversations via Close ✓ Most Closed Lost leads cite cost per seat and lack of workflow automation as reasons for not pursuing a paid subscription. Start with leads who specifically cited missing automation. Want me to draft re-engagement e”
  - mcp_available | MCP mentioned in vendor docs | https://developer.close.com/
      “uthentication API keys for scripts or OAuth 2.0 for user-facing integrations. Webhooks & Events Real-time event notifications and a 30-day event log. MCP Server Model Context Protocol for AI agents. Build an Integration Create an OAuth app, connect your produc”
  - mcp_available | MCP mentioned in vendor docs | https://close.com
      “line, activity, forecasting FormsCapture leads straight into Close IntegrationsChatGPT, Claude, WhatsApp, and 100+ more ChatGPT + ClaudeUse Close via MCP or API Services Expert help from the Close team All ServicesPut AI to work across your revenue team AI Rev”
  - mcp_available | MCP registry entry: ai.salescloser/salescloser | https://registry.modelcontextprotocol.io/v0/servers?search=close&limit=60
      “”
  - mcp_available | MCP registry entry: city.close/close-api | https://registry.modelcontextprotocol.io/v0/servers?search=close&limit=60
      “https://github.com/henryspatialanalysis/wtm.api”
  - mcp_available | MCP registry entry: city.close/close-api | https://registry.modelcontextprotocol.io/v0/servers?search=close&limit=60
      “https://github.com/henryspatialanalysis/wtm.api”

## [9] Copper — CRM and Sales
heuristic: auth=['OAuth2', 'API Key', 'Personal Access Token'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 5728c https://developer.copper.com/
  page 200 direct 13674c https://copper.com
  page 200 direct 4488c https://developer.copper.com/introduction/authentication.html
  page 200 direct 7274c https://developer.copper.com/introduction/oauth/index.html
  page 200 direct 5891c https://developer.copper.com/introduction/oauth/quickstart.html
  page 200 direct 8924c https://developer.copper.com/introduction/oauth/flow.html
  page 200 direct 5728c https://developer.copper.com/index.html
  page 200 direct 4670c https://developer.copper.com/introduction/requests.html
  page 404 direct 0c https://developer.copper.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://developer.copper.com/
      “Domain Update ⚠️ Change Policy Postman Resources Import the Collection Import and Use the Environment Authentication Authentication Overview OAuth2.0 OAuth2.0 Overview Quickstart Guide Documentation Requests Responses Search Paginating search results Best prac”
  - auth_methods | Supports OAuth2 | https://developer.copper.com/introduction/authentication.html
      “Copper Developer API Introduction Introduction Getting started Authentication Authentication Overview Overview Table of contents API Keys OAuth2.0 OAuth2.0 OAuth2.0 Overview Quickstart Guide Documentation Requests Responses Search Paginating search results Bes”
  - auth_methods | Supports API Key | https://developer.copper.com/introduction/authentication.html
      “ing search Copper Developer API Introduction Introduction Getting started Authentication Authentication Overview Overview Table of contents API Keys OAuth2.0 OAuth2.0 OAuth2.0 Overview Quickstart Guide Documentation Requests Responses Search Paginating search ”
  - auth_methods | Supports API Key | https://developer.copper.com/introduction/oauth/index.html
      “OAuth2.0¶ 1. Introduction¶ You can now access the Copper Developer API via OAuth2.0. This authentication method is an alternative to Copper's legacy API Keys, and is particularly well-suited for third-party integrations looking to create a seamless and secure ”
  - auth_methods | Supports Personal Access Token | https://developer.copper.com/introduction/authentication.html
      “ated the token. Users can hold multiple valid tokens at the same time. Admins can see all user generated tokens and generate new ones. To generate an API token, in the Copper web app go to System settings > API Keys and click the 'GENERATE API KEY' button. Cop”
  - api_type | REST API documented | https://developer.copper.com/
      “tions that interact with Copper in more complex ways than the integrations we provide out of the box. The Copper Developer API ("Dev API") provides a RESTful interface with JSON-formatted responses to access most Copper resources. We are continuously working o”
  - api_type | REST API documented | https://developer.copper.com/introduction/oauth/index.html
      “: more granular scopes will be added in the future 8. Client Libraries¶ Although it's entirely feasible to implement the OAuth 2.0 flow through plain REST, it's advisable to leverage a library tailored to your chosen application language or framework. Language”
  - credential_access | Access signal: partner_gated | https://copper.com
      “signAll integrations Resources BlogWebinarsGuides & eBooksCRM resource hubCase studiesHelp center Company About usCareersGet a demoDeveloperContact usBecome a partnerTrust Center Copper CRM, Inc. © 2026 Do Not Sell or Share My Personal InformationPrivacyTerms”
  - credential_access | Access signal: trial | https://copper.com
      “c is $29 ($23 billed annually), Professional is $69 ($59 billed annually) and Business is $134 ($99 billed annually). Every plan starts with a 14-day free trial, and no credit card is required. See Copper's pricing for a full feature comparison. Which tools do”
  - credential_access | Access signal: free | https://copper.com
      “lled annually), Professional is $69 ($59 billed annually) and Business is $134 ($99 billed annually). Every plan starts with a 14-day free trial, and no credit card is required. See Copper's pricing for a full feature comparison. Which tools does Copper integr”
  - mcp_available | MCP registry entry: dev.cotlet/copper-crm | https://registry.modelcontextprotocol.io/v0/servers?search=copper&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/copper-crm | https://registry.modelcontextprotocol.io/v0/servers?search=copper&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/copper-crm | https://registry.modelcontextprotocol.io/v0/servers?search=copper&limit=60
      “”

## [10] DealCloud — CRM and Sales
heuristic: auth=['OAuth2', 'API Key', 'Basic', 'Other'] api=['REST'] access=Unclear mcp=Official verdict=Buildable with limitations llms_txt=False
  page 200 direct 3250c https://api.docs.dealcloud.com/
  page 200 direct 3250c https://api.docs.dealcloud.com
  page 200 direct 7597c https://api.docs.dealcloud.com/docs/apikeys
  page 200 direct 8336c https://api.docs.dealcloud.com/docs/token
  page 200 direct 7389c https://api.docs.dealcloud.com/mcp/authentication
  page 200 direct 17430c https://api.docs.dealcloud.com/sdk/python-1.X/configuration/authentication
  page 200 direct 14819c https://api.docs.dealcloud.com/sdk/intapp-rest-client/configuration/authentication
  page 200 direct 9181c https://api.docs.dealcloud.com/sdk/python/authentication
  page 404 direct 0c https://api.docs.dealcloud.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://api.docs.dealcloud.com/docs/token
      “ght On This Page Scopes Examples HTTP Question? Give us feedback → (opens in a new tab)Edit this page API Reference Authorization Token Requesting an OAuth2 Bearer Token DealCloud uses the OAuth2 Client Credentials flow to generate a bearer token, which is the”
  - auth_methods | Supports OAuth2 | https://api.docs.dealcloud.com/mcp/authentication
      “Encryption Relationship Intelligence POST Emails POST Meetings GET Status GET Settings Schema Contracts MCP Getting Started AI Clients Authentication OAuth User Data Access Permissions Client Authentication Available Tools Custom MCP Servers SDKs Python SDK v1”
  - auth_methods | Supports API Key | https://api.docs.dealcloud.com/
      “FeedbackFeedback (opens in a new tab) Feedback (opens in a new tab) API Reference Getting Started API Keys Authorization Token Pagination Rate Limits Status Codes and Handling Core Schema EntryTypes All Entry Types Entry Type by ID Fields All Fields Fields”
  - auth_methods | Supports API Key | https://api.docs.dealcloud.com
      “FeedbackFeedback (opens in a new tab) Feedback (opens in a new tab) API Reference Getting Started API Keys Authorization Token Pagination Rate Limits Status Codes and Handling Core Schema EntryTypes All Entry Types Entry Type by ID Fields All Fields Fields”
  - auth_methods | Supports Basic | https://api.docs.dealcloud.com/sdk/intapp-rest-client/configuration/authentication
      “g Started Installation Quick Start Configuration Configuration Authentication Authentication Methods OAuth2 Client Credentials API Key Authentication Basic Authentication JWT Authentication Microsoft Entra ID (Azure AD) Okta Enterprise Authentication (httpx-au”
  - auth_methods | Supports Other | https://api.docs.dealcloud.com/sdk/intapp-rest-client/configuration/authentication
      “n Quick Start Configuration Configuration Authentication Authentication Methods OAuth2 Client Credentials API Key Authentication Basic Authentication JWT Authentication Microsoft Entra ID (Azure AD) Okta Enterprise Authentication (httpx-auth) Combining with Re”
  - api_type | REST API documented | https://api.docs.dealcloud.com/
      “uning Logging & Debugging Troubleshooting & FAQ Reference API Reference Data Models Constants Utilities & helpers Exceptions Changelog License Intapp REST Client Getting Started Getting Started Installation Quick Start Configuration Configuration Authenticatio”
  - api_type | REST API documented | https://api.docs.dealcloud.com
      “uning Logging & Debugging Troubleshooting & FAQ Reference API Reference Data Models Constants Utilities & helpers Exceptions Changelog License Intapp REST Client Getting Started Getting Started Installation Quick Start Configuration Configuration Authenticatio”
  - mcp_available | MCP mentioned in vendor docs | https://api.docs.dealcloud.com/
      “ackups Request Backup Retrieve Backups Delete Encryption Relationship Intelligence POST Emails POST Meetings GET Status GET Settings Schema Contracts MCP Getting Started AI Clients Authentication Available Tools Custom MCP Servers SDKs Python SDK v1.X Getting ”
  - mcp_available | MCP mentioned in vendor docs | https://api.docs.dealcloud.com
      “ackups Request Backup Retrieve Backups Delete Encryption Relationship Intelligence POST Emails POST Meetings GET Status GET Settings Schema Contracts MCP Getting Started AI Clients Authentication Available Tools Custom MCP Servers SDKs Python SDK v1.X Getting ”

## [11] Zendesk — Support and Helpdesk
heuristic: auth=['OAuth2', 'API Key', 'Basic', 'Personal Access Token', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Third-party/community verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 3188c https://developer.zendesk.com/api-reference/
  page 200 direct 6219c https://developer.zendesk.com/api-reference/introduction/security-and-auth/
  page 200 render 47450c https://zendesk.com
  page 200 direct 1146c https://developer.zendesk.com/api-reference/introduction/introduction/
  page 200 direct 2902c https://developer.zendesk.com/api-reference/betas/introduction/
  page 200 direct 18298c https://developer.zendesk.com/api-reference/changelog/changelog/
  page 200 direct 5954c https://developer.zendesk.com/api-reference/ticketing/introduction/
  page 200 direct 4831c https://developer.zendesk.com/api-reference/help_center/help-center-api/introduction/
  page 200 direct 1284c https://developer.zendesk.com/api-reference/ai-agents/introduction/
  page 200 direct 138296c https://developer.zendesk.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developer.zendesk.com/api-reference/introduction/security-and-auth/
      “vailability Security and authentication Rate limits Requests Data types Pagination Working with AI tools Change policy Undocumented APIs On this page OAuth access token Global OAuth access token API token (deprecated) SSL requirements End user authentication S”
  - auth_methods | Supports OAuth2 | https://developer.zendesk.com/api-reference/changelog/changelog/
      “letely removed. See Upgrading from Templating API v1, Upgrading from Templating API v2, and Upgrading from Templating API v3. Aug 26, 2026 Deprecated OAuth Tokens The Create Token (/api/v2/oauth/tokens) endpoint is deprecated. Use Create Token for Grant Type i”
  - auth_methods | Supports API Key | https://developer.zendesk.com/api-reference/changelog/changelog/
      “and Custom Objects API. Mar 30, 2023 Added Webhooks API Added a new custom_headers property to webhooks and the authentication property now supports api_key as a type. See Creating and monitoring webhooks. Mar 2, 2023 Deprecated Status API Four Status API endp”
  - auth_methods | Supports Basic | https://developer.zendesk.com/api-reference/introduction/security-and-auth/
      “quests. Zendesk supports using OAuth access tokens to authenticate API requests. Note: If you're an existing Zendesk customer and are currently using basic authentication or API tokens, you will have to migrate to OAuth access tokens for improved security and ”
  - auth_methods | Supports Basic | https://developer.zendesk.com/api-reference/changelog/changelog/
      “ting API Introduced Help Center Templating API v4 and an update to the Copenhagen theme. See Upgrading from Templating API v3. Jul 1, 2024 Deprecated Basic authentication Starting July 31, 2024, basic authentication using an email and password is deprecated fo”
  - auth_methods | Supports Personal Access Token | https://developer.zendesk.com/api-reference/introduction/security-and-auth/
      “limits Requests Data types Pagination Working with AI tools Change policy Undocumented APIs On this page OAuth access token Global OAuth access token API token (deprecated) SSL requirements End user authentication Security and authentication On this page OAuth”
  - auth_methods | Supports Personal Access Token | https://developer.zendesk.com/api-reference/changelog/changelog/
      “y on V2 should remain on V2 and will be supported by Zendesk for now. Zendesk will reach out to V2 customers with next steps. June 1, 2026 Deprecated API tokens Starting July 28, 2026, Zendesk will begin a phased end-of-life process for API tokens. On July 28,”
  - auth_methods | Supports Other | https://developer.zendesk.com/api-reference/changelog/changelog/
      “d Help Center APIs available as OAS file downloads. You can download them from the Ticketing and Help Center home pages. Oct 12, 2023 Breaking change JWT Changed the https://yoursubdomain.zendesk.com/access/jwt endpoint method from GET to POST. See How JWT SSO”
  - api_type | REST API documented | https://zendesk.com
      “nter with voice and intelligent channel routing and reporting and performance insights that scale across every channel. **Integrate service with the rest of your systems** Integrate Zendesk with your existing systems through prebuilt integrations and APIs to r”
  - api_type | REST API documented | https://developer.zendesk.com/api-reference/changelog/changelog/
      “switch to the authorization code grant flow. See also Using PKCE to make Zendesk OAuth access tokens more secure. Aug 19, 2024 Deprecated Zopim Chat REST API Beginning May 12, 2025, Live Chat API endpoints that use the www.zopim.com/api/v2 path will stop worki”
  - credential_access | Access signal: partner_gated | https://zendesk.com
      “cks with a unified system that embeds AI across voice and digital. Deliver an enterprise-grade contact center without the middleware or complexity. [Contact sales](https://www.zendesk.com/contact/)[Learn more](https://www.zendesk.com/service/contact-center/) R”
  - credential_access | Access signal: trial | https://zendesk.com
      “to improve customer and employee experiences with the Zendesk Outcome AI™ Platform. Trusted by 32,000+ customers to drive better outcomes. **14-day free trial.** No credit card required. Use your work email to connect customer emails, apps, and invite team mem”
  - credential_access | Access signal: free | https://zendesk.com
      “stomer and employee experiences with the Zendesk Outcome AI™ Platform. Trusted by 32,000+ customers to drive better outcomes. **14-day free trial.** No credit card required. Use your work email to connect customer emails, apps, and invite team members. Try for”
  - credential_access | Access signal: free | https://developer.zendesk.com/api-reference/ticketing/introduction/
      “hen try out different requests to learn how the API works. Click the following button to get started: If you don't use Postman, you can sign up for a free account on the Postman website and download the app. For more information about using Postman with Zendes”
  - mcp_available | MCP registry entry: com.swifteq/zendesk-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=zendesk&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/zendesk | https://registry.modelcontextprotocol.io/v0/servers?search=zendesk&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/zendesk | https://registry.modelcontextprotocol.io/v0/servers?search=zendesk&limit=60
      “”

## [12] Intercom — Support and Helpdesk
heuristic: auth=['OAuth2', 'API Key'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 5399c https://developers.intercom.com/docs
  page 200 direct 4064c https://developers.intercom.com/docs/build-an-integration/learn-more/authentication
  page 200 direct 10494c https://intercom.com
  page 200 direct 17300c https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/setting-up-oauth
  page 200 direct 7481c https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/installing-uninstalling-apps
  page 200 direct 3028c https://developers.intercom.com/docs/references/introduction
  page 200 direct 6701c https://developers.intercom.com/docs/build-an-integration/getting-started
  page 200 direct 12173c https://developers.intercom.com/docs/build-an-integration/getting-started/build-an-app-for-your-messenger
  page 200 direct 14928c https://developers.intercom.com/docs/build-an-integration/getting-started/build-an-app-for-your-messenger/sheets-app
  page 200 direct 264556c https://developers.intercom.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.intercom.com/docs
      “Domains Model Context Protocol (MCP) References Object Model REST API Reference Canvas Kit Reference Webhook Topics Public Apps & App Store Configure OAuth Build and Publish Apps App Store Guidelines Home/ Overview Overview Copy The Intercom Developer Platform”
  - auth_methods | Supports OAuth2 | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication
      “Domains Model Context Protocol (MCP) References Object Model REST API Reference Canvas Kit Reference Webhook Topics Public Apps & App Store Configure OAuth Build and Publish Apps App Store Guidelines Home/ Authentication Authentication Copy To access the Inter”
  - auth_methods | Supports API Key | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication
      “are requesting access to other people's Intercom accounts/data (for example, through an integration you've built) You currently ask people for their API Keys to request resources on their behalf You want to make it easier for your customers to share their cust”
  - api_type | REST API documented | https://developers.intercom.com/docs
      “Contacts Tickets Help Center Reporting Using the APIs Webhooks Fin Agent API News Center Domains Model Context Protocol (MCP) References Object Model REST API Reference Canvas Kit Reference Webhook Topics Public Apps & App Store Configure OAuth Build and Publi”
  - api_type | REST API documented | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication
      “Contacts Tickets Help Center Reporting Using the APIs Webhooks Fin Agent API News Center Domains Model Context Protocol (MCP) References Object Model REST API Reference Canvas Kit Reference Webhook Topics Public Apps & App Store Configure OAuth Build and Publi”
  - credential_access | Access signal: free | https://developers.intercom.com/docs
      “com team for review. Set up a development workspace To develop a public app you will need to use a development workspace: sign up here to create your free account. This will give you access to your Developer Hub, where you can configure webhooks, define your e”
  - credential_access | Access signal: free | https://intercom.com
      “ustomer conversation improves the next one, enabling perfect experiences that were never possible before. Start free trialView demo14 day free trial. No credit card required. Two products, one seamless experience Intercom helpdesk Fin AI Agent Trusted by 30,00”
  - credential_access | Access signal: partner_gated | https://intercom.com
      “tomer experience.Learn more Introducing Fin 4.Learn more Introducing Fin 4. A major step toward a fully agentic customer experience.Learn more Log in Contact sales View demo Start free trial Fin AI Agent→ Product Explore all products Intercom helpdesk Fin AI A”
  - credential_access | Access signal: trial | https://intercom.com
      “troducing Fin 4.Learn more Introducing Fin 4. A major step toward a fully agentic customer experience.Learn more Log in Contact sales View demo Start free trial Fin AI Agent→ Product Explore all products Intercom helpdesk Fin AI Agent↗ Platform Channels Integr”
  - credential_access | Access signal: trial | https://developers.intercom.com/docs/build-an-integration/getting-started/build-an-app-for-your-messenger
      “the Messenger in the bottom right. Next steps Deploy with Replit If you're ready to deploy your app you can do so right from Replit. However, Replit test accounts are free, but deployments are a premium feature. You can see the costs on the Replit pricing page”
  - credential_access | Access signal: admin_approval | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/installing-uninstalling-apps
      “nfigure OAuth Build and Publish Apps Building Successful Apps Listing your App Writing your Start Guide Installing your App Installation Health Check App Review and Publishing Promoting your App App Store Guidelines Home/ Build and Publish Apps Installing your”
  - mcp_available | MCP mentioned in vendor docs | https://developers.intercom.com/docs
      “Build an Inbox App Developer Guides Messenger Inbox Contacts Tickets Help Center Reporting Using the APIs Webhooks Fin Agent API News Center Domains Model Context Protocol (MCP) References Object Model REST API Reference Canvas Kit Reference Webhook Topics Pub”
  - mcp_available | MCP mentioned in vendor docs | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication
      “Build an Inbox App Developer Guides Messenger Inbox Contacts Tickets Help Center Reporting Using the APIs Webhooks Fin Agent API News Center Domains Model Context Protocol (MCP) References Object Model REST API Reference Canvas Kit Reference Webhook Topics Pub”
  - mcp_available | MCP registry entry: io.github.MuhammadTalhaMT/intercom | https://registry.modelcontextprotocol.io/v0/servers?search=intercom&limit=60
      “https://github.com/MuhammadTalhaMT/claude-intercom”
  - mcp_available | MCP registry entry: io.github.MuhammadTalhaMT/intercom | https://registry.modelcontextprotocol.io/v0/servers?search=intercom&limit=60
      “https://github.com/MuhammadTalhaMT/claude-intercom”
  - mcp_available | MCP registry entry: io.github.iambashar/agent-intercom | https://registry.modelcontextprotocol.io/v0/servers?search=intercom&limit=60
      “https://github.com/iambashar/agent-intercom”

## [13] Freshdesk — Support and Helpdesk
heuristic: auth=['OAuth2', 'API Key', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 621503c https://developers.freshdesk.com/api/
  page 200 direct 4388c https://freshdesk.com
  page 200 direct 2975c https://developers.freshdesk.com/v2/docs/quick-start/
  page 200 direct 13531c https://support.freshdesk.com/en/support/solutions/articles/50000004224-overview-of-custom-objects-in-freshdesk
  page 404 direct 0c https://developers.freshdesk.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://developers.freshdesk.com/api/
      “und Email 10 Status Value Open 2 Pending 3 Resolved 4 Closed 5 Priority Value Low 1 Medium 2 High 3 Urgent 4 Create a Ticket post /api/v2/tickets OAuth 2.0 Scope 1 freshdesk.tickets.create Parameters Attribute Type Description name string Name of the requester”
  - auth_methods | Supports API Key | https://developers.freshdesk.com/api/
      “View a Service Account /api/v2/agents/[id] Update a Service Account /api/v2/agents/[id] Delete a Service Account /api/v2/agents/[id] List API Keys /api/v2/agents/[id]/api_keys Create an API Key /api/v2/agents/[id]/api_keys View an API Key /api/v2/agents/[id]/a”
  - auth_methods | Supports Other | https://developers.freshdesk.com/api/
      “ly Authenticated Agent /api/v2/agents/me Create Multiple Agents /api/v2/agents/bulk Search Agents /api/v2/agents/autocomplete?term=[keyword] Service Accounts Service Accounts Create a Service Account /api/v2/agents View a Service Account /api/v2/agents/[id] Up”
  - api_type | REST API documented | https://developers.freshdesk.com/api/
      “talk to their customers and make it easy for users to get in touch with businesses. Freshdesk's APIs belong to the Representational State Transfer (REST) category. They allow you to perform 'RESTful' operations such as reading, modifying, adding or deleting da”
  - credential_access | Access signal: enterprise | https://developers.freshdesk.com/api/
      “d messages cover both send and retrieve endpoints. These limits are set at 1,000 calls per minute for the Pro plan and 2,000 calls per minute for the Enterprise plan. To comply with WhatsApp's policies, these outbound messages must use structured templates, wh”
  - credential_access | Access signal: admin_approval | https://developers.freshdesk.com/api/
      “dicates that the agent whose credentials were used in making this request was not authorized to perform this API call. It could be that this API call requires admin level credentials or perhaps the Freshdesk portal doesn't have the corresponding feature enable”
  - credential_access | Access signal: paid_plan | https://developers.freshdesk.com/api/
      “tion. Note: Template message delivery on WhatsApp Business Platform via public API is only available to customers on Pro and Enterprise tiers of our paid plans. Attribute Type Description message_id string Unique identifier generated when an outbound message r”
  - credential_access | Access signal: trial | https://developers.freshdesk.com/api/
      “T 'https://domain.freshdesk.com/api/v2/discussions/categories' EXPAND ↓ Response 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 [ { "id" : 1, "name" : "Test Account Forums", "description" : "Default forum category, feel free to edit or delete it.", "created_at" : "201”
  - credential_access | Access signal: trial | https://support.freshdesk.com/en/support/solutions/articles/50000004224-overview-of-custom-objects-in-freshdesk
      “Custom Object records in Freshdesk Custom Objects - Portals Freshdesk Omni The agentic AI solution for modern, omnichannel customer service. Start free trial Learn more Our Products Freshdesk Freshservice Freshsales Freshdesk Contact Center Freshteam Freshchat”
  - credential_access | Access signal: partner_gated | https://freshdesk.com
      “Skip to main content The Customer Service Benchmark Report 2026 is now live. Download the report here EnglishContact SalesLoginSkip to main content Products AI Platform Resources Pricing Start for free Get a demo Products AI Platform Resources Demo Pricing Lan”
  - credential_access | Access signal: partner_gated | https://developers.freshdesk.com/v2/docs/quick-start/
      “rcesResources Getting Started Tutorials & Guides Sample Apps Developer Blog Events Community & SupportCommunity & Support Developer Community Support Partner Program Feature Requests CompanyCompany About Us Customers Partners All Systems Operational (opens Fre”
  - mcp_available | MCP mentioned in vendor docs | https://freshdesk.com
      “service on your timeline. Connect the tools your team relies on Connect Freshdesk with the AI tools and apps your support team already uses. Through MCP, bring customer data into everyday workflows and automate support at scale. Explore Freshdesk MCP Connect y”
  - mcp_available | MCP registry entry: io.github.WYRE-AI/freshdesk-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=freshdesk&limit=60
      “https://github.com/WYRE-AI/freshdesk-mcp”
  - mcp_available | MCP registry entry: io.github.WYRE-AI/freshdesk-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=freshdesk&limit=60
      “https://github.com/WYRE-AI/freshdesk-mcp”
  - mcp_available | MCP registry entry: io.github.WYRE-AI/freshdesk-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=freshdesk&limit=60
      “https://github.com/WYRE-AI/freshdesk-mcp”

## [14] Front — Support and Helpdesk
heuristic: auth=['OAuth2', 'Basic', 'Personal Access Token'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 10443c https://dev.frontapp.com/docs/welcome
  page 200 direct 6223c https://dev.frontapp.com/docs/authentication
  page 200 direct 9493c https://front.com
  page 200 direct 9891c https://dev.frontapp.com/docs/oauth
  page 200 direct 7268c https://dev.frontapp.com/docs/create-and-revoke-api-tokens
  page 200 direct 2532c https://dev.frontapp.com/docs/auth0-react-vite-template-plugin
  page 200 direct 5586c https://dev.frontapp.com/docs/token-instrospection-for-channel-identification
  page 200 direct 11323c https://dev.frontapp.com/reference
  page 200 direct 3325c https://dev.frontapp.com/docs/core-api-overview
  page 200 direct 64710c https://dev.frontapp.com/llms.txt
  - auth_methods | Supports OAuth2 | https://dev.frontapp.com/docs/welcome
      “artnering With Front Create, manage, and publish apps Join our Developer Community Core API Overview Getting Started with the Core API Authentication OAuth API tokens Fundamentals API Terminology 101 Base URL Rate limits Pagination Search Query object 'q' Reso”
  - auth_methods | Supports OAuth2 | https://dev.frontapp.com/docs/authentication
      “artnering With Front Create, manage, and publish apps Join our Developer Community Core API Overview Getting Started with the Core API Authentication OAuth API tokens Fundamentals API Terminology 101 Base URL Rate limits Pagination Search Query object 'q' Reso”
  - auth_methods | Supports Basic | https://dev.frontapp.com/docs/oauth
      “POST HTTP request to https://app.frontapp.com/oauth/token with the body parameters noted in the table below. Your request MUST be authenticated with Basic authentication using your OAuth application Client ID and Client Secret base64 encoded, as shown below: 📘”
  - auth_methods | Supports Basic | https://dev.frontapp.com/docs/token-instrospection-for-channel-identification
      “the client makes a POST request to the configured token introspection URL. The request should include the following components: Authentication—Using Basic Auth, providing the client_id and client_secret as credentials. Request Body—Include the access_token to ”
  - auth_methods | Supports Personal Access Token | https://dev.frontapp.com/docs/welcome
      “ing With Front Create, manage, and publish apps Join our Developer Community Core API Overview Getting Started with the Core API Authentication OAuth API tokens Fundamentals API Terminology 101 Base URL Rate limits Pagination Search Query object 'q' Resource A”
  - auth_methods | Supports Personal Access Token | https://dev.frontapp.com/docs/authentication
      “ing With Front Create, manage, and publish apps Join our Developer Community Core API Overview Getting Started with the Core API Authentication OAuth API tokens Fundamentals API Terminology 101 Base URL Rate limits Pagination Search Query object 'q' Resource A”
  - api_type | REST API documented | https://dev.frontapp.com/docs/oauth
      “d when making OAuth requests to the https://app.frontapp.com/ OAuth service. Otherwise, authentication will be Bearer authentication as stated in the rest of these docs. 📘 💡 Basic Authentication The Basic Authentication string is your client ID and secret join”
  - credential_access | Access signal: trial | https://dev.frontapp.com/docs/welcome
      “es, Postman collections and more. We’re also available at Front Community to help with any questions or feedback! How to get started Step 1: Create a developer account If you are building an app you intend to publish on our App Store, you must build this app i”
  - credential_access | Access signal: partner_gated | https://front.com
      “ntercom Front vs. Help Scout Front vs. Salesforce Front vs. Hiver Front vs. Missive Front vs. Pylon Company About Careers Press Kit Real-Time Metrics Become a Partner Customer Referral Contact Support Legal More Features Front Overview Help Desk Shared Inbox T”
  - mcp_available | MCP mentioned in vendor docs | https://dev.frontapp.com/docs/welcome
      “Attachments Webhooks Application webhooks Rule webhooks Deprecation Policy Application Triggers Core API Reference Tools Sample Applications Front AI MCP Server Admin MCP Server AI agents Plugins Overview Getting Started with the Plugin SDK Fundamentals Plugin”
  - mcp_available | MCP mentioned in vendor docs | https://dev.frontapp.com/docs/authentication
      “Attachments Webhooks Application webhooks Rule webhooks Deprecation Policy Application Triggers Core API Reference Tools Sample Applications Front AI MCP Server Admin MCP Server AI agents Plugins Overview Getting Started with the Plugin SDK Fundamentals Plugin”
  - mcp_available | MCP registry entry: ai.clize/storefront | https://registry.modelcontextprotocol.io/v0/servers?search=front&limit=60
      “https://github.com/cooldk/clize-cli”
  - mcp_available | MCP registry entry: ai.clize/storefront | https://registry.modelcontextprotocol.io/v0/servers?search=front&limit=60
      “https://github.com/cooldk/clize-cli”
  - mcp_available | MCP registry entry: ai.clize/storefront | https://registry.modelcontextprotocol.io/v0/servers?search=front&limit=60
      “https://github.com/cooldk/clize-cli”

## [15] Pylon — Support and Helpdesk
heuristic: auth=['Personal Access Token', 'Other'] api=[] access=Unclear mcp=Official verdict=Insufficient evidence llms_txt=True
  page 200 direct 2907c https://docs.usepylon.com/pylon-docs/developer/api
  page 200 direct 6654c https://docs.usepylon.com/pylon-docs/developer/api/authentication
  page 200 direct 6756c https://usepylon.com
  page 200 direct 2448c https://docs.usepylon.com/pylon-docs/knowledge-base/custom-authentication
  page 200 direct 2737c https://docs.usepylon.com/pylon-docs/customer-portal/custom-authentication
  page 200 render 169c https://docs.usepylon.com/pylon-docs/~gitbook/mcp
  page 200 direct 2705c https://docs.usepylon.com/pylon-docs
  page 200 direct 1914c https://docs.usepylon.com/pylon-docs/getting-started/publish-your-docs
  page 200 direct 2324c https://docs.usepylon.com/pylon-docs/getting-started/setup
  page 200 direct 35315c https://docs.usepylon.com/llms.txt
  - auth_methods | Supports Personal Access Token | https://docs.usepylon.com/pylon-docs/developer/api
      “to read and write data in Pylon Pylon’s API can be used to programmatically access and take action on data within Pylon. Only Admin users can create API tokens. To learn more about Admins, see Roles & User Management. Some common use cases for our API include:”
  - auth_methods | Supports Personal Access Token | https://docs.usepylon.com/pylon-docs/developer/api/authentication
      “page Developer API Authentication How to authenticate with Pylon's API The Pylon API uses Bearer authentication. This means you’ll need to pass your API token in the header of your request: Copy Authorization: Bearer <token> Generate an API token in the Pylon ”
  - auth_methods | Supports Other | https://docs.usepylon.com/pylon-docs/customer-portal/custom-authentication
      “your Pylon customer portal (and knowledge base). For more details on how to implement this, view the setup guide in our help center. When sending the JWT to the callback by POST, use Content-Type: application/x-www-form-urlencoded and a form field named jwt. T”
  - mcp_available | MCP mentioned in vendor docs | https://docs.usepylon.com/pylon-docs/developer/api
      “Markdown versions of documentation pages are available by appending .md to page URLs. Agents can also search and read this documentation through its MCP server.Skip to content ⌘Ctrlk Knowledge BaseWebsiteChangelogBook a DemoLogin More Getting Started Introduct”
  - mcp_available | MCP mentioned in vendor docs | https://docs.usepylon.com/pylon-docs/developer/api/authentication
      “Markdown versions of documentation pages are available by appending .md to page URLs. Agents can also search and read this documentation through its MCP server.Skip to content ⌘Ctrlk Knowledge BaseWebsiteChangelogBook a DemoLogin More Getting Started Introduct”
  - mcp_available | MCP registry entry: io.github.JustinBeckwith/pylon-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pylon&limit=60
      “https://github.com/JustinBeckwith/pylon-mcp”
  - mcp_available | MCP registry entry: io.github.JustinBeckwith/pylon-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pylon&limit=60
      “https://github.com/JustinBeckwith/pylon-mcp”
  - mcp_available | MCP registry entry: io.github.JustinBeckwith/pylon-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pylon&limit=60
      “https://github.com/JustinBeckwith/pylon-mcp”

## [16] LiveAgent — Support and Helpdesk
heuristic: auth=['API Key'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 404 direct 0c https://www.liveagent.com/api/ ERR HTTP 404
  page 200 direct 18518c https://liveagent.com
  page 200 direct 30140c https://www.liveagent.com/pricing/
  page 200 direct 124556c https://support.liveagent.com/840770-Complete-API-reference
  page 200 direct 14971c https://www.liveagent.com/llms.txt
  - auth_methods | Supports API Key | https://www.liveagent.com/pricing/
      “run actions automatically after a set time passes. Custom roles —Not included 2 5 Unlimited Create custom roles with specific permissions for agents. API keys 1 5 10 Unlimited Let third-party apps retrieve and push data and manage tickets from outside LiveAgen”
  - auth_methods | Supports API Key | https://support.liveagent.com/840770-Complete-API-reference
      “ould also use .yaml to get response in YAML format. Error messages formats 400 - Bad request error You can get this in case your athentification with API key failed because of problem with API key in application. 401 - Forbidden You can get this in case of fai”
  - api_type | REST API documented | https://support.liveagent.com/840770-Complete-API-reference
      “My tickets Submit ticket Login Complete API reference Home > Technical Support > LiveAgent API > REST API > API v1 > Documentation > Complete API reference Data fields formats Return messages formats Error messages formats Api v.1 Agents”
  - credential_access | Access signal: paid_plan | https://liveagent.com
      “Everything LiveAgent does, in one list Data in the EU (Frankfurt), the US or Singapore, you choose Free help moving your tickets and history with any paid plan 30-day free trial, no credit card AI AI in LiveAgent AI that answers customers and drafts replies, i”
  - credential_access | Access signal: paid_plan | https://www.liveagent.com/pricing/
      “Everything LiveAgent does, in one list Data in the EU (Frankfurt), the US or Singapore, you choose Free help moving your tickets and history with any paid plan 30-day free trial, no credit card AI AI in LiveAgent AI that answers customers and drafts replies, i”
  - credential_access | Access signal: trial | https://liveagent.com
      “ent does, in one list Data in the EU (Frankfurt), the US or Singapore, you choose Free help moving your tickets and history with any paid plan 30-day free trial, no credit card AI AI in LiveAgent AI that answers customers and drafts replies, inside the same in”
  - credential_access | Access signal: trial | https://www.liveagent.com/pricing/
      “ent does, in one list Data in the EU (Frankfurt), the US or Singapore, you choose Free help moving your tickets and history with any paid plan 30-day free trial, no credit card AI AI in LiveAgent AI that answers customers and drafts replies, inside the same in”
  - credential_access | Access signal: free | https://liveagent.com
      “one list Data in the EU (Frankfurt), the US or Singapore, you choose Free help moving your tickets and history with any paid plan 30-day free trial, no credit card AI AI in LiveAgent AI that answers customers and drafts replies, inside the same inbox your team”
  - credential_access | Access signal: free | https://www.liveagent.com/pricing/
      “one list Data in the EU (Frankfurt), the US or Singapore, you choose Free help moving your tickets and history with any paid plan 30-day free trial, no credit card AI AI in LiveAgent AI that answers customers and drafts replies, inside the same inbox your team”
  - credential_access | Access signal: partner_gated | https://www.liveagent.com/pricing/
      “price: $3,199. /mo Extra agents $23.40 each Flat fee · billed annually Code BLACKFRIDAY40Y at checkout Code BLACKFRIDAY33M at checkoutRequest a quoteTalk to sales AI agents Unlimited Departments Unlimited Email accounts Unlimited Live chat buttons UnlimitedWha”
  - mcp_available | MCP mentioned in vendor docs | https://www.liveagent.com/pricing/
      “department, channel, SLA compliance, time and tag reports, CSAT surveys SLA rules and custom roles Business Per agent · any team size More AI agents, MCP and control Black Friday 40% off Offer price $29.40$29.40 $39.53$39.53 Regular price: $49. /agent/mo 5 age”

## [17] Plain — Support and Helpdesk
heuristic: auth=['OAuth2', 'API Key', 'Other'] api=['GraphQL'] access=Self-serve (free trial / sandbox) mcp=Official verdict=Ready to build llms_txt=True
  page 200 direct 45351c https://www.plain.com/docs/api-reference/graphql
  page 200 direct 40194c https://www.plain.com/docs/api-reference/graphql/authentication
  page 200 direct 8080c https://plain.com
  page 200 direct 40194c https://www.plain.com/docs/graphql/authentication
  page 200 direct 70977c https://www.plain.com/docs/graphql/oauth
  page 200 direct 86837c https://www.plain.com/docs/product/channels/chat-authentication
  page 200 direct 40194c https://www.plain.com/docs/graphql/authentication/
  page 200 direct 45351c https://www.plain.com/docs/graphql/introduction
  page 200 direct 592045c https://www.plain.com/docs/graphql-reference/queries/account
  page 200 direct 9158c https://www.plain.com/llms.txt
  - auth_methods | Supports OAuth2 | https://www.plain.com/docs/api-reference/graphql
      “elp Center Changelog Blog Search... Navigation GraphQL API Introduction Documentation Developer API Reference GraphQL API Introduction Authentication OAuth Schema Pagination Error handling Error codes Customers Accounts Threads Tiers SLA policies Business hour”
  - auth_methods | Supports OAuth2 | https://www.plain.com/docs/api-reference/graphql/authentication
      “p Center Changelog Blog Search... Navigation GraphQL API Authentication Documentation Developer API Reference GraphQL API Introduction Authentication OAuth Schema Pagination Error handling Error codes Customers Accounts Threads Tiers SLA policies Business hour”
  - auth_methods | Supports API Key | https://www.plain.com/docs/api-reference/graphql
      “k.plain.com/graphql/v1 Allowed method: POST Required headers: Content-Type: application/json Authorization: Bearer YOUR_TOKEN where the token is your API key. See authentication for more details. JSON body: query: the GraphQL query string variables: a JSON obj”
  - auth_methods | Supports API Key | https://www.plain.com/docs/api-reference/graphql/authentication
      “Spacer Text UI components SDK Security Request signing mTLS IP Addresses Changelog Changelog GraphQL API Authentication Create a machine user and an API key, and scope it with fine-grained permissions. A machine user can have several API keys, so you can rotat”
  - auth_methods | Supports Other | https://www.plain.com/docs/api-reference/graphql
      “und Examples UI Components Overview Badge Container CopyButton Divider LinkButton WorkflowButton PlainText Row Spacer Text UI components SDK Security Request signing mTLS IP Addresses Changelog Changelog On this pageBack to top Key details Your first API call ”
  - auth_methods | Supports Other | https://www.plain.com/docs/api-reference/graphql/authentication
      “und Examples UI Components Overview Badge Container CopyButton Divider LinkButton WorkflowButton PlainText Row Spacer Text UI components SDK Security Request signing mTLS IP Addresses Changelog Changelog GraphQL API Authentication Create a machine user and an ”
  - api_type | GraphQL API documented | https://www.plain.com/docs/api-reference/graphql
      “nses are generated using AI and may contain mistakes. Plain Docs home page Search...⌘KAsk Assistant⌘I Help Center Changelog Blog Search... Navigation GraphQL API Introduction Documentation Developer API Reference GraphQL API Introduction Authentication OAuth S”
  - api_type | GraphQL API documented | https://www.plain.com/docs/api-reference/graphql/authentication
      “nses are generated using AI and may contain mistakes. Plain Docs home page Search...⌘KAsk Assistant⌘I Help Center Changelog Blog Search... Navigation GraphQL API Authentication Documentation Developer API Reference GraphQL API Introduction Authentication OAuth”
  - credential_access | Access signal: trial | https://plain.com
      “to. Keep your knowledge up-to-date When it finds a knowledge gap, it hands the thread to your team and suggests updates. Test it on real threads Use Test Mode to see its draft replies on live traffic before you turn it on. Joseph Myers Why is our invoice $480 ”
  - credential_access | Access signal: trial | https://www.plain.com/docs/product/channels/chat-authentication
      “{"title":"Custom instructions","href":"/product/agents/ari/custom-instructions"},{"title":"Handoffs","href":"/product/agents/ari/handoffs"},{"title":"Test mode","href":"/product/agents/ari/test-mode"},{"title":"Citations","href":"/product/agents/ari/citations"”
  - mcp_available | MCP mentioned in vendor docs | https://www.plain.com/docs/api-reference/graphql
      “d Interacting in Discussions Working on Threads Tool Calls Suggesting Replies Working with Notes Using Knowledge Examples Agent integrations Overview MCP server Agent skill Cursor Webhooks Overview Webhook Versions Webhook events Webhooks SDK Channels Authenti”
  - mcp_available | MCP mentioned in vendor docs | https://www.plain.com/docs/api-reference/graphql/authentication
      “d Interacting in Discussions Working on Threads Tool Calls Suggesting Replies Working with Notes Using Knowledge Examples Agent integrations Overview MCP server Agent skill Cursor Webhooks Overview Webhook Versions Webhook events Webhooks SDK Channels Authenti”
  - mcp_available | MCP registry entry: ai.livecore/voiceover-tts-dubbing-translate-lip-sync-audio-music-sfx-silence-ffmpeg-remotion-capcut-descript-opus-premiere-after-effects-ugc-faceless-explainer-promo-montage-thumbnail-watermark-blur | https://registry.modelcontextprotocol.io/v0/servers?search=plain&limit=60
      “https://github.com/brajendrak00068/agentic-ai-video-production”
  - mcp_available | MCP registry entry: ai.plainvoice/mcp | https://registry.modelcontextprotocol.io/v0/servers?search=plain&limit=60
      “”
  - mcp_available | MCP registry entry: ai.smithery/plainyogurt21-clintrials-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=plain&limit=60
      “”

## [18] Help Scout — Support and Helpdesk
heuristic: auth=['OAuth2'] api=['REST'] access=Unclear mcp=Third-party/community verdict=Buildable with limitations llms_txt=True
  page 200 direct 5014c https://developer.helpscout.com/mailbox-api/
  page 200 direct 8641c https://developer.helpscout.com/mailbox-api/overview/authentication/
  page 200 direct 6550c https://helpscout.com
  page 200 direct 8641c https://developer.helpscout.com/mailbox-api/overview/authentication
  page 200 direct 4658c https://developer.helpscout.com/mailbox-api/overview/backward-compatibility/
  page 200 direct 4495c https://developer.helpscout.com/mailbox-api/overview/content_type/
  page 200 direct 13738c https://developer.helpscout.com/mailbox-api/overview/errors/
  page 200 direct 4493c https://developer.helpscout.com/mailbox-api/overview/http-methods/
  page 200 direct 4926c https://developer.helpscout.com/mailbox-api/overview/links/
  page 200 direct 40456c https://developer.helpscout.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developer.helpscout.com/mailbox-api/
      “anual Workflows Update workflow status Changelog Inbox API 2.0 Welcome to the second generation of our Inbox API. This is an HTTPS-only API, with OAuth 2 authentication and CORS support running at: https://api.helpscout.net/v2 It uses JSON for requests, respon”
  - auth_methods | Supports OAuth2 | https://developer.helpscout.com/mailbox-api/overview/authentication/
      “te Webhook Workflows List Workflows Run Manual Workflows Update workflow status Changelog Authentication This is an HTTPS-only API and it uses OAuth 2.0 authorization, implementing Authorization Code and Client Credential flows. All requests have to be authent”
  - api_type | REST API documented | https://developer.helpscout.com/mailbox-api/overview/errors/
      “are sent. User may not create users The caller does not have permission to create users. Only Administrators and Account Owners can create users via POST /v2/users. Returned with HTTP 403. User email not unique A user with the supplied email address already ex”
  - mcp_available | MCP registry entry: dev.cotlet/help-scout | https://registry.modelcontextprotocol.io/v0/servers?search=help&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/help-scout | https://registry.modelcontextprotocol.io/v0/servers?search=help&limit=60
      “”

## [19] Gorgias — Support and Helpdesk
heuristic: auth=['OAuth2', 'API Key'] api=['REST'] access=Partnership / contact-sales gated mcp=Third-party/community verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 4854c https://developers.gorgias.com/reference/introduction
  page 200 direct 4174c https://developers.gorgias.com/docs/authentication
  page 200 direct 7762c https://gorgias.com
  page 200 direct 4174c https://developers.gorgias.com/reference/authentication
  page 200 direct 1888c https://developers.gorgias.com/docs
  page 200 direct 4854c https://developers.gorgias.com/reference
  page 200 direct 4994c https://developers.gorgias.com/reference/limitations
  page 200 direct 1888c https://developers.gorgias.com/docs/private-vs-public-app
  page 200 direct 8625c https://developers.gorgias.com/docs/set-up-oauth2-app-store
  page 200 direct 20429c https://developers.gorgias.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.gorgias.com/docs/authentication
      “The Statistic object Powered by Copy Page Authentication The Gorgias API supports two authentication methods: 🔐 Private app → API key 👥 Public app → OAuth2 Using OAuth2 is mandatory for public apps. For testing purposes, you can perform requests directly from ”
  - auth_methods | Supports OAuth2 | https://developers.gorgias.com/reference/authentication
      “The Statistic object Powered by Copy Page Authentication The Gorgias API supports two authentication methods: 🔐 Private app → API key 👥 Public app → OAuth2 Using OAuth2 is mandatory for public apps. For testing purposes, you can perform requests directly from ”
  - auth_methods | Supports API Key | https://developers.gorgias.com/docs/authentication
      “HttpIntegration object The Statistic object Powered by Copy Page Authentication The Gorgias API supports two authentication methods: 🔐 Private app → API key 👥 Public app → OAuth2 Using OAuth2 is mandatory for public apps. For testing purposes, you can perform ”
  - auth_methods | Supports API Key | https://developers.gorgias.com/reference/authentication
      “HttpIntegration object The Statistic object Powered by Copy Page Authentication The Gorgias API supports two authentication methods: 🔐 Private app → API key 👥 Public app → OAuth2 Using OAuth2 is mandatory for public apps. For testing purposes, you can perform ”
  - api_type | REST API documented | https://developers.gorgias.com/reference/introduction
      “PI Reference HomeQuickstartAPI ReferenceChangelog Introduction Gorgias API Introduction Authentication Requests Errors Pagination Rate Limits Gorgias REST API Account The Account object Retrieve your accountget List settingsget Create a settingpost Update a se”
  - api_type | REST API documented | https://developers.gorgias.com/docs/authentication
      “Reference HomeQuickstartAPI ReferenceChangelog Authentication Gorgias API Introduction Authentication Requests Errors Pagination Rate Limits Gorgias REST API Account The Account object Retrieve your accountget List settingsget Create a settingpost Update a set”
  - credential_access | Access signal: partner_gated | https://gorgias.com
      “ndRefer a ClientHelp centerGorgias AcademyCustomer ResourcesOnboarding CompanyAbout GorgiasCareersEventsSustainabilityPeople resourcesGorgias PartnersBecome a PartnerAffiliate programPartner LoginGorgias brandHey AI, learn about us The Conversational AI platfo”
  - credential_access | Access signal: free | https://gorgias.com
      “. Protected investment Scales with you. From 100 tickets a month to 100,000. Same platform. Start driving revenue from every conversation Start free. No credit card required. Live on your store in under an hour. Book a demoSign up for free Product Industries C”
  - credential_access | Access signal: trial | https://developers.gorgias.com/docs
      “s) OAuth2 Bearer Token OAuth2 Scopes Building a Public App Overview Building a high-quality Gorgias app 1. Register on Developer Portal & Get Gorgias Sandbox Account 2. Create a Draft App submission form 3. Set up OAuth2 4. Build and test your app 5. Submit ap”
  - credential_access | Access signal: trial | https://developers.gorgias.com/docs/private-vs-public-app
      “s) OAuth2 Bearer Token OAuth2 Scopes Building a Public App Overview Building a high-quality Gorgias app 1. Register on Developer Portal & Get Gorgias Sandbox Account 2. Create a Draft App submission form 3. Set up OAuth2 4. Build and test your app 5. Submit ap”
  - mcp_available | MCP registry entry: dev.cotlet/gorgias | https://registry.modelcontextprotocol.io/v0/servers?search=gorgias&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/gorgias | https://registry.modelcontextprotocol.io/v0/servers?search=gorgias&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/gorgias | https://registry.modelcontextprotocol.io/v0/servers?search=gorgias&limit=60
      “”

## [20] Gladly — Support and Helpdesk
heuristic: auth=['Basic', 'Personal Access Token', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Third-party/community verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 150133c https://developer.gladly.com/rest/
  page 200 direct 5219c https://gladly.com
  page 200 direct 9445c https://help.gladly.com/developer/docs/lookup-adapter-introduction
  page 200 direct 1383c https://developer.gladly.com/
  page 200 direct 3361c https://developer.gladly.com/llms.txt
  - auth_methods | Supports Basic | https://developer.gladly.com/rest/
      “in a secure location. Delete the old token. Update your applications/scripts with the new token. Authentication BasicAuth Gladly API uses token-based Basic Authentication. API tokens are associated with designated Gladly users. To create and use an API token, ”
  - auth_methods | Supports Personal Access Token | https://developer.gladly.com/rest/
      “Introducing the Gladly API Overview REST API Lookup API Testing Getting Started Permissions Creating API Tokens Replacing/Rotating API Tokens Authentication REST API Agents getList Agents getGet Agent getGet Agent Availability getGet Agent CallRecorder patchUp”
  - auth_methods | Supports Other | https://developer.gladly.com/rest/
      “reeform topics postAdd task comment getGet task comments getGet task comment Teams getList teams getGet team User Identity postCreate a User Identity JWT Topics getList Topics postAdd Topic getGet Topic patchUpdate Topic Webhooks postCreate webhook getList web”
  - api_type | REST API documented | https://developer.gladly.com/rest/
      “Introducing the Gladly API Overview REST API Lookup API Testing Getting Started Permissions Creating API Tokens Replacing/Rotating API Tokens Authentication REST API Agents getList Agents getGet”
  - api_type | REST API documented | https://developer.gladly.com/
      “Gladly DeveloperDeveloper Gladly.com Toggle Menu Home Developer API REST API Chat Web SDK Chat iOS SDK Chat Android SDK Help Center Tutorials Help and Support A platform with people at the heart of it Looking to extend”
  - credential_access | Access signal: trial | https://developer.gladly.com/rest/
      “nd more can be found here. Testing Test the myriad possibilities of the Gladly API in a safe, secure space. We'll enable the Gladly API in a separate sandbox environment, so you can experiment freely without impacting your production environment (or vice versa”
  - credential_access | Access signal: partner_gated | https://gladly.com
      “AI Platform integration Enterprise-grade security Evaluate Why choose Gladly Customer case studies ROI Calculator Company About Careers Stay informed Become a partner Support Help center Implementation guides API reference System Status Gladly in action View d”
  - mcp_available | MCP registry entry: dev.cotlet/gladly | https://registry.modelcontextprotocol.io/v0/servers?search=gladly&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/gladly | https://registry.modelcontextprotocol.io/v0/servers?search=gladly&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/gladly | https://registry.modelcontextprotocol.io/v0/servers?search=gladly&limit=60
      “”

## [21] Slack — Communications and Messaging
heuristic: auth=['OAuth2', 'Personal Access Token', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 37234c https://api.slack.com/docs
  page 200 direct 21885c https://api.slack.com/authentication/oauth-v2
  page 200 direct 11645c https://api.slack.com/authentication/token-types
  page 200 direct 12236c https://slack.com
  page 200 direct 6805c https://slack.com/marketplace/A0BSYHESRJR-hubspot-mcp?install_referrer=marketplace_api
  page 200 direct 30028c https://slack.com/intl/en-in/pricing
  page 200 direct 15724c https://slack.com/intl/en-in/whats-new
  page 200 direct 9673c https://slack.com/intl/en-in/pricing/paid-vs-free
  page 200 direct 40604c https://api.slack.com/llms.txt
  - auth_methods | Supports OAuth2 | https://api.slack.com/docs
      “ll it to your workspace Choose Install to Workspace and approve the permissions. 3 Connect your code or agent runtime Copy the bot token (xoxb-) from OAuth & Permissions. For Socket Mode, create an app-level token (xapp-) with connections:write under Basic Inf”
  - auth_methods | Supports OAuth2 | https://api.slack.com/authentication/oauth-v2
      “APPS Quickstart Resources Slack platform concepts AI in Slack APIs App management App manifests Admin resources Authentication Tokens Installing via OAuth authorization code flow Enterprise-managed authorization Using token rotation Using PKCE Verifying reques”
  - auth_methods | Supports Personal Access Token | https://api.slack.com/authentication/token-types
      “oke them apart: applying them in phases to existing apps as well as new ones. Read more about the motivation behind ending the preview. Legacy custom integration tokens​ These tokens were associated with legacy custom integrations and early Slack integrations ”
  - auth_methods | Supports Other | https://api.slack.com/docs
      “ed": false } } 2 Install it to your workspace Choose Install to Workspace and approve the permissions. 3 Connect your code or agent runtime Copy the bot token (xoxb-) from OAuth & Permissions. For Socket Mode, create an app-level token (xapp-) with connections”
  - auth_methods | Supports Other | https://api.slack.com/authentication/oauth-v2
      “liant to the OAuth 2.0 RFC. Comparing oauth.v2.access and oauth.v2.user.access endpoints​ The oauth.v2.access API method supports generating either a bot token or user token or both. The oauth.v2.user.access API method generates a user token by default followi”
  - api_type | REST API documented | https://api.slack.com/docs
      “mins stay in control of what connects.App approvals → Find your path What brings you here? Examples of how to use these docs. Pick yours and skip the rest. Connect my AI tools “I just need the Slack MCP server in my agent.”One-step setup → Slack MCP server MCP”
  - api_type | REST API documented | https://api.slack.com/authentication/oauth-v2
      “could cause installations to be rejected. OAuth 2.0 refers to the 2.0 version of the OAuth spec, and this is our second version of OAuth 2.0. For the rest of this guide, we'll just refer to it as "OAuth". How it works: a high-level overview​ OAuth allows a use”
  - credential_access | Access signal: admin_approval | https://api.slack.com/docs
      “ls so they know how to build on Slack. Server URL https://mcp.slack.com/mcpCopyCopied https://mcp.slack.com/mcp Remote MCP over HTTP with OAuth. Your workspace admin may need to approve it. No approval yet? Try it in a free Developer Program sandbox.Your AI to”
  - credential_access | Access signal: admin_approval | https://slack.com/intl/en-in/whats-new
      “Slack features straight away? In most cases, yes. Once a feature is released to your workspace, you can start using it immediately. Some features may require admin permission. How can I stay notified about new Slack features? You can bookmark this page to chec”
  - credential_access | Access signal: paid_plan | https://api.slack.com/docs
      “l key into .env, for example ANTHROPIC_API_KEY for the Claude Agent SDK. 5 Run it slack run Then message your agent in Slack. Some AI features need a paid plan; a free Developer Program sandbox has them. Agent quickstartApp quickstart → Search Acme Acme Activi”
  - credential_access | Access signal: paid_plan | https://slack.com/intl/en-in/pricing
      “opers Slack Community Partner programme Partner offers AI era of workThe future of enterprise growth Pricing Talk to salesGet startedSign in Choose a paid subscription that’s built for businesses. Or start with the basics for free, and upgrade at any time. The”
  - credential_access | Access signal: enterprise | https://api.slack.com/authentication/oauth-v2
      “every response indicating which scopes the calling token currently has: x-oauth-scopes: identity.basic,reactions:read Securing OAuth connections for enterprise customers​ When your app completes the OAuth flow with a Slack workspace, we strongly recommend veri”
  - credential_access | Access signal: partner_gated | https://slack.com
      “ces Discover What’s new Resources library Customer stories Events Learn Blog Product tour Help Centre Slack vs Teams Build Developers Slack Community Partner programme Partner offers AI era of workThe future of enterprise growth Watch demoDownload Slack Pricin”
  - credential_access | Access signal: partner_gated | https://slack.com/intl/en-in/pricing
      “ces Discover What’s new Resources library Customer stories Events Learn Blog Product tour Help Centre Slack vs Teams Build Developers Slack Community Partner programme Partner offers AI era of workThe future of enterprise growth Watch demoDownload Slack Pricin”
  - mcp_available | MCP mentioned in vendor docs | https://api.slack.com/docs
      “sIn your browser, nothing to install A coding agent 1 Give your coding agent Slack skills One install adds the Slack developer skills, plus the Slack MCP server in Claude Code and Cursor.Coding agentClaude CodeCursorCodexOther agents /plugin marketplace add sl”
  - mcp_available | MCP mentioned in vendor docs | https://api.slack.com/authentication/oauth-v2
      “token or both. The oauth.v2.user.access API method generates a user token by default following the standard OAuth spec and works out-of-the-box with MCP authorization flows. The oauth.v2.user.access endpoint should be used in scenarios where: You only need use”
  - mcp_available | MCP registry entry: ai.smithery/smithery-ai-slack | https://registry.modelcontextprotocol.io/v0/servers?search=slack&limit=60
      “https://github.com/smithery-ai/mcp-servers”
  - mcp_available | MCP registry entry: ai.wakeshift/slackline | https://registry.modelcontextprotocol.io/v0/servers?search=slack&limit=60
      “https://github.com/wakeshift/apps”
  - mcp_available | MCP registry entry: ai.waystation/slack | https://registry.modelcontextprotocol.io/v0/servers?search=slack&limit=60
      “https://github.com/waystation-ai/mcp”

## [22] Twilio — Communications and Messaging
heuristic: auth=['OAuth2', 'API Key', 'Basic'] api=['REST'] access=Partnership / contact-sales gated mcp=Third-party/community verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 4135c https://www.twilio.com/docs/usage/api
  page 200 direct 4740c https://www.twilio.com/docs/iam/api-keys
  page 200 direct 15795c https://twilio.com
  page 200 direct 20197c https://www.twilio.com/docs/iam/api-keys/key-resource-v1
  page 200 direct 6717c https://www.twilio.com/docs/usage/api-security-reference-guide/secure-auth
  page 200 direct 7252c https://www.twilio.com/docs/usage/api-security-reference-guide/auth-anti-patterns
  page 200 direct 12051c https://www.twilio.com/docs/usage/webhooks/webhook-auth-profiles
  page 200 direct 7001c https://www.twilio.com/docs/usage/secure-credentials
  page 200 direct 14970c https://www.twilio.com/docs/usage/trials
  page 200 direct 400000c https://www.twilio.com/llms.txt
  - auth_methods | Supports OAuth2 | https://www.twilio.com/docs/usage/api
      “Webhooks IntroductionGet started with webhooks Webhooks configuration API OverviewConfigure webhook settingsConfigure webhook rulesAuthenticate with OAuth 2.0, Basic, or DigestSign webhooks with shared keysTest webhook deliveryTrack webhook rule changesChoose ”
  - auth_methods | Supports OAuth2 | https://www.twilio.com/docs/iam/api-keys
      “Keys and Tokens API Keys OverviewCreate API Keys in the ConsoleREST API: Key Resource v1REST API: Key Resource v2010Restricted API KeysAccess Tokens OAuth Apps OverviewAccount OAuth AppsOrganization OAuth AppsOAuth Token APIREST API: OAuth App resourceFAQs Cre”
  - auth_methods | Supports API Key | https://www.twilio.com/docs/iam/api-keys
      “ationsManaged AccountsManaged UsersDomains SCIM API SCIM API overviewOkta SCIM integrationEntra ID SCIM integrationSCIM API reference Keys and Tokens API Keys OverviewCreate API Keys in the ConsoleREST API: Key Resource v1REST API: Key Resource v2010Restricted”
  - auth_methods | Supports API Key | https://www.twilio.com/docs/iam/api-keys/key-resource-v1
      “ationsManaged AccountsManaged UsersDomains SCIM API SCIM API overviewOkta SCIM integrationEntra ID SCIM integrationSCIM API reference Keys and Tokens API Keys OverviewCreate API Keys in the ConsoleREST API: Key Resource v1REST API: Key Resource v2010Restricted”
  - auth_methods | Supports Basic | https://www.twilio.com/docs/usage/webhooks/webhook-auth-profiles
      “Create an OAuth 2.0 AuthProfile What Twilio sends to your authorization server What your authorization server must return When token retrieval fails HTTP Basic Request body parameters HTTP Digest No authentication Manage AuthProfiles List all AuthProfiles Fetc”
  - api_type | REST API documented | https://www.twilio.com/docs/usage/api
      “ations BulkExport API OverviewExports Configuration resourceExports Jobs: custom jobsJobs resourceDays resourceKeyUsage recordsUsage triggers Monitor REST API AlertsEventsBrowse all of Twilio's APIs API Security OverviewSecure authenticationREST API conceptsEn”
  - api_type | REST API documented | https://www.twilio.com/docs/iam/api-keys
      “Twilio Docs Identity and Access Management (IAM) Getting Started OverviewTest CredentialsREST API: Auth TokenREST API: Secondary Auth Token Accounts REST API: Accounts ResourceSubaccounts Organizations OrganizationsManaged AccountsManaged UsersDomains SCIM API”
  - credential_access | Access signal: trial | https://www.twilio.com/docs/usage/api
      “Skip to contentSkip to navigationSkip to topbar Twilio Docs General Usage Get started Get started with your Twilio trial accountWelcome to the new Twilio consoleA Beginner's Guide to the Command LineSet up your local development environmentTwilio Console Assis”
  - credential_access | Access signal: trial | https://twilio.com
      “ngagement, and the next era of CX. See the findings Pricing Overview All Pricing Transparent pricing with discounts as you scale. Sign up for a free trial—no credit card required. Conversations Conversations Conversation Memory Conversation Orchestrator Conver”
  - credential_access | Access signal: partner_gated | https://twilio.com
      “Webinars Podcasts Customer stories State of Customer Engagement Events Customer data recipes Support and services Help Center Find a partner Become a partner Professional services Support plans Status SendGrid status Segment status Customer Insights Series Dis”
  - credential_access | Access signal: free | https://twilio.com
      “and the next era of CX. See the findings Pricing Overview All Pricing Transparent pricing with discounts as you scale. Sign up for a free trial—no credit card required. Conversations Conversations Conversation Memory Conversation Orchestrator Conversation Inte”
  - mcp_available | MCP registry entry: io.github.codespar/mcp-twilio | https://registry.modelcontextprotocol.io/v0/servers?search=twilio&limit=60
      “https://github.com/codespar/mcp-dev-latam”
  - mcp_available | MCP registry entry: io.github.codespar/mcp-twilio | https://registry.modelcontextprotocol.io/v0/servers?search=twilio&limit=60
      “https://github.com/codespar/mcp-dev-latam”
  - mcp_available | MCP registry entry: io.github.mrfentmen/twilio-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=twilio&limit=60
      “https://github.com/mrfentmen/twilio-mcp”

## [23] Zoho Cliq — Communications and Messaging
heuristic: auth=['OAuth2'] api=['REST'] access=Enterprise-only mcp=None found verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 288617c https://www.zoho.com/cliq/help/restapi/v2/
  page 200 direct 4974c https://zoho.com/cliq
  page 200 direct 18695c https://www.zoho.com/cliq/pricing.html
  page 200 direct 38670c https://www.zoho.com/llms.txt
  - auth_methods | Supports OAuth2 | https://www.zoho.com/cliq/help/restapi/v2/
      “REST API DocumentationAccess Cliq Pricing Help Center Introduction About Cliq REST API Authentication OAuth Token OpenAPI Specification (OAS) HTTP Methods Response Errors API Call Limit MAINTENANCE APIs Bulk Export Conversations Channels M”
  - api_type | REST API documented | https://www.zoho.com/cliq/help/restapi/v2/
      “REST API DocumentationAccess Cliq Pricing Help Center Introduction About Cliq REST API Authentication OAuth Token OpenAPI Specification (OAS) HTTP”
  - api_type | REST API documented | https://www.zoho.com/cliq/pricing.html
      “, and desktop app also. IP restrictions can be applied for specific clients like mobile, and desktop app also. Data encryption both in transit and at rest SSL support Consents Dialogs requesting permissions to access data in extensions and internal tools Secre”
  - credential_access | Access signal: trial | https://zoho.com/cliq
      “have for Modern Communication Collaboration Needs Leader G2 Spring Reports: Grid and Momentum Leader in Business Instant Messaging Start your 15-day free trial Brands using Zoho Cliq Uninterrupted WorkLearn more Your central hub for uninterrupted team collabor”
  - credential_access | Access signal: trial | https://www.zoho.com/cliq/pricing.html
      “arly Yearly -Save 10% Free Try NowGet Started Messaging and channels File storage Meetings with screen share Remote work Chat export Standard Start free trialGet Started Everything in the Free edition + External channels Call recording Custom domain and email ”
  - credential_access | Access signal: free | https://zoho.com/cliq
      “ere you left off. Full-time support Looking for help or a product demo? Get in touch and we’ll be happy to assist you. Try Zoho Cliq for your businessSign up for free”
  - credential_access | Access signal: free | https://www.zoho.com/cliq/pricing.html
      “ions and advanced features squarely intact. If you choose to not subscribe to Zoho Cliq after your trial ends, your account will be downgraded to our free plan, where you can continue to communicate and collaborate with your colleagues. How can I pay? We accep”
  - credential_access | Access signal: enterprise | https://www.zoho.com/cliq/pricing.html
      “rs1TB storageCompare Plans Note: - Networks is available as an add-on for the Cliq Standard plan and above. - Additionally, the Cliq Professional and Enterprise plans include 3 free Networks. - Every org user added to a network will be considered as a network ”
  - credential_access | Access signal: paid_plan | https://www.zoho.com/cliq/pricing.html
      “Take a small tour Zoho Cliq Pricing Zoho Cliq pricing is determined by the customer's country, available currency, and billing frequency. Zoho Cliq paid plans are available with monthly and annual billing. Monthly billing shows the monthly subscription price. ”

## [24] Lark (Larksuite) — Communications and Messaging
heuristic: auth=[] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Insufficient evidence llms_txt=True
  page 200 render 14000c https://open.larksuite.com/document/home/index
  page 200 render 3323c https://open.larksuite.com/document/server-docs/api-call-guide/calling-process/get-access-token
  page 200 render 10908c https://open.larksuite.com
  page 200 render 2624c https://open.larksuite.com/document/home/introduction-to-scope-and-authorization/overview
  page 200 render 2688c https://open.larksuite.com/document/server-docs/getting-started/getting-started
  page 200 render 3564c https://open.larksuite.com/document/mcp_open_tools/overview-of-lark-agent-integration-capabilities
  page 200 render 1988c https://open.larksuite.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list
  page 200 render 19069c https://open.larksuite.com/document/home/introduction-to-custom-app-development/self-built-application-development-process
  page 200 render 5381c https://open.larksuite.com/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message-development-tutorial/introduction
  page 200 direct 10752c https://open.larksuite.com/llms.txt
  - api_type | REST API documented | https://open.larksuite.com/document/server-docs/getting-started/getting-started
      “ocument/server-docs/getting-started/getting-started Markdown Content: Last updated on 2024-02-18 The APIs provided by Lark Open Platform follow the RESTful style, and the format of the request URL is as follows: ![Image 1](https://sf16-sg.larksuitecdn.com/obj/”
  - api_type | REST API documented | https://open.larksuite.com/document/home/introduction-to-custom-app-development/self-built-application-development-process
      “reviewed and published, the enabled capabilities will take effect in the live version. ### Enable API scopes Configure the permissions required for OpenAPI interface calls or SDK interface calls. As shown in the following figure, the list of permissions that n”
  - credential_access | Access signal: free | https://open.larksuite.com/document/home/index
      “og) [Reach a whole new world of Message Cards, with the newly updated Message Card Builder!](https://open.larksuite.com/changelog) [Lark CLI is now open source Empower your workflow with the open-source Lark CLI. Access and manage 12 business domains — includi”
  - credential_access | Access signal: free | https://open.larksuite.com
      “ce experiences [CREATE APP](https://open.larksuite.com/app)[VIEW TUTORIALS](https://open.larksuite.com/document/home/course) * ## Lark CLI, Now Open Source Bring any AI agent to Lark. Up and running in a single command. [Get Started](https://open.larksuite.com”
  - credential_access | Access signal: admin_approval | https://open.larksuite.com/document/home/introduction-to-scope-and-authorization/overview
      “er data ranges while column permissions indicate accessible user data fields. Data permissions are set through the developer console requiring tenant admin approval. For example, User A may access Department B user mobile numbers, with Department B as the row ”
  - credential_access | Access signal: admin_approval | https://open.larksuite.com/document/home/introduction-to-custom-app-development/self-built-application-development-process
      “t versions. When using the test version, the permissions and configurations related to the application will take effect immediately without requiring administrator approval. You can also use the accounts of test enterprise members for testing. For more informa”
  - credential_access | Access signal: partner_gated | https://open.larksuite.com/document/server-docs/getting-started/getting-started
      “ss permissions. When calling APIs, the access token needs to be included in the HTTP header to access resources within the defined permissions. * [Apply for API scopes](https://open.larksuite.com/document/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN). If you want to call”
  - credential_access | Access signal: partner_gated | https://open.larksuite.com/document/home/introduction-to-custom-app-development/self-built-application-development-process
      “Related documents * [Application Authentication](https://open.larksuite.com/document/home/introduction-to-scope-and-authorization/overview) * [Application Review Rules](https://www.larksuite.com/hc/zh-CN/articles/360046527434-%E5%BA%94%E7%94%A8%E5%AE%A1%E6%A0%”
  - credential_access | Access signal: enterprise | https://open.larksuite.com/document/server-docs/getting-started/getting-started
      “e/introduction-to-scope-and-authorization/configure-app-data-permissions). When an app requests permissions for certain APIs (e.g., Contacts, Lark HR Enterprise Edition), it needs to configure the corresponding data permissions and submit them for review. The ”
  - credential_access | Access signal: trial | https://open.larksuite.com/document/home/introduction-to-custom-app-development/self-built-application-development-process
      “ways: * **Create an organization** If you are an enterprise administrator, you can go to the [Lark website](https://www.larksuite.com/), click **Free Trial** in the upper right corner, register, and create an organization account. After creating your account, ”
  - mcp_available | MCP registry entry: ai.meetlark/mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=lark&limit=60
      “”
  - mcp_available | MCP registry entry: ai.meetlark/mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=lark&limit=60
      “”
  - mcp_available | MCP registry entry: com.cuelark/tools | https://registry.modelcontextprotocol.io/v0/servers?search=lark&limit=60
      “https://github.com/cuelark/cuelark-tools-mcp”

## [25] Pumble — Communications and Messaging
heuristic: auth=['OAuth2', 'API Key', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 404 direct 0c https://pumble.com/help/integrations/add-pumble-apps/pumble-api-keys-integration/ ERR HTTP 404
  page 200 direct 7851c https://pumble.com
  page 200 direct 4574c https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/
  page 200 direct 23690c https://pumble.com/pricing
  page 200 direct 4844c https://pumble.com/mcp
  page 200 direct 8281c https://pumble.com/why-use
  page 200 direct 15006c https://pumble.com/llms.txt
  - auth_methods | Supports OAuth2 | https://pumble.com/pricing
      “seat. /month billed annually (or $7.99 if billed monthly) Upgrade All BUSINESS features, plus: Single sign-on (SSO) Manage access using SSO (SAML2, OAuth2) Data retention Decide for how long you want to have your messages and files. Full organization analytics”
  - auth_methods | Supports API Key | https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/
      “space Settings Manage Team Members Billing Pumble Help Center Integrations Pumble API Overview In this article Install API addon Generate an API key Delete API key Valid commands Pumble API Overview 2 min read isidora.komaromi@cake.com Who can use this feature”
  - auth_methods | Supports API Key | https://pumble.com/mcp
      “Pumble. Learn how to connect specific AI tools Security and trust Full control over your AI connection Safety Your agent is connected via secure API keys to prevent unauthorized access. Permissions You control what your AI agent can access with different permi”
  - auth_methods | Supports Other | https://pumble.com/mcp
      “rmissions to limit your AIs access your workspace. STEP 4 Install the app Select Create app to use its app key and install app to use the user and bot tokens. STEP 5 Connect the app to your AI agent Use developer tools (e.g., your terminal) to connect your AI ”
  - api_type | REST API documented | https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/
      “mber of that channel) Listing the channels and DMs that belong to the user who created the key The full list of available actions is available in the Swagger documentation. You can also use the documentation in Swagger, just enter your API key in the Authorize”
  - api_type | REST API documented | https://pumble.com/pricing
      “user names for active as well as invited Pumble members through CAKE Account. Security Data encryption Data encryption Pumble encrypts all data at rest and in transit. SOC 2 SOC 2 Annual audit certification for Service Organization Controls Trust Services Prin”
  - credential_access | Access signal: free | https://pumble.com
      “human-based support 99.99% service uptime level Start chatting with your team • Unlimited users • Unlimited chat history • Free forever Create FREE Account Communication and collaboration software for businesses Book a Demo Log In Sign Up Product Overview Apps”
  - credential_access | Access signal: free | https://pumble.com/pricing
      “n upgrade to the PRO, BUSINESS, or ENTERPRISE plan. Can I try out the paid features? Absolutely! You can try out all features for free for 7 days, no credit card required. You can activate the free trial on the Upgrade page. If you need more time, be sure to c”
  - credential_access | Access signal: partner_gated | https://pumble.com/pricing
      “out all features for free for 7 days, no credit card required. You can activate the free trial on the Upgrade page. If you need more time, be sure to contact our sales team for an extension and a demo. Do you offer any discounts? If you pay annually, you get ~”
  - credential_access | Access signal: enterprise | https://pumble.com/pricing
      “mble experience.Qualifying criteria for a dedicated success rep are: 200 seats for the PRO plan, 120 seats for the BUSINESS plan, or 70 seats for the ENTERPRISE plan. BEST VALUE BUSINESS Administration $ 3.99 per seat Every active user or invited member listed”
  - credential_access | Access signal: paid_plan | https://pumble.com/pricing
      “wire transfers and purchase orders - in which case, it's best to contact us at sales@pumble.com. What is a seat? Each active and invited user on a paid plan requires a paid seat. If you deactivate some user, you free up their paid seat so you can invite a new ”
  - credential_access | Access signal: trial | https://pumble.com/pricing
      “plan. Can I try out the paid features? Absolutely! You can try out all features for free for 7 days, no credit card required. You can activate the free trial on the Upgrade page. If you need more time, be sure to contact our sales team for an extension and a d”
  - mcp_available | MCP mentioned in vendor docs | https://pumble.com
      “p discussions. Packed with Useful Features From integrations to security, Pumble has everything a modern team needs. Integrations External Guests MCP Server Voice Messages Video Messages Scheduling Permissions Analytics Integrations Integrate with different ap”
  - mcp_available | MCP mentioned in vendor docs | https://pumble.com/pricing
      “mmunication and collaboration software for businesses Book a Demo Log In Sign Up Product Overview Apps Integrations What’s New Roadmap API MCP Plans Free Pro Business Enterprise See pricing Features Channels Messages Threads Notifications History Files Guests ”

## [26] Discord — Communications and Messaging
heuristic: auth=['OAuth2', 'API Key', 'Basic', 'Personal Access Token', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Third-party/community verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 193086c https://discord.com/developers/docs/reference
  page 200 direct 207292c https://discord.com/developers/docs/topics/oauth2
  page 200 direct 4064c https://discord.com
  page 200 direct 207292c https://docs.discord.com/developers/topics/oauth2
  page 200 direct 77877c https://docs.discord.com/developers/bots/overview
  page 200 direct 86115c https://docs.discord.com/developers/discord-social-sdk/overview
  page 200 direct 71428c https://docs.discord.com/developers/activities/overview
  page 200 direct 193086c https://docs.discord.com/developers/reference
  page 200 direct 88452c https://docs.discord.com/developers/topics/rate-limits
  page 404 direct 0c https://discord.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://discord.com/developers/docs/reference
      “Companion Apps Social SDK Activities Guides Change Log Reference Developer Portal API & SDK Reference Developer Community API Reference API Reference OAuth2 Opcodes and Status Codes Permissions Rate Limits Threads SDK Reference Social SDK Reference Embedded Ap”
  - auth_methods | Supports OAuth2 | https://discord.com/developers/docs/topics/oauth2
      “. Skip to main content Documentation - Discord home page Search...⌘K Help Center Developer Portal Developer Portal Search... Navigation API Reference OAuth2 Home Bots & Companion Apps Social SDK Activities Guides Change Log Reference Developer Portal API & SDK”
  - auth_methods | Supports API Key | https://discord.com/developers/docs/reference
      “ocess for limiting and preventing excessive requests in accordance with RFC 6585. API users that regularly hit and ignore rate limits will have their API keys revoked, and be blocked from the platform. For more information on rate limiting of requests, please ”
  - auth_methods | Supports API Key | https://docs.discord.com/developers/reference
      “ocess for limiting and preventing excessive requests in accordance with RFC 6585. API users that regularly hit and ignore rate limits will have their API keys revoked, and be blocked from the platform. For more information on rate limiting of requests, please ”
  - auth_methods | Supports Basic | https://discord.com/developers/docs/reference
      “within your app’s settings. For more information on bots see bots vs user accounts. Using an OAuth2 bearer token gained through the OAuth2 API. Using basic authentication with credentials as the client ID and client secret found on the OAuth2 page of your app’”
  - auth_methods | Supports Basic | https://discord.com/developers/docs/topics/oauth2
      “orted token endpoint authentication methods in token_endpoint_auth_methods_supported: client_secret_basic: send the client ID and client secret using HTTP Basic authentication. client_secret_post: send client_id and client_secret in the form-encoded request bo”
  - auth_methods | Supports Personal Access Token | https://discord.com/developers/docs/reference
      “t secret found on the OAuth2 page of your app’s settings in the format client_id:client_secret as a Base64 encoded string. Only applicable for OAuth2 API token endpoints. For all authentication types, authentication is performed with the Authorization HTTP hea”
  - auth_methods | Supports Personal Access Token | https://docs.discord.com/developers/reference
      “t secret found on the OAuth2 page of your app’s settings in the format client_id:client_secret as a Base64 encoded string. Only applicable for OAuth2 API token endpoints. For all authentication types, authentication is performed with the Authorization HTTP hea”
  - auth_methods | Supports Other | https://discord.com/developers/docs/reference
      “ssage": "Command exceeds maximum size (8000)" } ] } } Authentication Authenticating with the Discord API can be done in one of three ways: Using a bot token found on the Bot page within your app’s settings. For more information on bots see bots vs user account”
  - auth_methods | Supports Other | https://discord.com/developers/docs/topics/oauth2
      “bot users, which are a separate type of user dedicated to automation. Bot users are automatically added to all apps, and are authenticated using the bot token found in your app’s settings. Unlike the normal OAuth2 flow, bot users have full access to most API r”
  - api_type | REST API documented | https://discord.com/developers/docs/reference
      “CDN URLs Uploading Files Editing Message Attachments File Type Filtering Locales API Reference API Reference Copy pageCopy page The Discord API is a REST API that allows you to interact with Discord data from your own applications. It’s the primary way to inte”
  - api_type | REST API documented | https://discord.com/developers/docs/topics/oauth2
      “nge-log"}]},{"tab":"Reference","icon":"code","groups":[{"group":"API Reference","pages":[{"title":"API Reference","description":"The Discord API is a REST API that allows you to interact with Discord data from your own applications. It's the primary way to int”
  - credential_access | Access signal: partner_gated | https://discord.com/developers/docs/topics/oauth2
      “t approval from Discord may cause errors or undocumented behavior in the OAuth2 flow. To inquire about access about scopes that are only available to approved partners, speak to your Discord account representative to see if they are a fit for your needs. Name ”
  - credential_access | Access signal: partner_gated | https://docs.discord.com/developers/topics/oauth2
      “t approval from Discord may cause errors or undocumented behavior in the OAuth2 flow. To inquire about access about scopes that are only available to approved partners, speak to your Discord account representative to see if they are a fit for your needs. Name ”
  - mcp_available | MCP registry entry: ai.agentapigate/telegram-discord-twitch-kick-medium-pinterest-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=discord&limit=60
      “”
  - mcp_available | MCP registry entry: ai.agentapihub/telegram-discord-twitch-kick-medium-pinterest-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=discord&limit=60
      “”
  - mcp_available | MCP registry entry: ai.smithery/Danushkumar-V-mcp-discord | https://registry.modelcontextprotocol.io/v0/servers?search=discord&limit=60
      “https://github.com/Danushkumar-V/mcp-discord”

## [27] Telegram — Communications and Messaging
heuristic: auth=['OAuth2', 'Basic', 'Other'] api=[] access=Admin approval / app review mcp=Third-party/community verdict=Insufficient evidence llms_txt=True
  page 200 direct 523400c https://core.telegram.org/bots/api
  page 200 direct 18870c https://core.telegram.org/api
  page 200 direct 18822c https://core.telegram.org
  page 200 direct 8212c https://core.telegram.org/bots
  page 200 direct 55361c https://core.telegram.org/bots/features
  page 200 direct 10602c https://core.telegram.org/widgets/login
  page 200 direct 3959c https://core.telegram.org/bots/inline
  page 200 direct 19411c https://core.telegram.org/bots/payments
  page 200 direct 25151c https://core.telegram.org/api/auth
  page 200 direct 4518c https://core.telegram.org/llms.txt
  - auth_methods | Supports OAuth2 | https://core.telegram.org/bots/api
      “. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat”
  - auth_methods | Supports OAuth2 | https://core.telegram.org/widgets/login
      “ication using any OIDC-compatible library or authentication platform (e.g., Keycloak, Authentik, Auth0 etc.). Our implementation follows the standard Authorization Code Flow with PKCE support. For an in-depth understanding of the general OIDC flow, please refe”
  - auth_methods | Supports Basic | https://core.telegram.org/widgets/login
      “Client ID and Client Secret (base64(client_id:client_secret)). POST https://oauth.telegram.org/token Content-Type: application/x-www-form-urlencoded Authorization: Basic <BASE64_CREDENTIALS> grant_type=authorization_code& code=<AUTHORIZATION_CODE>& redirect_ur”
  - auth_methods | Supports Other | https://core.telegram.org/bots
      “ework required to integrate your code. To get started, message @BotFather on Telegram to register your bot and receive its authentication token. Your bot token is its unique identifier – store it in a secure place, and only share it with people who need direct”
  - auth_methods | Supports Other | https://core.telegram.org/widgets/login
      “n the login flow completes, the callback may receive either a success payload (user data) or an error. Field Type Description id_token string An OIDC JWT token containing user claims. Important: Verify the validity of ID token server-side user UserData Decoded”
  - credential_access | Access signal: admin_approval | https://core.telegram.org/bots/api
      “Yes A JSON-serialized object describing the message to be sent getUserChatBoosts Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object. Parameter Type Required Descriptio”
  - credential_access | Access signal: paid_plan | https://core.telegram.org/bots/api
      “l. Bot-specified invoice payload. Can be available only for “invoice_payment” transactions. subscription_period Integer Optional. The duration of the paid subscription. Can be available only for “invoice_payment” transactions. paid_media Array of PaidMedia Opt”
  - credential_access | Access signal: paid_plan | https://core.telegram.org/bots/features
      “hats where it has the relevant paid-media permission and chats managed through a Business Connection. Subscription Plans Developers are able to offer paid subscriptions to their bot – adding multiple tiers of content and features tailored to their audience. Re”
  - credential_access | Access signal: free | https://core.telegram.org/api
      “egram messages for an interface. The Telegram API and TDLib allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the Gateway API allows any business, app or website to send verification codes through”
  - credential_access | Access signal: free | https://core.telegram.org
      “egram messages for an interface. The Telegram API and TDLib allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the Gateway API allows any business, app or website to send verification codes through”
  - credential_access | Access signal: trial | https://core.telegram.org/bots/features
      “nt providers. Here is a quick start guide to implement payments: Pick a provider and obtain the proper token as well as a test token from the "Stripe TEST MODE" provider. Implement payments via the appropriate API methods. Test your implementation by using you”
  - credential_access | Access signal: trial | https://core.telegram.org/bots/payments
      “will find the necessary methods for building your payment implementation in the Payments Section of the Bot API Manual. Testing Payments: the 'Stripe TEST MODE' Provider While you're still developing and testing payments for your bot, use the “Stripe TEST MODE”
  - mcp_available | MCP registry entry: ai.agentapigate/telegram-discord-twitch-kick-medium-pinterest-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=telegram&limit=60
      “”
  - mcp_available | MCP registry entry: ai.agentapihub/telegram-discord-twitch-kick-medium-pinterest-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=telegram&limit=60
      “”
  - mcp_available | MCP registry entry: ai.awraiter/telegram | https://registry.modelcontextprotocol.io/v0/servers?search=telegram&limit=60
      “https://github.com/MediaZione/AwrAiter”

## [28] WhatsApp Business — Communications and Messaging
heuristic: auth=['OAuth2'] api=['REST'] access=Partnership / contact-sales gated mcp=None found verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 18513c https://developers.facebook.com/docs/whatsapp/cloud-api
  page 200 direct 12602c https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
  page 200 direct 12940c https://developers.facebook.com/docs/whatsapp
  page 200 direct 10164c https://developers.facebook.com/documentation/business-messaging/whatsapp/access-tokens
  page 200 direct 19357c https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates
  page 200 direct 5061c https://developers.facebook.com/documentation/business-messaging/whatsapp/direct-send/send-utility-and-authentication-messages
  page 200 direct 15480c https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/authentication-templates/authentication-templates
  page 200 direct 9680c https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/authentication-templates/authentication-best-practices
  page 200 direct 6235c https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/authentication-templates/error-signals
  page 200 direct 6068c https://developers.facebook.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.facebook.com/docs/whatsapp/cloud-api
      “hrub.com/webhooks&quot; &#125;, &quot;id&quot;: &quot;106540352242922&quot; &#125; ``` ### Authentication and authorization Authentication uses OAuth (not 2.0) access tokens, while permissions restrict access to specific resources. - [Learn more about access t”
  - api_type | REST API documented | https://developers.facebook.com/docs/whatsapp/cloud-api
      “urely delivered to the destination chosen by each business. Cloud API uses industry standard encryption techniques to protect data in transit and at rest. Cloud API uses Graph API for sending messages and Webhooks for receiving events, and both operate over in”
  - api_type | REST API documented | https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
      “gnup - [Become a partner](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/overview) - [View WhatsApp API OpenAPI Specification](https://github.com/meta/openapi) --- Full documentation index for this product: https:/”
  - credential_access | Access signal: trial | https://developers.facebook.com/docs/whatsapp/cloud-api
      “s-messaging/whatsapp/get-started), a test WhatsApp account, test Messaging account, and test business phone number are automatically created for you. Test accounts and test phone numbers are useful for testing purposes, as they have relaxed messaging limits an”
  - credential_access | Access signal: trial | https://developers.facebook.com/docs/whatsapp
      “scription Session Initiation Protocol Call button messages and deep links Integration patterns Integration examples Reference Troubleshooting Calling sandbox account App Review guidelines Pricing FAQ Groups Overview Get started Group management Group messaging”
  - credential_access | Access signal: partner_gated | https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
      “rs) — allow businesses already using the WhatsApp Business app to connect their existing account and phone number to Cloud API via Embedded Signup - [Become a partner](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers”
  - credential_access | Access signal: partner_gated | https://developers.facebook.com/docs/whatsapp
      “late messages Product carousel messages Product carousel template messages Single-product messages Single-product template messages Partners Overview Become a partner Become a Tech Provider Become a Technology Partner with the Reseller add-on Become a Measurem”
  - credential_access | Access signal: admin_approval | https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
      “n/development/create-an-app/whatsapp-use-case#permissions-and-features) - View required and optional permissions for this use case and add them to an App Review submission, if applicable. - [**Quickstart**](https://developers.facebook.com/documentation/develop”
  - credential_access | Access signal: admin_approval | https://developers.facebook.com/docs/whatsapp
      “n Initiation Protocol Call button messages and deep links Integration patterns Integration examples Reference Troubleshooting Calling sandbox account App Review guidelines Pricing FAQ Groups Overview Get started Group management Group messaging Webhooks Error ”

## [29] Aircall — Communications and Messaging
heuristic: auth=['OAuth2', 'API Key', 'Basic', 'Personal Access Token'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 458739c https://developer.aircall.io/api-references/
  page 200 direct 3970c https://developer.aircall.io/tutorials/basic-authentication/
  page 200 direct 7936c https://aircall.io
  page 200 direct 145841c https://developers.aircall.io/images/api-references/authentication/oauth-e7de2c2f.png
  page 200 direct 458739c https://developers.aircall.io/api-references
  page 200 direct 458739c https://developers.aircall.io/api-references/
  page 200 direct 60103c https://developers.aircall.io/images/api-references/webhooks/inbound_call_flow-317b866a.png
  page 200 direct 9938c https://developers.aircall.io/images/api-references/webhooks/outbound_call_flow-38f03056.png
  page 200 direct 58724c https://developers.aircall.io/images/api-references/webhooks/inbound_sms_flow-a3c820f2.png
  page 200 direct 979c https://developer.aircall.io/llms.txt
  - auth_methods | Supports OAuth2 | https://developer.aircall.io/api-references/
      “API References Guides Start building REST API Authentication Introduction OAuth ﹣ Technology Partners Basic Auth ﹣ Aircall customers Rate limiting Pagination Errors Versioning Versioning Strategy Content-Type Announcements APIS l”
  - auth_methods | Supports OAuth2 | https://developer.aircall.io/tutorials/basic-authentication/
      “ranscripts and Insights Call summaries Retrieve playbook results QA & Call Evaluations FOUNDATIONS Authentication Overview Authenticate with API Keys OAuth implementation guide Webhooks Overview Webhook setup for integration builders Calls Overview How to work”
  - auth_methods | Supports API Key | https://developer.aircall.io/api-references/
      “﹣ Aircall customers As an Aircall customer, an api_id and api_token are needed to use Aircall Public API: go to your Company's Settings page. In the API Keys section, click on Add a new API key and get your api_token and api_token. Do not forget to copy/paste ”
  - auth_methods | Supports API Key | https://developer.aircall.io/tutorials/basic-authentication/
      “st Call Transcripts and Insights Call summaries Retrieve playbook results QA & Call Evaluations FOUNDATIONS Authentication Overview Authenticate with API Keys OAuth implementation guide Webhooks Overview Webhook setup for integration builders Calls Overview Ho”
  - auth_methods | Supports Basic | https://developer.aircall.io/api-references/
      “API References Guides Start building REST API Authentication Introduction OAuth ﹣ Technology Partners Basic Auth ﹣ Aircall customers Rate limiting Pagination Errors Versioning Versioning Strategy Content-Type Announcements APIS list User V1 User overview List ”
  - auth_methods | Supports Basic | https://developers.aircall.io/api-references
      “API References Guides Start building REST API Authentication Introduction OAuth ﹣ Technology Partners Basic Auth ﹣ Aircall customers Rate limiting Pagination Errors Versioning Versioning Strategy Content-Type Announcements APIS list User V1 User overview List ”
  - auth_methods | Supports Personal Access Token | https://developer.aircall.io/api-references/
      “igns are now available via the public API: Retrieve a Campaign, List all Campaigns, Retrieve Campaign statistics, and List Campaign call outcomes. An API token has company-wide access to Campaigns. See Outbound Campaigns for details. 17-09-2026 Retrieve a Camp”
  - auth_methods | Supports Personal Access Token | https://developers.aircall.io/api-references
      “igns are now available via the public API: Retrieve a Campaign, List all Campaigns, Retrieve Campaign statistics, and List Campaign call outcomes. An API token has company-wide access to Campaigns. See Outbound Campaigns for details. 17-09-2026 Retrieve a Camp”
  - api_type | REST API documented | https://developer.aircall.io/api-references/
      “API References Guides Start building REST API Authentication Introduction OAuth ﹣ Technology Partners Basic Auth ﹣ Aircall customers Rate limiting Pagination Errors Versioning Versioning Strategy”
  - api_type | REST API documented | https://developer.aircall.io/tutorials/basic-authentication/
      “o build voice and messaging experiences with APIs, webhooks, and AI-native tools. Classic integrations Connect Aircall to any business tool using our REST API and webhooks. AI integrations Build MCP-compliant integrations for Aircall's AI Virtual Agent. 🚧 Comi”
  - credential_access | Access signal: admin_approval | https://developer.aircall.io/api-references/
      “isplays the authorization window. Only users who are Admins will be able to see this window, others will be redirected to the Download page. Once the Admin consented to the permissions the app is requesting (scope=public_api), Aircall loads the redirect_uri UR”
  - credential_access | Access signal: admin_approval | https://developers.aircall.io/api-references
      “isplays the authorization window. Only users who are Admins will be able to see this window, others will be redirected to the Download page. Once the Admin consented to the permissions the app is requesting (scope=public_api), Aircall loads the redirect_uri UR”
  - credential_access | Access signal: free | https://developer.aircall.io/api-references/
      “a 200 HTTP Code! During development, you can create SSH tunnels to your local environment. At Aircall, we use and recommend ngrok which is free and open-source. Web server Once the endpoints are registered, a simple web server is needed in order to receive eve”
  - credential_access | Access signal: free | https://developers.aircall.io/api-references
      “a 200 HTTP Code! During development, you can create SSH tunnels to your local environment. At Aircall, we use and recommend ngrok which is free and open-source. Web server Once the endpoints are registered, a simple web server is needed in order to receive eve”
  - credential_access | Access signal: partner_gated | https://developer.aircall.io/tutorials/basic-authentication/
      “essages: Skipping-inbox Embed Aircall Overview Embed Aircall in a CRM sidebar Analytics Overview Build your own reports PUBLISH How to publish an App Partner program Plan your integration Build & Launch Assets Icons, logo, colors and fonts TOOLS Aircall Everyw”
  - credential_access | Access signal: partner_gated | https://aircall.io
      “A View our success stories hub → Partners Build an integration Become a Channel Partner Meet our Partners Partner stories Become an Affiliate Partner Talk to SalesGet free access Customer communications, evolved with AI that handles customer interactions, end ”
  - mcp_available | MCP mentioned in vendor docs | https://developer.aircall.io/tutorials/basic-authentication/
      “lic vs Private app Your first API call Best practices Feedback & Feature requests Aircall AI Discover Aircall AI What can you build Connect with your MCP Register a Public MCP MCP FAQs AI Voice Agent (AIVA) AI-powered outbound calls Log Voice Agent calls AI As”
  - mcp_available | MCP registry entry: dev.cotlet/aircall | https://registry.modelcontextprotocol.io/v0/servers?search=aircall&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/aircall | https://registry.modelcontextprotocol.io/v0/servers?search=aircall&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/aircall | https://registry.modelcontextprotocol.io/v0/servers?search=aircall&limit=60
      “”

## [30] Vonage — Communications and Messaging
heuristic: auth=['API Key', 'Basic', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 24873c https://developer.vonage.com/en/getting-started/concepts/authentication
  page 200 direct 9084c https://developer.vonage.com
  page 404 direct 0c https://developer.vonage.com/en/video/guides/authentication.md ERR HTTP 404
  page 200 direct 4897c https://developer.vonage.com/video/guides/create-token
  page 200 direct 22810c https://www.vonage.com/communications-apis/pricing
  page 200 direct 6969c https://developer.vonage.com/api/pricing
  page 200 direct 3721c https://developer.vonage.com/api/pricing.v2
  page 200 direct 7671c https://developer.vonage.com/messages/technical-details
  page 200 direct 20003c https://developer.vonage.com/llms.txt
  - auth_methods | Supports API Key | https://developer.vonage.com/en/getting-started/concepts/authentication
      “rning Center View All docs Authentication Vonage APIs support different authentication methods depending on which product you are using: API{filter} API Key and Secret (Header) JSON Web Token (JWT) Accounts Application Audit Channel Manager Conversation Conver”
  - auth_methods | Supports API Key | https://developer.vonage.com/api/pricing
      “fied country. gethttps://rest.nexmo.com/account/get-pricing/outbound/:type Authentication Key Description Where Example Authorization Base64 encoded API key and secret joined by a colon. Read more Headers Basic <base64> Path Parameters type string Required The”
  - auth_methods | Supports Basic | https://developer.vonage.com/en/getting-started/concepts/authentication
      “ght Pricing v1 Pricing v2 Programmable SIP Quality on Demand Redact Reports SMS Verify (Legacy) Verify2 Voice3 Video 1 Messages supports both JWT and Basic authentication, however basic authentication does not support webhooks or advanced features such as ACLs”
  - auth_methods | Supports Basic | https://developer.vonage.com/messages/technical-details
      “on and Location messages are supported as Suggestion Chips in text, card, and carousel type messages Authentication The Messages API supports either Basic authentication or JWT (JSON Web Token) authentication, but there are some important differences between t”
  - auth_methods | Supports Other | https://developer.vonage.com/en/getting-started/concepts/authentication
      “onage APIs support different authentication methods depending on which product you are using: API{filter} API Key and Secret (Header) JSON Web Token (JWT) Accounts Application Audit Channel Manager Conversation Conversion Device Location Retrieval Dispatch Ext”
  - auth_methods | Supports Other | https://developer.vonage.com
      “curity protections that prevent fraud and validate users. Prevent fraud with two-factor authentication Authenticate your end-users where they prefer JWT authentication available Real-time Monitoring Fraud Notification Prevent fraud with two-factor authenticati”
  - api_type | REST API documented | https://developer.vonage.com
      “arn the basic concepts of the Vonage Video API platform, including how users can communicate through video, voice, and messaging. Unified Video Video REST API Basic API Functionality Client SDKs Server SDKs Reference App Video REST API Basic API Functionality ”
  - api_type | REST API documented | https://developer.vonage.com/api/pricing
      “ng API Version 1 Version 2 The API to retrieve pricing information. Please note the Pricing API is rate limited to one request per second. Download OpenAPI Specification Available Operations Retrieve outbound pricing for a specific country. Retrieve outbound p”
  - credential_access | Access signal: free | https://developer.vonage.com
      “k Features Low Code and AI Privacy and Security Learning Center Most Popular Video Messaging Verify Identity Voice Ready to start building? Create a free account now! Experience seamless connectivity, real-time messaging, and crystal-clear voice and video call”
  - credential_access | Access signal: free | https://www.vonage.com/communications-apis/pricing
      “trial user will need to switch to an offered pay as you go, fixed price, or tiered pricing plan. Try it free Start developing now with free credit. No credit card required. Start coding API Pricing FAQs What Is an API? Select to expand or collapse this FAQ ans”
  - credential_access | Access signal: partner_gated | https://www.vonage.com/communications-apis/pricing
      “ge marks are registered trademarks of Vonage or its affiliates in the United States and other countries. Quick Links Marketplace Developer center Become a partner System status Download apps Support Referrals Global contact Corporate About us Newsroom Events C”
  - credential_access | Access signal: trial | https://www.vonage.com/communications-apis/pricing
      “and a varying usage quota. The higher the fee, the higher the quota. It’s then up to each user to determine which tier best suits their needs. The Free Trial API Pricing Model Select to expand or collapse this FAQ answer. This is perhaps better described as a ”
  - mcp_available | MCP registry entry: io.github.Vonage/vonage-documentation-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=vonage&limit=60
      “https://github.com/Vonage/vonage-mcp-server-documentation”

## [31] Google Ads — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2', 'Personal Access Token', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 13104c https://developers.google.com/google-ads/api/docs/start
  page 200 direct 24785c https://developers.google.com/google-ads/api/docs/api-policy/developer-token
  page 200 direct 11858c https://developers.google.com/google-ads/api/docs/api-policy/access-levels
  page 200 direct 2325c https://developers.google.com/google-ads
  page 200 direct 11991c https://developers.google.com/google-ads/api/docs/oauth/overview
  page 200 direct 20762c https://developers.google.com/google-ads/api/docs/oauth/access-model
  page 200 direct 15971c https://developers.google.com/google-ads/api/docs/oauth/service-accounts
  page 200 direct 11311c https://developers.google.com/google-ads/api/docs/oauth/user-authentication
  page 200 direct 19156c https://developers.google.com/google-ads/api/docs/oauth/single-user-authentication
  page 200 direct 16636c https://developers.google.com/google-ads/api/docs/oauth/multi-user-authentication
  page 404 direct 0c https://developers.google.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://developers.google.com/google-ads/api/docs/start
      “account workflow User authentication workflow Overview Single-user authentication workflow Multi-user authentication workflow Security requirements OAuth 2.0 internals Set up a Google API Console project for authorization Credential management Multi-party appr”
  - auth_methods | Supports OAuth2 | https://developers.google.com/google-ads/api/docs/api-policy/developer-token
      “existing code will continue working without any changes. Your API access levels are determined by the Google Cloud project you used to generate your OAuth credentials. If your app uses the user authentication workflow, then this is the project that owns your O”
  - auth_methods | Supports Personal Access Token | https://developers.google.com/google-ads/api/docs/api-policy/developer-token
      “eloper token. There are two possibilities: Your developer token access might be revoked for inactivity: Under Google policies, Google may revoke your API token if it's not used consecutively for 90 days. If you haven't used your developer token in a while, its”
  - auth_methods | Supports Other | https://developers.google.com/google-ads/api/docs/start
      “and use Google Ads API Explorer Google Ads Query Builder Google Ads Query Validator Authentication and authorization Overview Access model overview Service account workflow User authentication workflow Overview Single-user authentication workflow Multi-user au”
  - auth_methods | Supports Other | https://developers.google.com/google-ads/api/docs/api-policy/developer-token
      “th credentials. If your app uses the user authentication workflow, then this is the project that owns your OAuth client ID and secret. If you use the service account workflow, then this is the project that owns your service account. A new signup experience for”
  - api_type | REST API documented | https://developers.google.com/google-ads/api/docs/start
      “del overview, Service account workflow, User authentication workflow, Brand verification, Developer token sunset Install a client library or call REST Client libraries Java, .NET, PHP, Python, Ruby, Perl, Code samples, REST interface Query reports and build GA”
  - api_type | REST API documented | https://developers.google.com/google-ads/api/docs/oauth/overview
      “le Ads access model. See the multi-user authentication workflow or the service account workflow depending on the approach you are using with the rest of the Google APIs that your app is using. I am building an app that manages Google Ads accounts that I alread”
  - credential_access | Access signal: trial | https://developers.google.com/google-ads/api/docs/start
      “ks Develop applications Test and troubleshoot your application Best practices Overview API limits and quotas System limits Troubleshooting Testing Test accounts Error debugging Error types Understand API errors Common errors Partial failures Warnings Policy ex”
  - credential_access | Access signal: trial | https://developers.google.com/google-ads/api/docs/api-policy/developer-token
      “nt to get started. API access is now managed directly in your Google Cloud project: enabling the API grants Test access (15,000 operations per day on test accounts), and you can apply on the Google Ads API Overview page for Explorer access (automated review an”
  - credential_access | Access signal: partner_gated | https://developers.google.com/google-ads/api/docs/api-policy/developer-token
      “ur Google Cloud project, so your existing code should continue to work without any changes. If you need to use a new Google Cloud project, you should apply for API access from your Google Cloud project's Google Ads API Overview page. My developer token was par”
  - mcp_available | MCP mentioned in vendor docs | https://developers.google.com/google-ads/api/docs/start
      “overview Release notes Feature deprecations Get started Introduction Quickstart Handle errors Common errors Next steps Developer toolkit Google Ads MCP server Google Ads API AI agent skills Google Ads API Developer Assistant Overview Install and use Google Ads”
  - mcp_available | MCP mentioned in vendor docs | https://developers.google.com/google-ads/api/docs/api-policy/developer-token
      “for up to 2,880 operations per day on production accounts). Follow the Make your first call quickstart or connect an AI assistant with the Google Ads MCP server. Go to Google Ads API Overview in Cloud Console What's changing? We introduced several changes to t”
  - mcp_available | MCP registry entry: academy.mycontent/google-ads | https://registry.modelcontextprotocol.io/v0/servers?search=google&limit=60
      “”
  - mcp_available | MCP registry entry: ai.adplane/google-ads | https://registry.modelcontextprotocol.io/v0/servers?search=google&limit=60
      “”
  - mcp_available | MCP registry entry: ai.adplane/google-ads | https://registry.modelcontextprotocol.io/v0/servers?search=google&limit=60
      “”

## [32] Meta Ads — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2'] api=[] access=Admin approval / app review mcp=Official verdict=Insufficient evidence llms_txt=True
  page 200 direct 26494c https://developers.facebook.com/docs/marketing-apis
  page 200 direct 9307c https://developers.facebook.com/docs/marketing-api/overview/authorization
  page 200 direct 9307c https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization
  page 200 direct 7912c https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authentication
  page 200 direct 2433c https://developers.facebook.com/documentation/ads-commerce/marketing-api/collaborative-ads/managed-partner-ads/api-guide/prerequisites/generate-access-token-system-user
  page 200 direct 25767c https://developers.facebook.com/documentation/ads-commerce
  page 200 direct 26516c https://developers.facebook.com/documentation/ads-commerce/marketing-api
  page 200 direct 2553c https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview
  page 200 direct 6068c https://developers.facebook.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.facebook.com/docs/marketing-api/overview/authorization
      “em for the `ads_management` or `ads_read` permissions. Your app gets access when they click **Allow**. ```html https://www.facebook.com/v27.0/dialog/oauth? client_id=&lt;YOUR_APP_ID&gt; &amp;redirect_uri=&lt;YOUR_URL&gt; &amp;scope=ads_management ``` **Note:**”
  - auth_methods | Supports OAuth2 | https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization
      “em for the `ads_management` or `ads_read` permissions. Your app gets access when they click **Allow**. ```html https://www.facebook.com/v27.0/dialog/oauth? client_id=&lt;YOUR_APP_ID&gt; &amp;redirect_uri=&lt;YOUR_URL&gt; &amp;scope=ads_management ``` **Note:**”
  - credential_access | Access signal: admin_approval | https://developers.facebook.com/docs/marketing-api/overview/authorization
      “an additional layer of Graph API authorization called [access levels](https://developers.facebook.com/docs/graph-api/overview/access-levels). During [App Review](https://developers.facebook.com/docs/app-review), your app must also request specific permissions ”
  - credential_access | Access signal: admin_approval | https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization
      “an additional layer of Graph API authorization called [access levels](https://developers.facebook.com/docs/graph-api/overview/access-levels). During [App Review](https://developers.facebook.com/docs/app-review), your app must also request specific permissions ”
  - mcp_available | MCP mentioned in vendor docs | https://developers.facebook.com/docs/marketing-apis
      “I Connectors Ads CLI Overview Setup Get started Configuration Command reference Ad creatives Datasets and catalogs Tutorials and recipes Insights Ads MCP Server Overview Get started Available tools Comprehensive reporting Ad creation and management Catalog cre”
  - mcp_available | MCP mentioned in vendor docs | https://developers.facebook.com/documentation/ads-commerce
      “I Connectors Ads CLI Overview Setup Get started Configuration Command reference Ad creatives Datasets and catalogs Tutorials and recipes Insights Ads MCP Server Overview Get started Available tools Comprehensive reporting Ad creation and management Catalog cre”
  - mcp_available | MCP registry entry: ai.adlio/meta-ads | https://registry.modelcontextprotocol.io/v0/servers?search=meta&limit=60
      “”
  - mcp_available | MCP registry entry: ai.adweave/meta-ads-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=meta&limit=60
      “”
  - mcp_available | MCP registry entry: ai.agentapigate/facebook-meta-google-tiktok-ads-library-api-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=meta&limit=60
      “”

## [33] LinkedIn Ads — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2', 'API Key'] api=['REST'] access=Partnership / contact-sales gated mcp=Third-party/community verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 4116c https://learn.microsoft.com/en-us/linkedin/marketing/
  page 200 direct 14321c https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access
  page 200 direct 4301c https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
  page 200 direct 4116c https://learn.microsoft.com/linkedin/marketing
  page 200 direct 17903c https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?view=li-lms-2026-11&toc=/linkedin/marketing/toc.json&bc=/linkedin/breadcrumb/toc.json
  page 200 direct 9835c https://learn.microsoft.com/en-us/linkedin/marketing/quick-start?view=li-lms-2026-11
  page 200 direct 13162c https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/getting-started?view=li-lms-2026-11
  page 200 direct 14159c https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/getting-started?view=li-lms-2026-11
  page 200 direct 7973c https://learn.microsoft.com/en-us/linkedin/marketing/event-management/event-management-overview?view=li-lms-2026-11
  page 200 direct 7292c https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview?view=li-lms-2026-11
  page 404 direct 0c https://learn.microsoft.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access
      “ons. What permissions are available? The following table lists each LinkedIn Marketing API product, who can access it, how to request access, and the OAuth permissions granted upon approval. General Availability (GA) programs are open to all approved developer”
  - auth_methods | Supports OAuth2 | https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
      “ge requires authorization. You can try changing directories. Overview Feedback Summarize this article for me In this article The LinkedIn API uses OAuth 2.0 for member (user) authorization and API authentication. Applications must be authorized and authenticat”
  - auth_methods | Supports API Key | https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?view=li-lms-2026-11&toc=/linkedin/marketing/toc.json&bc=/linkedin/breadcrumb/toc.json
      “s://oauth.pstmn.io/v1/callback as your redirect URL and enable Authorize using browser. Each application is assigned a unique Client ID (Consumer key/API key) and Client Secret. Please make a note of these values as they will be integrated into your applicatio”
  - api_type | REST API documented | https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
      “details, refer to Getting Access to LinkedIn APIs page. Sample Application You can explore the OAuth Sample Applications that enables you to try out RESTful OAuth calls to the LinkedIn Authentication server. The sample app is available in Java. Additionally, y”
  - api_type | REST API documented | https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/getting-started?view=li-lms-2026-11
      “rtising API tiers and how to gain access to them, see Increasing Access. Create an Ad Account Ad Account Sample Request POST https://api.linkedin.com/rest/adAccounts Sample Request Body { "currency": "USD", "name": "Company ABC", "notifiedOnCampaignOptimizatio”
  - credential_access | Access signal: partner_gated | https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access
      “accepting new applications. What permissions are available? The following table lists each LinkedIn Marketing API product, who can access it, how to request access, and the OAuth permissions granted upon approval. General Availability (GA) programs are open to”
  - credential_access | Access signal: partner_gated | https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?view=li-lms-2026-11&toc=/linkedin/marketing/toc.json&bc=/linkedin/breadcrumb/toc.json
      “rmissions and Best Practices for Application Development for additional information. Yes The scopes available to your app depend on which Products or Partner Programs your app has access to. This information is available in the LinkedIn Developer Portal. Your ”
  - credential_access | Access signal: free | https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
      “permissions your integration will require, follow one of the authorization flows to get started. Note There are several third-party libraries in the open source community which abstract the OAuth 2.0 authentication process in every major programming language. ”
  - credential_access | Access signal: admin_approval | https://learn.microsoft.com/en-us/linkedin/marketing/quick-start?view=li-lms-2026-11
      “e a Standard tier access form, submit a screen recording of your app, and share test credentials for your app. Learn more on the Community Management App Review page. Step 4: Get Started with the Lead Sync API If you have an existing integration and need to mi”
  - mcp_available | MCP registry entry: ai.sprites/linkedin-ads | https://registry.modelcontextprotocol.io/v0/servers?search=linkedin&limit=60
      “”
  - mcp_available | MCP registry entry: ai.sprites/linkedin-ads | https://registry.modelcontextprotocol.io/v0/servers?search=linkedin&limit=60
      “https://github.com/sprites-mcp/linkedin-ads-mcp-server”
  - mcp_available | MCP registry entry: ai.sprites/linkedin-ads | https://registry.modelcontextprotocol.io/v0/servers?search=linkedin&limit=60
      “https://github.com/sprites-ai/linkedin-ads-mcp-server”

## [34] GoHighLevel — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2', 'Personal Access Token'] api=['REST'] access=Admin approval / app review mcp=Official verdict=Buildable with limitations llms_txt=False
  page 200 render 658c https://highlevel.stoplight.io/docs/integrations
  page 200 direct 2005c https://marketplace.gohighlevel.com/docs/
  page 200 render 641c https://highlevel.stoplight.io
  page 200 direct 910c https://marketplace.gohighlevel.com/docs/oauth/GettingStarted
  page 200 direct 2358c https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc
  page 404 direct 0c https://highlevel.stoplight.io/llms.txt ERR HTTP 404
  page 200 direct 0c https://marketplace.gohighlevel.com/llms.txt
  - auth_methods | Supports OAuth2 | https://marketplace.gohighlevel.com/docs/
      “stant webhook callbacks.Explore Webhooks → Quick Start Guide Choose Integration Type - Marketplace app or Private integration Set Up Authentication - OAuth 2.0 or Private Integration Token Make Your First API Call - Test with our interactive documentation Buil”
  - auth_methods | Supports OAuth2 | https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc
      “to main content Marketplace DocsHighLevel API ReferenceSDKCLI v3 v3 2023-02-21 2021-07-28 2021-04-15 Sign In Authorization Private Integrations Token OAuth 2.0 MCP Server Rate Limits Versioning Changelog Country List FAQs Marketplace Docs OAuth 2.0 Ad Manager ”
  - auth_methods | Supports Personal Access Token | https://marketplace.gohighlevel.com/docs/
      “ks.Explore Webhooks → Quick Start Guide Choose Integration Type - Marketplace app or Private integration Set Up Authentication - OAuth 2.0 or Private Integration Token Make Your First API Call - Test with our interactive documentation Build & Deploy - Use our ”
  - auth_methods | Supports Personal Access Token | https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc
      “that a user has the right to access specific resources or perform certain actions. HighLevel currently supports two types of authorization:​ Private Integration Token OAuth 2.0 Flow When should I use a Private Integration Token?​ You should use a Private Integ”
  - api_type | REST API documented | https://marketplace.gohighlevel.com/docs/
      “kip to main content Marketplace DocsHighLevel API ReferenceSDKCLI v3 v3 2023-02-21 2021-07-28 2021-04-15 Sign In HighLevel API Documentation Complete REST API documentation for the HighLevel CRM platform.Build powerful integrations with our comprehensive devel”
  - credential_access | Access signal: admin_approval | https://marketplace.gohighlevel.com/docs/oauth/GettingStarted
      “sHighLevel API ReferenceSDKCLI v3 v3 2023-02-21 2021-07-28 2021-04-15 Sign In Getting Started Key Concepts Create a Marketplace App App Testing Guide App Review Guidelines How to Update Your App How to Update Your Pricing App Studio External Billing External A”
  - mcp_available | MCP mentioned in vendor docs | https://marketplace.gohighlevel.com/docs/Authorization/authorization_doc
      “ntent Marketplace DocsHighLevel API ReferenceSDKCLI v3 v3 2023-02-21 2021-07-28 2021-04-15 Sign In Authorization Private Integrations Token OAuth 2.0 MCP Server Rate Limits Versioning Changelog Country List FAQs Marketplace Docs OAuth 2.0 Ad Manager Affiliate ”
  - mcp_available | MCP registry entry: ai.makebox.mcp/gohighlevel | https://registry.modelcontextprotocol.io/v0/servers?search=gohighlevel&limit=60
      “https://github.com/russol07/makebox-gohighlevel-plugin”
  - mcp_available | MCP registry entry: dev.cotlet/gohighlevel | https://registry.modelcontextprotocol.io/v0/servers?search=gohighlevel&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/gohighlevel | https://registry.modelcontextprotocol.io/v0/servers?search=gohighlevel&limit=60
      “”

## [35] Mailchimp — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2', 'API Key', 'Basic'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 2361c https://mailchimp.com/developer/marketing/docs/fundamentals/
  page 200 direct 7154c https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
  page 200 direct 3139c https://mailchimp.com/developer
  page 200 direct 4177c https://mailchimp.com/developer/marketing/api-concepts/authentication
  page 200 direct 2758c https://mailchimp.com/developer/marketing/api-concepts/authentication/api-keys
  page 200 direct 3810c https://mailchimp.com/developer/marketing/api-concepts/authentication/oauth-2
  page 200 direct 2892c https://mailchimp.com/developer/marketing
  page 200 direct 11244c https://mailchimp.com/developer/marketing/api/root/list
  page 200 direct 3523c https://mailchimp.com/developer/marketing/api-concepts/rate-limits-and-timeouts
  page 200 direct 400000c https://mailchimp.com/llms.txt
  - auth_methods | Supports OAuth2 | https://mailchimp.com/developer/marketing/docs/fundamentals/
      “meters Rate limits and timeouts Errors Webhooks Batch operations Alternative schemas Audiences endpoints (beta) API structure Authentication API keys OAuth 2 Methods and parameters Rate limits and timeouts Errors Webhooks Batch operations Alternative schemas A”
  - auth_methods | Supports OAuth2 | https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
      “at you’ll need Register your application Implement the flow on your server Rotate a client secret Next steps Scroll to top Start developing Set up an OAuth app Copy page This page is for Mailchimp Marketing API. This page walks through implementing OAuth 2 so ”
  - auth_methods | Supports API Key | https://mailchimp.com/developer/marketing/docs/fundamentals/
      “and parameters Rate limits and timeouts Errors Webhooks Batch operations Alternative schemas Audiences endpoints (beta) API structure Authentication API keys OAuth 2 Methods and parameters Rate limits and timeouts Errors Webhooks Batch operations Alternative s”
  - auth_methods | Supports API Key | https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
      “API on behalf of other Mailchimp users. For how the flow works and why it has the steps it does, see OAuth 2. What you’ll need A Mailchimp account An API key, if you want to test against your own account first A redirect URI for your application, the URL Mailc”
  - auth_methods | Supports Basic | https://mailchimp.com/developer/marketing/api-concepts/authentication
      “enticate with an API key or OAuth 2 token API keys and OAuth 2 access tokens are sent the same way. We’ll refer to both as tokens. You can use either HTTP Basic Authentication or Bearer Authentication. HTTP Basic Authentication passes the token as the password”
  - api_type | REST API documented | https://mailchimp.com/developer/marketing/docs/fundamentals/
      “g with MailchimpAPI ReferenceSkip to navigation API structure Copy page This page is for Mailchimp Marketing API. The Marketing API generally follows REST conventions, with some deviations. Resources are typically nouns like subscribers or campaigns. Subresour”
  - api_type | REST API documented | https://mailchimp.com/developer/marketing/api/root/list
      “ceSkip to navigation This page is for Mailchimp Marketing API. API ReferenceRoot List API root resources Copy page GET https://api.mailchimp.com/3.0/ GET /3.0/ cURL curl https://api.mailchimp.com/3.0/ \ -H "Authorization: Bearer <token>" Try it 200Retrieved { ”
  - credential_access | Access signal: partner_gated | https://mailchimp.com/developer/marketing/docs/fundamentals/
      “Batch operations Alternative schemas Audiences endpoints (beta) Mailchimp Marketing API Mailchimp Transactional Tools Release Notes Blog Integration Partner Program Products Mailchimp Marketing API Mailchimp Transactional Resources Tools Release Notes API Stat”
  - credential_access | Access signal: partner_gated | https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
      “n OAuth app Build with AI tools MCP server Agent skills llms.txt Mailchimp Marketing API Mailchimp Transactional Tools Release Notes Blog Integration Partner Program Products Mailchimp Marketing API Mailchimp Transactional Resources Tools Release Notes API Sta”
  - mcp_available | MCP mentioned in vendor docs | https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
      “ort and export contacts Organize contacts with tags Client libraries and SDKs Send your first API request CLI Set up an OAuth app Build with AI tools MCP server Agent skills llms.txt Mailchimp Marketing API Mailchimp Transactional Tools Release Notes Blog Inte”
  - mcp_available | MCP registry entry: com.insightfulpipe/mailchimp | https://registry.modelcontextprotocol.io/v0/servers?search=mailchimp&limit=60
      “https://github.com/Insightful-Pipe/mailchimp-mcp-server”
  - mcp_available | MCP registry entry: io.github.asklokesh/mailchimp-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=mailchimp&limit=60
      “https://github.com/asklokesh/mailchimp-mcp-server”
  - mcp_available | MCP registry entry: io.github.cyanheads/mailchimp-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=mailchimp&limit=60
      “https://github.com/cyanheads/mailchimp-mcp-server”

## [36] Klaviyo — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2', 'API Key', 'Basic'] api=['REST'] access=Admin approval / app review mcp=Official verdict=Buildable with limitations llms_txt=True
  page 200 direct 12645c https://developers.klaviyo.com/en/docs/authenticate_
  page 200 direct 29733c https://developers.klaviyo.com/en/reference/api_overview
  page 200 direct 4028c https://developers.klaviyo.com
  page 200 direct 10745c https://developers.klaviyo.com/en/docs/authenticate_.md
  page 200 direct 31870c https://developers.klaviyo.com/en/docs/set_up_oauth
  page 200 direct 0c https://www.klaviyo.com/settings/account/api-keys
  page 200 direct 8291c https://developers.klaviyo.com/en/docs/create_public_api_key_allow_list
  page 200 direct 9130c https://developers.klaviyo.com/en/docs/create_a_public_oauth_app
  page 200 direct 14756c https://developers.klaviyo.com/en/docs/handle_your_apps_oauth_flow
  page 200 direct 17994c https://developers.klaviyo.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.klaviyo.com/en/docs/authenticate_
      “able, client-side environments only (see Client API reference). Klaviyo provides 3 methods of authentication including private key authentication and OAuth (used to call server-side APIs) and public key authentication (used to call client-side APIs). Read the ”
  - auth_methods | Supports OAuth2 | https://developers.klaviyo.com/en/reference/api_overview
      “ed by checking out our Postman collection guide. Authentication Klaviyo provides 3 methods of authentication including private key authentication and OAuth (used to call server-side APIs) and public key authentication (used to call client-side APIs). Read belo”
  - auth_methods | Supports API Key | https://developers.klaviyo.com/en/docs/authenticate_
      “: Server-side APIs Client-side APIs Private key authentication All /api endpoints use API private keys to authenticate requests. If you do not use an API key for your requests, or if you use a key from the wrong account, your call will return an error. A 401 e”
  - auth_methods | Supports API Key | https://developers.klaviyo.com/en/reference/api_overview
      “entication (used to call client-side APIs). Read below for a quick overview of each method. Private key authentication All /api endpoints use private API keys with API key scopes to authenticate requests. If you do not use an API key for your requests, or if y”
  - auth_methods | Supports Basic | https://developers.klaviyo.com/en/docs/set_up_oauth
      “`state`, handles a denied authorization, and exchanges the `code` (with the stored verifier) for tokens at https://a.klaviyo.com/oauth/token, using `Authorization: Basic <base64 of client_id:client_secret>`. Never send token requests to www.klaviyo.com. 3. Sto”
  - api_type | REST API documented | https://developers.klaviyo.com/en/docs/authenticate_
      “aviyo (opens in a new tab) Privacy Policy (opens in a new tab) Guides Get started Install SDKs Set up your AI agent For agents llms.txt llms-full.txt OpenAPI spec MCP server Agent skills Terms and Privacy (opens in a new tab) Trademarks (opens in a new tab) Se”
  - api_type | REST API documented | https://developers.klaviyo.com/en/reference/api_overview
      “v2025-04-15 v2025-01-15 Changelog Help Center Community Klaviyo API Reference Copy as Markdown View as MarkdownOpen this page as plain Markdown View OpenAPI specThe machine-readable definition this page is generated from Open in Claude↗(opens in a new tab) Ope”
  - credential_access | Access signal: admin_approval | https://developers.klaviyo.com/en/docs/authenticate_
      “s for your app Submit, publish, and manage your app Prepare your app Klaviyo app listing requirements Create help docs for your integration Pass your app review Submit your app for review Create promotional material for your integration Monitor your app Manage”
  - credential_access | Access signal: admin_approval | https://developers.klaviyo.com/en/docs/set_up_oauth
      “ng tips and a glossary of errors, consult our OAuth troubleshooting tips guide. Once your app has successfully configured OAuth, follow our Pass your app review and Submit your app for review guides to get your app in Klaviyo's App Marketplace. Additional reso”
  - credential_access | Access signal: trial | https://developers.klaviyo.com/en/docs/authenticate_
      “Klaviyo object Last updated 2026-11-10Guides Changelog Changelog API versioning and deprecation policy Get started Get started with Klaviyo Create a test account Install a library Authenticate API requests Make a test API request Rate limits, status codes, and”
  - credential_access | Access signal: trial | https://developers.klaviyo.com
      “ery Klaviyo API operation as a typed command from your terminal, to build, test and script your integration, or to give an AI agent the API. Create a test accountLearn how to create a sandbox account that is linked to your production account login. Test your c”
  - mcp_available | MCP mentioned in vendor docs | https://developers.klaviyo.com/en/docs/authenticate_
      “or API usage Review API error alerts Use Klaviyo's Postman collections Klaviyo CLI Create an allowlist for your public API key Glossary index Klaviyo MCP server Available tools Connect to the MCP server Klaviyo Stripe Projects Agent Context Klaviyo text messag”
  - mcp_available | MCP mentioned in vendor docs | https://developers.klaviyo.com/en/reference/api_overview
      “in a new tab) Privacy Policy (opens in a new tab) Guides Get started Install SDKs Set up your AI agent For agents llms.txt llms-full.txt OpenAPI spec MCP server Agent skills Terms and Privacy (opens in a new tab) Trademarks (opens in a new tab) Security (opens”
  - mcp_available | MCP registry entry: com.insightfulpipe/klaviyo | https://registry.modelcontextprotocol.io/v0/servers?search=klaviyo&limit=60
      “https://github.com/Insightful-Pipe/klaviyo-mcp-server”
  - mcp_available | MCP registry entry: com.mcparmory/klaviyo | https://registry.modelcontextprotocol.io/v0/servers?search=klaviyo&limit=60
      “https://github.com/mcparmory/registry”
  - mcp_available | MCP registry entry: com.mcparmory/klaviyo | https://registry.modelcontextprotocol.io/v0/servers?search=klaviyo&limit=60
      “https://github.com/mcparmory/registry”

## [37] systeme.io — Marketing, Ads, Email and Social
heuristic: auth=['API Key'] api=['REST'] access=Self-serve (free) mcp=Official verdict=Ready to build llms_txt=True
  page 200 direct 14136c https://developer.systeme.io/
  page 200 direct 1979c https://systeme.io
  page 200 direct 14136c https://developer.systeme.io/reference
  page 200 direct 9184c https://developer.systeme.io/reference/mailing_automation_email_statistics_overview_get
  page 200 direct 9168c https://developer.systeme.io/reference/mailing_campaign_step_statistics_overview_get
  page 200 direct 9127c https://developer.systeme.io/reference/mailing_newsletter_statistics_overview_get
  page 200 direct 9314c https://help.systeme.io/article/2323-how-to-create-a-public-api-key-on-systeme-io
  page 200 direct 8249c https://systeme.io/pricing
  page 200 direct 32208c https://developer.systeme.io/llms.txt
  - auth_methods | Supports API Key | https://developer.systeme.io/
      “unlocking the API's capabilities. Simply navigate to the profile settings within your Systeme.io dashboard, and generate a new key under the "Public API keys" section. Once you have your key, you're all set to embark on your first API request journey! 🚧 Import”
  - auth_methods | Supports API Key | https://developer.systeme.io/reference
      “unlocking the API's capabilities. Simply navigate to the profile settings within your Systeme.io dashboard, and generate a new key under the "Public API keys" section. Once you have your key, you're all set to embark on your first API request journey! 🚧 Import”
  - api_type | REST API documented | https://developer.systeme.io/
      “fer a seamless integration experience, allowing you to manage contacts, tags, and a variety of other operations integral to our platform. Adhering to RESTful conventions, our API ensures an intuitive and consistent interaction pattern for all users. Getting St”
  - api_type | REST API documented | https://developer.systeme.io/reference
      “fer a seamless integration experience, allowing you to manage contacts, tags, and a variety of other operations integral to our platform. Adhering to RESTful conventions, our API ensures an intuitive and consistent interaction pattern for all users. Getting St”
  - credential_access | Access signal: free | https://systeme.io
      “Your platform for sales funnels email marketing online courses selling online blogging sales funnels Powering 500,000+ entrepreneurs Get your free account now! Click here Free forever No credit card required Doris S Corporate trainer "My online business manage”
  - credential_access | Access signal: free | https://systeme.io/pricing
      “free now En⌄ Choose your plan Monthly billing Annual billing 2 months free Free migration Monthly billingAnnual billing 2 months free Free migration No credit card requiredStart for free No credit card requiredStart for free No credit card requiredStart for fr”
  - mcp_available | MCP mentioned in vendor docs | https://help.systeme.io/article/2323-how-to-create-a-public-api-key-on-systeme-io
      “ategories Affiliation Blog Booking calendar Contact management Courses Customer support Deliverability Editor Emails General› Migrating to systeme.io Model Context Protocol (MCP) Payments Sales funnels On this page 1. What is an API? 2. How does our public API”
  - mcp_available | MCP registry entry: dev.cotlet/systeme-io | https://registry.modelcontextprotocol.io/v0/servers?search=systeme&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/systeme-io | https://registry.modelcontextprotocol.io/v0/servers?search=systeme&limit=60
      “”
  - mcp_available | MCP registry entry: dev.cotlet/systeme-io | https://registry.modelcontextprotocol.io/v0/servers?search=systeme&limit=60
      “”

## [38] Pinterest — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2', 'Basic', 'Personal Access Token'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 3417c https://developers.pinterest.com/docs/getting-started/set-up-app/
  page 200 direct 22785c https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/
  page 200 direct 1661c https://developers.pinterest.com
  page 200 direct 22785c https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/
  page 200 direct 3463c https://developers.pinterest.com/docs/developer-tools/quickstart-tools/
  page 200 direct 2050c https://developers.pinterest.com/docs/developer-tools/token-debugger/
  page 200 direct 3822c https://help.pinterest.com/article/two-factor-authentication
  page 200 direct 3417c https://developers.pinterest.com/docs/getting-started/connect-app/
  page 200 render 1550c https://developers.pinterest.com/docs/api/v5/introduction
  page 200 direct 10040c https://developers.pinterest.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.pinterest.com/docs/getting-started/set-up-app/
      “evel of access. Configure your app's redirect URI We accept multiple redirect URIs when configuring your app. The value given for redirect_uri during OAuth authorization will be matched against the redirect URIs listed in your app profile. They must be an exac”
  - auth_methods | Supports OAuth2 | https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/
      “rmissions, or scopes, for using the API on their behalf. Before you begin Make sure you have the following items before you generate an access token: OAuth prerequisites What you need Why you need it How to get it Your app ID and client secret You will provide”
  - auth_methods | Supports Basic | https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/
      “e collection site, select OAuth under Pinterest REST API (latest) in the left navigation panel. Then select Generate access token. Authentication Use HTTP Basic Authentication: Username: client_id Password: client_secret Authorization Header Authorization: Bas”
  - auth_methods | Supports Basic | https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/
      “e collection site, select OAuth under Pinterest REST API (latest) in the left navigation panel. Then select Generate access token. Authentication Use HTTP Basic Authentication: Username: client_id Password: client_secret Authorization Header Authorization: Bas”
  - auth_methods | Supports Personal Access Token | https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/
      “itHub's secret scanning partner program, which alerts our security team if a Pinterest access token has been leaked in a developer's code commit. Our API tokens, such as access and refresh tokens, are secrets that developers should not share in their code or r”
  - auth_methods | Supports Personal Access Token | https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/
      “itHub's secret scanning partner program, which alerts our security team if a Pinterest access token has been leaked in a developer's code commit. Our API tokens, such as access and refresh tokens, are secrets that developers should not share in their code or r”
  - api_type | REST API documented | https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/
      “s: POST Generate OAuth access token Try out this endpoint with the Pinterest Postman collection. On the collection site, select OAuth under Pinterest REST API (latest) in the left navigation panel. Then select Generate access token. Try out this endpoint with ”
  - api_type | REST API documented | https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/
      “s: POST Generate OAuth access token Try out this endpoint with the Pinterest Postman collection. On the collection site, select OAuth under Pinterest REST API (latest) in the left navigation panel. Then select Generate access token. Try out this endpoint with ”
  - credential_access | Access signal: trial | https://developers.pinterest.com/docs/getting-started/set-up-app/
      “n to test the API without setting up the Oauth flow.Test tokens expire after 24 hours and allow you to explore certain endpoints faster. Sandbox: Our sandbox environment allows you to make test calls without impacting the Pinterest product environment.Learn mo”
  - credential_access | Access signal: trial | https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/
      “ur_code}' \ --data-urlencode 'redirect_uri=http://localhost/' \ --data-urlencode 'continuous_refresh=true' If you want to use an OAuth token in the Sandbox environment, you can generate a Sandbox token by inserting -sandbox into the request URL path. The first”
  - credential_access | Access signal: partner_gated | https://developers.pinterest.com/docs/getting-started/authentication-and-scopes/
      “epeat these steps before 60 days in order to keep the continuous refresh token valid. Once the refresh token has expired, you will need to explicitly request access again by repeating the Authorization Code flow. Once the refresh token has expired, you will ne”
  - credential_access | Access signal: partner_gated | https://developers.pinterest.com/docs/getting-started/set-up-authentication-and-authorization/
      “epeat these steps before 60 days in order to keep the continuous refresh token valid. Once the refresh token has expired, you will need to explicitly request access again by repeating the Authorization Code flow. Once the refresh token has expired, you will ne”
  - credential_access | Access signal: free | https://developers.pinterest.com
      “uidelines Developer & API terms Pinterest terms & privacy Copyright & trademark Resources Pinterest Partners Pinterest Status For businesses Github Open source Stack Overflow Facebook Twitter YouTube © 2026 Pinterest One API to seamlessly integrate with Pinter”
  - mcp_available | MCP mentioned in vendor docs | https://developers.pinterest.com
      “seamlessly integrate with Pinterest Securely plan content, manage ads, upload product feeds, and more. Get started Launch faster than ever! Pinterest MCP is on the way Learn More Launch faster than ever!Pinterest MCP is on the way Learn More Use cases Track Co”
  - mcp_available | MCP registry entry: ai.agentapigate/sec-edgar-crypto-real-estate-pinterest-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pinterest&limit=60
      “”
  - mcp_available | MCP registry entry: ai.agentapigate/telegram-discord-twitch-kick-medium-pinterest-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pinterest&limit=60
      “”
  - mcp_available | MCP registry entry: ai.agentapihub/sec-edgar-crypto-real-estate-pinterest-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=pinterest&limit=60
      “”

## [39] Threads (Meta) — Marketing, Ads, Email and Social
heuristic: auth=['OAuth2'] api=['REST'] access=Admin approval / app review mcp=Official verdict=Buildable with limitations llms_txt=True
  page 200 direct 2267c https://developers.facebook.com/docs/threads
  page 200 direct 6833c https://developers.facebook.com/docs/threads/get-started
  page 200 direct 6068c https://developers.facebook.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developers.facebook.com/docs/threads/get-started
      “xpired permission to your app again. ### Threads user access tokens API authentication is handled by Threads user access tokens that conform to the OAuth 2.0 protocol. Access tokens are app-scoped (unique to the app and user pair) and can be short-lived or lon”
  - api_type | REST API documented | https://developers.facebook.com/docs/threads/get-started
      “](https://developers.facebook.com/documentation/threads/get-started/long-lived-tokens#refresh-a-long-lived-token) before they expire by querying the `GET /refresh_access_token` endpoint. ### Authorization Window The Authorization Window allows your app to get ”
  - credential_access | Access signal: admin_approval | https://developers.facebook.com/docs/threads/get-started
      “ssions at any time. For app users without a role on your app to grant your app these permissions, each permission must first be approved through the [App Review](https://developers.facebook.com/documentation/resp-plat-initiatives/individual-processes/app-revie”
  - credential_access | Access signal: free | https://developers.facebook.com/docs/threads/get-started
      “ount Settings**](https://www.threads.com/settings/account) of the Threads website or mobile app after signing into their account. ## Sample app The open-source [Threads API sample app](https://github.com/fbsamples/threads_api) serves as a practical guide, enab”
  - mcp_available | MCP registry entry: ai.agentapigate/threads-instagram-truthsocial-linkedin-posts-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=threads&limit=60
      “”
  - mcp_available | MCP registry entry: ai.agentapihub/threads-instagram-truthsocial-linkedin-posts-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=threads&limit=60
      “”
  - mcp_available | MCP registry entry: app.threads-mcp/threads | https://registry.modelcontextprotocol.io/v0/servers?search=threads&limit=60
      “”

## [40] SendGrid — Marketing, Ads, Email and Social
heuristic: auth=['API Key'] api=['REST'] access=Partnership / contact-sales gated mcp=Third-party/community verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 15923c https://www.twilio.com/docs/sendgrid/api-reference
  page 200 direct 10904c https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys
  page 200 direct 9974c https://sendgrid.com
  page 200 direct 16003c https://www.twilio.com/docs/sendgrid/api-reference/how-to-use-the-sendgrid-v3-api/authentication
  page 200 direct 15227c https://www.twilio.com/docs/sendgrid/api-reference/how-to-use-the-sendgrid-v3-api/authorization
  page 200 direct 15734c https://www.twilio.com/docs/sendgrid/api-reference/domain-authentication
  page 200 direct 22629c https://www.twilio.com/docs/sendgrid/api-reference/domain-authentication/authenticate-a-domain
  page 200 direct 22114c https://www.twilio.com/docs/sendgrid/api-reference/domain-authentication/get-the-default-authentication
  page 200 direct 20532c https://www.twilio.com/docs/sendgrid/api-reference/domain-authentication/retrieve-an-authenticated-domain
  page 200 direct 400000c https://www.twilio.com/llms.txt
  - auth_methods | Supports API Key | https://www.twilio.com/docs/sendgrid/api-reference
      “t of all SendersGet a specific SenderUpdate a SenderDelete a SenderResend a Sender verification Send Test E-Mail Send a Test Marketing Email Security API Keys API Keys API OverviewCreate API keysRetrieve an existing API KeyRetrieve all API Keys belonging to th”
  - auth_methods | Supports API Key | https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys
      “in ClaudeOpen in CursorOpen in Perplexity Build with AI Connect your AI agentInstall Twilio Skills Accelerate development with AIOn this page Manage API keys Create an API key Store your API key in an environment variable Edit your API key Delete your API key ”
  - api_type | REST API documented | https://www.twilio.com/docs/sendgrid/api-reference
      “Open in CursorOpen in Perplexity Build with AIConnect your AI agentInstall Twilio Skills SendGrid v3 API reference The SendGrid v3 Web API provides a REST interface to send email at scale and ensure your application can handle high volumes. The SendGrid API en”
  - api_type | REST API documented | https://sendgrid.com
      “, proven deliverability, and so much more Send email on a world-class platform that delivers more than 200 billion emails every month—and explore the rest of the Twilio Platform to build a complete solution for verification and identity, alerts, support and sa”
  - credential_access | Access signal: free | https://www.twilio.com/docs/sendgrid/api-reference
      “an email quickstart in your programming language of choice to implement the Mail Send API. C# Go Java Node.js PHP Python Ruby SDKs and tools See our open-source SDKs and tools to integrate with SendGrid. C# Go Java Node.js PHP Python Ruby OpenAPI specification”
  - credential_access | Access signal: free | https://sendgrid.com
      “interruptions, and routing. Try the demo Pricing Overview All Pricing Transparent pricing with discounts as you scale. Sign up for a free trial—no credit card required. Conversations Conversations Conversation Memory Conversation Orchestrator Conversation Inte”
  - credential_access | Access signal: partner_gated | https://sendgrid.com
      “Webinars Podcasts Customer stories State of Customer Engagement Events Customer data recipes Support and services Help Center Find a partner Become a partner Professional services Support plans Status SendGrid status Segment status Test out our voice AI now De”
  - credential_access | Access signal: trial | https://sendgrid.com
      “th pauses, interruptions, and routing. Try the demo Pricing Overview All Pricing Transparent pricing with discounts as you scale. Sign up for a free trial—no credit card required. Conversations Conversations Conversation Memory Conversation Orchestrator Conver”
  - mcp_available | MCP registry entry: io.github.Choppaaahh/sendgrid-mcp-secure | https://registry.modelcontextprotocol.io/v0/servers?search=sendgrid&limit=60
      “https://github.com/Choppaaahh/sendgrid-mcp-secure”
  - mcp_available | MCP registry entry: io.github.Neschadin/sendgrid-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=sendgrid&limit=60
      “https://github.com/Neschadin/sendgrid-mcp”
  - mcp_available | MCP registry entry: io.github.Neschadin/sendgrid-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=sendgrid&limit=60
      “https://github.com/Neschadin/sendgrid-mcp”

## [41] Shopify — Ecommerce
heuristic: auth=['OAuth2', 'API Key', 'Other'] api=['REST', 'GraphQL'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 17371c https://shopify.dev/docs/api/admin-graphql
  page 200 direct 11014c https://shopify.dev/docs/apps/build/authentication-authorization
  page 200 direct 6571c https://shopify.dev
  page 200 direct 21591c https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens
  page 200 direct 7922c https://shopify.dev/docs/api
  page 200 direct 17371c https://shopify.dev/docs/api/admin-graphql/latest
  page 200 direct 130447c https://shopify.dev/docs/api/admin-graphql/latest/full-index
  page 200 direct 30265c https://shopify.dev/docs/api/usage/access-scopes
  page 200 direct 288139c https://shopify.dev/api/admin-graphql/2026-10/objects/queryroot
  page 404 direct 0c https://shopify.dev/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://shopify.dev/docs/api/admin-graphql
      “7 8 9 10 11 12 13 14 15 16 const queryString = `{ products (first: 3) { edges { node { id title } } } }` // `session` is built as part of the OAuth process const client = new shopify.clients.Graphql({session}); const products = await client.query({ data: query”
  - auth_methods | Supports OAuth2 | https://shopify.dev/docs/apps/build/authentication-authorization
      “, so if you're authenticating requests to the Storefront API or the Customer Account API, see Shopify API authentication instead. You don't implement OAuth by hand for most apps. Shopify CLI and the Shopify app templates handle the token flow for you. Anchor t”
  - auth_methods | Supports API Key | https://shopify.dev/api/admin-graphql/2026-10/objects/queryroot
      “e. Show fields Arguments Anchor to handlehandle•String! required Handle of the App. Anchor to appByKeyappByKey•App Retrieves an App by its client ID (API key). Returns the app's configuration, installation status, AccessScope objects, and developer information”
  - auth_methods | Supports Other | https://shopify.dev/docs/apps/build/authentication-authorization
      “s last as long as a staff member's session, while offline tokens persist across sessions. See access tokens. Anchor to ID tokenID token A short-lived JWT that proves a request comes from an authenticated Shopify user. App Bridge issues one to the frontend of a”
  - auth_methods | Supports Other | https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens
      “tials for an access token, with no merchant interaction. Instead of its client secret, an app can authenticate with a client assertion: a short-lived JWT that it signs with its own private key. An app with public distribution can then also get an application-o”
  - api_type | REST API documented | https://shopify.dev/docs/api/admin-graphql
      “h one of the objects listed under QueryRoot. The QueryRoot is the schema’s entry-point for queries. Queries are equivalent to making a GET request in REST. The example shown is a query to get the ID and title of the first three products. Learn more about API u”
  - api_type | REST API documented | https://shopify.dev/docs/apps/build/authentication-authorization
      “fer to protected customer data. Anchor to Key terminologyKey terminology These terms come up across Shopify's authentication flows and throughout the rest of this section. Anchor to Authentication and authorizationAuthentication and authorization Authenticatio”
  - api_type | GraphQL API documented | https://shopify.dev/docs/api/admin-graphql
      “re Orders Privacy Products and collections Retail Shipping and fulfillment Shopify Markets Shopify Payments Store properties Timeline events Webhooks GraphQL Types Full index GraphQL Admin API reference The Admin API lets you build apps and integrations that e”
  - api_type | GraphQL API documented | https://shopify.dev/docs/apps/build/authentication-authorization
      “Access requirements Key terminology Choosing an approach About app authentication Install AI ToolkitAsk about this pageCopy MD Shopify apps call the GraphQL Admin API to read and write store data on behalf of merchants. Before your app can make those calls, it”
  - credential_access | Access signal: partner_gated | https://shopify.dev/docs/api/usage/access-scopes
      “dispute_evidences write_shopify_payments_dispute_evidences Shopify approval required ShopifyPaymentsDisputeEvidence, ShopifyPaymentsDisputeFileUpload Request access from Shopify. read_shopify_payments_dispute_file_uploads write_shopify_payments_dispute_file_up”
  - credential_access | Access signal: partner_gated | https://shopify.dev/api/admin-graphql/2026-10/objects/queryroot
      “ntory management You can only retrieve the last 60 days worth of orders from a store by default. If you want to access older orders, then you need to request access to all orders. For large order datasets, consider using bulk operations. Bulk operations handle”
  - credential_access | Access signal: trial | https://shopify.dev/api/admin-graphql/2026-10/objects/queryroot
      “Example: tag_not:my_tag Anchor to test•boolean Filter by test orders. Test orders are made using the Shopify Bogus Gateway or a payment provider with test mode enabled. Example: test:true Anchor to total_weight•string Filter by the order weight. This filter su”
  - mcp_available | MCP mentioned in vendor docs | https://shopify.dev
      “nd up to date, so it builds correctly instead of guessing. Before you install, make sure you have Node.js 18 or higher. For agent skills and the Dev MCP server, see the [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit) page. #### Claude Code”
  - mcp_available | MCP mentioned in vendor docs | https://shopify.dev/docs/api
      “ion Search query syntax Global IDs Response status codes Limits Idempotent requests Feature previews Dev tools Shopify CLI Shopify AI Toolkit Shopify MCP Shopify GitHub app React Router app package Stores Libraries and templates App data and logic GraphQL Admi”
  - mcp_available | MCP registry entry: ai.agentapigate/amazon-product-walmart-shopify-ecommerce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=shopify&limit=60
      “”
  - mcp_available | MCP registry entry: ai.agentapihub/amazon-product-walmart-shopify-ecommerce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=shopify&limit=60
      “”
  - mcp_available | MCP registry entry: ai.gossiper/shopify-admin-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=shopify&limit=60
      “”

## [42] WooCommerce — Ecommerce
heuristic: auth=['OAuth2', 'API Key', 'Basic', 'Other'] api=['REST', 'GraphQL'] access=Self-serve (free trial / sandbox) mcp=Third-party/community verdict=Ready to build llms_txt=True
  page 200 direct 5537c https://woocommerce.com/document/woocommerce-rest-api/
  page 200 direct 754846c https://woocommerce.github.io/woocommerce-rest-api-docs/
  page 200 direct 5533c https://woocommerce.com/document/woocommerce-rest-api
  page 200 direct 5204c https://woocommerce.com/documentation/woocommerce/getting-started/
  page 200 direct 7719c https://woocommerce.com/pricing/
  page 200 direct 10135c https://woocommerce.com/llms.txt
  page 404 direct 0c https://woocommerce.github.io/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://woocommerce.github.io/woocommerce-rest-api-docs/
      “"wc/v3", query_string_auth: true // Force Basic Authentication as query string true and using under HTTPS } ) Authentication over HTTP You must use OAuth 1.0a "one-legged" authentication to ensure REST API credentials cannot be intercepted by an attacker. Typi”
  - auth_methods | Supports API Key | https://woocommerce.com/document/woocommerce-rest-api/
      “ST API WooCommerce REST API The WooCommerce REST API connects your store to external systems and services. Most integrations require you to generate API keys in WooCommerce and enter them in the external service to establish the connection. This document cover”
  - auth_methods | Supports API Key | https://woocommerce.github.io/woocommerce-rest-api-docs/
      “hon Ruby Introduction Requirements Request/Response Format Errors Parameters Pagination Libraries and Tools Learn more Authentication REST API keys Authentication over HTTPS Authentication over HTTP Index HTTP request Coupons Coupon properties Create a coupon ”
  - auth_methods | Supports Basic | https://woocommerce.github.io/woocommerce-rest-api-docs/
      “HP versions) or file_get_contents('php://input');. The URL generated must have all query string values encoded. Authentication over HTTPS You may use HTTP Basic Auth by providing the REST API Consumer Key as the username and the REST API Consumer Secret as the”
  - auth_methods | Supports Other | https://woocommerce.github.io/woocommerce-rest-api-docs/
      “orting parameters in PHP for example, you would use uksort( $params, 'strcmp' ). Parameters example: oauth_consumer_key=abc123&oauth_signature_method=HMAC-SHA1 Create the signature base string The above values collected so far must be joined to make a single s”
  - api_type | REST API documented | https://woocommerce.com/document/woocommerce-rest-api/
      “erformance Localization Security Store designExpand Mobile AppExpand Get helpExpand Documentation / WooCommerce / Site administration / WooCommerce REST API WooCommerce REST API The WooCommerce REST API connects your store to external systems and services. Mos”
  - api_type | REST API documented | https://woocommerce.github.io/woocommerce-rest-api-docs/
      “Python Ruby Introduction Requirements Request/Response Format Errors Parameters Pagination Libraries and Tools Learn more Authentication REST API keys Authentication over HTTPS Authentication over HTTP Index HTTP request Coupons Coupon properties Create a coup”
  - api_type | GraphQL API documented | https://woocommerce.github.io/woocommerce-rest-api-docs/
      “of this libraries you should contact the respective authors. Tools Some useful tools you can use to access the API include: Insomnia - Cross-platform GraphQL and REST client, available for Mac, Windows, and Linux. Postman - Cross-platform REST client, availabl”
  - credential_access | Access signal: trial | https://woocommerce.github.io/woocommerce-rest-api-docs/
      “abel": "Enable PayPal sandbox", "description": "PayPal sandbox can be used to test payments. Sign up for a <a href=\"https://developer.paypal.com/\">developer account</a>.", "type": "checkbox", "value": "yes", "default": "no", "tip": "PayPal sandbox can be use”
  - credential_access | Access signal: free | https://woocommerce.com/pricing/
      “Hire an expert Get support Sell Extensions Resources Enterprise ecommerce WooCommerce pricing puts you in control WooCommerce is the free, Open Source ecommerce platform for WordPress. Build a custom online store and only pay for the added features you use — n”
  - mcp_available | MCP registry entry: com.addsynapse/woocommerce | https://registry.modelcontextprotocol.io/v0/servers?search=woocommerce&limit=60
      “”
  - mcp_available | MCP registry entry: com.addsynapse/woocommerce | https://registry.modelcontextprotocol.io/v0/servers?search=woocommerce&limit=60
      “”
  - mcp_available | MCP registry entry: com.insightfulpipe/woocommerce | https://registry.modelcontextprotocol.io/v0/servers?search=woocommerce&limit=60
      “https://github.com/Insightful-Pipe/woocommerce-mcp-server”

## [43] BigCommerce — Ecommerce
heuristic: auth=['OAuth2', 'API Key', 'Basic', 'Personal Access Token', 'Other'] api=['REST', 'GraphQL'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 44072c https://developer.bigcommerce.com/docs/start/authentication
  page 200 direct 44072c https://developer.bigcommerce.com/docs/start/authentication/api-accounts
  page 200 direct 18242c https://developer.bigcommerce.com
  page 200 direct 22089c https://docs.bigcommerce.com/developer/docs/integrations/apps/guide/auth
  page 200 render 20494c https://accounts.bigcommerce.com/tokens
  page 200 direct 23646c https://docs.bigcommerce.com/developer/docs/storefront/guides/customer-authentication/customer-login
  page 200 direct 15106c https://docs.bigcommerce.com/developer/docs/storefront/guides/customer-authentication/current-customer
  page 200 direct 80193c https://docs.bigcommerce.com/developer/api-reference/rest/admin/payments/tokens/create-payment-access-token
  page 200 direct 81352c https://docs.bigcommerce.com/developer/api-reference/rest/admin/authentication-apis/storefront-api-tokens/create-token
  page 200 direct 945c https://developer.bigcommerce.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developer.bigcommerce.com/docs/start/authentication
      “s Delete apps carefully Account-level API accounts Creating account-level credentials Revoking account-level API credentials Migrating from legacy to OAuth Legacy API Accounts Benefits of migrating to OAuth How to migrate OAuth scopes Token creation scopes Sto”
  - auth_methods | Supports OAuth2 | https://developer.bigcommerce.com/docs/start/authentication/api-accounts
      “s Delete apps carefully Account-level API accounts Creating account-level credentials Revoking account-level API credentials Migrating from legacy to OAuth Legacy API Accounts Benefits of migrating to OAuth How to migrate OAuth scopes Token creation scopes Sto”
  - auth_methods | Supports API Key | https://docs.bigcommerce.com/developer/api-reference/rest/admin/payments/tokens/create-payment-access-token
      “kens cURL curl -X POST https://api.bigcommerce.com/stores/store_hash/v3/payments/access_tokens \ -H "Accept: application/json" \ -H "X-Auth-Token: <apiKey>" \ -H "Content-Type: application/json" \ -d '{ "order": { "id": 1, "is_recurring": false } }' Try it 201”
  - auth_methods | Supports API Key | https://docs.bigcommerce.com/developer/api-reference/rest/admin/authentication-apis/storefront-api-tokens/create-token
      “-token cURL curl -X POST https://api.bigcommerce.com/stores/store_hash/v3/storefront/api-token \ -H "Accept: application/json" \ -H "X-Auth-Token: <apiKey>" \ -H "Content-Type: application/json" \ -d '{ "expires_at": 1885635176, "allowed_cors_origins": [ "http”
  - auth_methods | Supports Basic | https://developer.bigcommerce.com/docs/start/authentication
      “spect a breach, you will know which resources could be affected. How to migrate Before you update your API connections to use OAuth instead of legacy basic authentication, take the following actions: Create an API account appropriate to your use case. Keeping ”
  - auth_methods | Supports Basic | https://developer.bigcommerce.com/docs/start/authentication/api-accounts
      “spect a breach, you will know which resources could be affected. How to migrate Before you update your API connections to use OAuth instead of legacy basic authentication, take the following actions: Create an API account appropriate to your use case. Keeping ”
  - auth_methods | Supports Personal Access Token | https://developer.bigcommerce.com/docs/start/authentication
      “and the use cases for each. It also contains a reference for available OAuth scopes and provides a compelling list of reasons to migrate from legacy API tokens to OAuth credentials. Every parent set of API credentials that you request for your store is its own”
  - auth_methods | Supports Personal Access Token | https://developer.bigcommerce.com/docs/start/authentication/api-accounts
      “and the use cases for each. It also contains a reference for available OAuth scopes and provides a compelling list of reasons to migrate from legacy API tokens to OAuth credentials. Every parent set of API credentials that you request for your store is its own”
  - auth_methods | Supports Other | https://developer.bigcommerce.com/docs/start/authentication
      “g app identifies itself by sending an API account’s client ID as a query parameter, and our servers return a BigCommerce-generated JSON web token, or JWT, which securely encrypts merchant data. The app can decode the JWT to view the response. For example, the ”
  - auth_methods | Supports Other | https://developer.bigcommerce.com/docs/start/authentication/api-accounts
      “g app identifies itself by sending an API account’s client ID as a query parameter, and our servers return a BigCommerce-generated JSON web token, or JWT, which securely encrypts merchant data. The app can decode the JWT to view the response. For example, the ”
  - api_type | REST API documented | https://developer.bigcommerce.com/docs/start/authentication
      “ion header example requests User-generated JWTs Customer Login API example request BigCommerce-encrypted payload JWTs Same-origin CORS authentication REST Storefront API Developer-configured authentication REST Provider APIs Resources Scroll to top OverviewAPI”
  - api_type | REST API documented | https://developer.bigcommerce.com/docs/start/authentication/api-accounts
      “ion header example requests User-generated JWTs Customer Login API example request BigCommerce-encrypted payload JWTs Same-origin CORS authentication REST Storefront API Developer-configured authentication REST Provider APIs Resources Scroll to top OverviewAPI”
  - api_type | GraphQL API documented | https://developer.bigcommerce.com/docs/start/authentication
      “make an informed choice about which best fits your use case. API or Use Case Store-level API account App-level API account Account-level API account GraphQL Account API, including Users × GraphQL Admin API × × GraphQL Storefront API × B2B REST Management API ×”
  - api_type | GraphQL API documented | https://developer.bigcommerce.com/docs/start/authentication/api-accounts
      “make an informed choice about which best fits your use case. API or Use Case Store-level API account App-level API account Account-level API account GraphQL Account API, including Users × GraphQL Admin API × × GraphQL Storefront API × B2B REST Management API ×”
  - credential_access | Access signal: free | https://developer.bigcommerce.com
      “FIPS, RH-ISAC, GDPR, and CCPA. What makes BigCommerce unique? We strive to open commerce through our open SaaS approach, blending the flexibility of open source with the usability and security of SaaS. It means developers and retailers get a powerhouse commerc”
  - credential_access | Access signal: free | https://accounts.bigcommerce.com/tokens
      “u%2FvnTjX%2FHnTBa9nZ7QbVz4WQ6iqI6b5nkX%2BuMfG9%2F%2FCw%3D%3D#) [Forgot password?](https://login.bigcommerce.com/recover/new) Don't have an account?[Sign up for free](https://www.bigcommerce.com/start-your-trial/)”
  - credential_access | Access signal: partner_gated | https://docs.bigcommerce.com/developer/docs/integrations/apps/guide/auth
      “rg) discusses security considerations, recommendations, and requirements. The following are some requirements and recommendations applicable to apps: Request access tokens with the minimal scope necessary. Keep access tokens and client secrets confidential in ”
  - mcp_available | MCP mentioned in vendor docs | https://developer.bigcommerce.com/docs/start/authentication
      “n Design Deprecations & Sunsets Docs Storefront Admin Integrations B2B AI Tools Additional Docs ArchiveDeprecated Closed Beta Programs Resources Docs MCP Server Product Docs Support Quick Start Sandboxes Tools & SDKs Remote Tunnels Support API Accounts Rate Li”
  - mcp_available | MCP mentioned in vendor docs | https://developer.bigcommerce.com/docs/start/authentication/api-accounts
      “n Design Deprecations & Sunsets Docs Storefront Admin Integrations B2B AI Tools Additional Docs ArchiveDeprecated Closed Beta Programs Resources Docs MCP Server Product Docs Support Quick Start Sandboxes Tools & SDKs Remote Tunnels Support API Accounts Rate Li”
  - mcp_available | MCP registry entry: io.github.mrfentmen/bigcommerce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=bigcommerce&limit=60
      “https://github.com/mrfentmen/awesome-mcps”
  - mcp_available | MCP registry entry: io.github.mrfentmen/bigcommerce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=bigcommerce&limit=60
      “https://github.com/mrfentmen/awesome-mcps”
  - mcp_available | MCP registry entry: io.github.mrfentmen/bigcommerce-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=bigcommerce&limit=60
      “https://github.com/mrfentmen/premium-mcps”

## [44] Salesforce Commerce Cloud — Ecommerce
heuristic: auth=['OAuth2', 'Other'] api=[] access=Partnership / contact-sales gated mcp=Official verdict=Insufficient evidence llms_txt=True
  page 200 render 2169c https://developer.salesforce.com/docs/commerce/commerce-api/overview
  page 200 direct 9215c https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-shopper-apis.html
  page 200 direct 8167c https://developer.salesforce.com/docs/commerce
  page 200 direct 6532c https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-admin-apis.html
  page 200 direct 6410c https://developer.salesforce.com/docs/commerce/commerce-api/guide/sfnext-quick-start-create-bm-github.html
  page 200 direct 5818c https://developer.salesforce.com/docs/commerce/commerce-api/guide/sfnext-quick-start-create-bm.html
  page 200 render 3348c https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/quick-start-landing-page.html
  page 200 render 2181c https://developer.salesforce.com/docs/commerce/retail-cloud/overview
  page 200 direct 547c https://developer.salesforce.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-admin-apis.html
      “ecret, only use alphanumeric passwords. Before you create your API client (or clients) for accessing the SCAPI Admin APIs, you must compile a list of OAuth scopes for each API family that you need to access. All the available scopes are listed in the Authoriza”
  - auth_methods | Supports OAuth2 | https://developer.salesforce.com/docs/commerce/commerce-api/guide/sfnext-quick-start-create-bm-github.html
      “your security, the client secrets are available for download only once and are deleted on subsequent downloads. You use the Account Manager and SLAS client credentials to run the storefront locally. When you run the storefront on MRT, MRT uses the autocreated ”
  - auth_methods | Supports Other | https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-admin-apis.html
      “ken bloat and do not work as expected. For the Token Endpoint Auth Method field, select client_secret_post. For the Access Token Format field, select JWT. In the Redirect URIs field, add http://localhost:8080. Click Save. Find your new API client in the table ”
  - credential_access | Access signal: partner_gated | https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-shopper-apis.html
      “Authorization for Shopper APIs Learn how to set up the Shopper Login and API Access Service (SLAS) so that you can request access tokens for Shopper APIs. Shopper APIs are secured with the Shopper Login and API Access Service (SLAS), but SCAPI Admin APIs are s”
  - mcp_available | MCP mentioned in vendor docs | https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/quick-start-landing-page.html
      “ge.html Markdown Content: # B2C Commerce Quick Start Try out some basic steps for using a few of the B2C Commerce storefront options: * [Agentic MCP Shopper Tools Quick Start (Pilot)](https://developer.salesforce.com/docs/commerce/b2c-commerce/guide/agentic-mc”

## [45] Magento (Adobe Commerce) — Ecommerce
heuristic: auth=['OAuth2', 'API Key', 'Personal Access Token', 'Other'] api=['REST', 'GraphQL'] access=Self-serve (free) mcp=Third-party/community verdict=Ready to build llms_txt=False
  page 200 direct 8568c https://developer.adobe.com/commerce/webapi/get-started/authentication/
  page 200 direct 3752c https://developer.adobe.com/commerce/webapi/rest/
  page 200 direct 1614c https://developer.adobe.com/commerce
  page 200 direct 3316c https://developer.adobe.com/commerce/webapi/rest/authentication/
  page 200 direct 8567c https://developer.adobe.com/commerce/webapi/rest/authentication/server-to-server
  page 200 direct 11287c https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token
  page 200 direct 17677c https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-oauth
  page 200 direct 1927c https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-session
  page 200 direct 15756c https://developer.adobe.com/commerce/php/development/components/attributes
  page 404 direct 0c https://developer.adobe.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://developer.adobe.com/commerce/webapi/get-started/authentication/
      “dentity, specify this token in the Authorization request header on web API calls. Third-party application authentication Third-party applications use OAuth-based authentication to access the web APIs. The third-party Integration registers with Adobe Commerce. ”
  - auth_methods | Supports OAuth2 | https://developer.adobe.com/commerce/webapi/rest/
      “lso supported. Authentication Adobe Commerce REST APIs support multiple authentication methods, including: Third-party applications authenticate with OAuth 1.0a. Mobile applications authenticate using tokens. Administrators and customers are authenticated with”
  - auth_methods | Supports API Key | https://developer.adobe.com/commerce/webapi/rest/authentication/server-to-server
      “ndpoint, data = null) { const accessToken = await this.tokenManager.getValidToken(); const headers = { 'Authorization': `Bearer ${accessToken}`, 'x-api-key': process.env.IMS_CLIENT_ID, 'x-gw-ims-org-id': process.env.IMS_ORG_ID, 'Content-Type': 'application/jso”
  - auth_methods | Supports Personal Access Token | https://developer.adobe.com/commerce/webapi/rest/authentication/
      “ased workflows and automated server-to-server integrations, ensuring secure and appropriate access for different use cases. The traditional admin and integration token generation methods is not supported in SaaS environments. Instead, you must obtain an IMS ad”
  - auth_methods | Supports Personal Access Token | https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token
      “s access to. 4 hours Customer Commerce grants access to resources with the anonymous or self permission. Merchants cannot edit these settings. 1 hour Integration tokens When a merchant creates and activates an integration, Commerce generates a consumer key, co”
  - auth_methods | Supports Other | https://developer.adobe.com/commerce/webapi/rest/authentication/server-to-server
      “, error.message); throw error; } } } module.exports = TokenManager; Step 3: Create an API Client Create an API client that handles authentication, request signing, and error handling. This client will use the token manager to obtain valid access tokens and mak”
  - auth_methods | Supports Other | https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token
      “$oauthParams = [ 'oauth_consumer_key' => $credentials->consumerKey, 'oauth_nonce' => base64_encode(random_bytes(32)), 'oauth_signature_method' => 'HMAC-SHA256', 'oauth_timestamp' => time(), 'oauth_token' => $credentials->accessToken ]; // Create the base strin”
  - api_type | REST API documented | https://developer.adobe.com/commerce/webapi/get-started/authentication/
      “ata-variant=info data-slots=text This topic is for Platform-as-a-Service (PaaS) customers only. Adobe Commerce Cloud Services customers must refer to REST Authentication for details on authentication. For practical implementation guides for Adobe Commerce as a”
  - api_type | REST API documented | https://developer.adobe.com/commerce/webapi/rest/
      “REST API Overview The REST API documentation describes the REST APIs that are available in Adobe Commerce (PaaS) and Adobe Commerce as a Cloud Service (SaaS).”
  - api_type | GraphQL API documented | https://developer.adobe.com/commerce/webapi/rest/
      “d on-premises deployments are not available in Adobe Commerce as a Cloud Service. However, access to similar functionality remains available with the GraphQL APIs. The API reference lists the available endpoints. Authentication In previous versions of Adobe Co”
  - credential_access | Access signal: free | https://developer.adobe.com/commerce/webapi/get-started/authentication/
      “er integration - Complete guide for automated system integration Generate the IMS access token - User authentication guide Adobe Commerce and Magento Open Source allow developers to define web API resources and their permissions in the webapi.xml configuration”
  - credential_access | Access signal: free | https://developer.adobe.com/commerce/webapi/rest/
      “y, content tagging is not supported. Adobe Commerce data-src=/_includes/paas-only.md Adobe Commerce on Cloud, Adobe Commerce on-premises, and Magento Open Source all use the same REST API framework. The REST API documentation describes the REST APIs that are a”
  - mcp_available | MCP registry entry: com.insightfulpipe/magento | https://registry.modelcontextprotocol.io/v0/servers?search=magento&limit=60
      “https://github.com/Insightful-Pipe/magento-mcp-server”
  - mcp_available | MCP registry entry: io.github.juan-cinto-infracommerce/magento-cloud | https://registry.modelcontextprotocol.io/v0/servers?search=magento&limit=60
      “https://github.com/juan-cinto-infracommerce/mcp-magento-cloud”
  - mcp_available | MCP registry entry: io.github.juan-cinto-infracommerce/magento-cloud | https://registry.modelcontextprotocol.io/v0/servers?search=magento&limit=60
      “https://github.com/juan-cinto-infracommerce/mcp-magento-cloud”

## [46] Squarespace — Ecommerce
heuristic: auth=['OAuth2', 'API Key'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 2231c https://developers.squarespace.com/commerce-apis/overview
  page 200 direct 4111c https://developers.squarespace.com/commerce-apis/authentication-and-permissions
  page 200 direct 2005c https://developers.squarespace.com
  page 200 direct 2405c https://developers.squarespace.com/changes/self-service-oauth-credential-management
  page 200 direct 10775c https://developers.squarespace.com/commerce-apis/oauth
  page 200 direct 3897c https://developers.squarespace.com/mcp/overview
  page 200 direct 3342c https://developers.squarespace.com/quick-start
  page 200 direct 9185c https://developers.squarespace.com/commerce-apis/contacts-overview
  page 200 direct 10775c https://developers.squarespace.com/oauth
  page 404 direct 0c https://developers.squarespace.com/llms.txt ERR HTTP 404
  - auth_methods | Supports OAuth2 | https://developers.squarespace.com/commerce-apis/authentication-and-permissions
      “tion. Read the permission levels for each Commerce API below. Then, depending on your development needs, authenticate requests by using an API key or OAuth access token. Remember: Requests only have access to data for the website that owns the API key or OAuth”
  - auth_methods | Supports OAuth2 | https://developers.squarespace.com/changes/self-service-oauth-credential-management
      “Commerce APIs MCP Reseller APIs Templates Custom Code Upcoming Changes Changes Self-Service OAuth Credential ManagementStandalone pages DOM changesProductItem-additional deprecation Menu Copy page Changes Announcing Self-Service OAuth Credential M”
  - auth_methods | Supports API Key | https://developers.squarespace.com/commerce-apis/authentication-and-permissions
      “e, and location. Read the permission levels for each Commerce API below. Then, depending on your development needs, authenticate requests by using an API key or OAuth access token. Remember: Requests only have access to data for the website that owns the API k”
  - auth_methods | Supports API Key | https://developers.squarespace.com/commerce-apis/contacts-overview
      “s book based on the order's delivery address. Further reading Become familiar with common commerce terms and how they're related to the API Obtain an API key or use OAuth Read the FAQ guide for answers to common questions ContactsAnalytics On this page Contact”
  - api_type | REST API documented | https://developers.squarespace.com/commerce-apis/overview
      “site, like when an order was created, by configuring a webhook endpoint. Structure and design All Commerce APIs are built on HTTPS and designed with REST principles in mind. Every endpoint uses HTTPS features such as authentication, standard verbs, and standar”
  - api_type | REST API documented | https://developers.squarespace.com
      “base. Read the docsStart building What can you build on Squarespace? Integration, customization, or extension. Our docs can get you started, and the rest is up to you. 01 App creation Use our APIs to connect your business to Squarespace and reach more customer”
  - credential_access | Access signal: partner_gated | https://developers.squarespace.com/commerce-apis/oauth
      “Parameter isn't appended if user selects Allow. state Alphanumeric value; not present if user selects Deny. code Alphanumeric value used in step 4. Request access token. Value is initially URL-encoded and should be decoded prior to sending in the access token ”
  - credential_access | Access signal: partner_gated | https://developers.squarespace.com/oauth
      “Parameter isn't appended if user selects Allow. state Alphanumeric value; not present if user selects Deny. code Alphanumeric value used in step 4. Request access token. Value is initially URL-encoded and should be decoded prior to sending in the access token ”
  - mcp_available | MCP mentioned in vendor docs | https://developers.squarespace.com/commerce-apis/overview
      “Commerce APIs MCP Reseller APIs Templates Custom Code Upcoming Changes Getting Started OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site in”
  - mcp_available | MCP mentioned in vendor docs | https://developers.squarespace.com/commerce-apis/authentication-and-permissions
      “Commerce APIs MCP Reseller APIs Templates Custom Code Upcoming Changes Getting Started OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site in”
  - mcp_available | MCP registry entry: io.github.mrfentmen/squarespace-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=squarespace&limit=60
      “https://github.com/mrfentmen/awesome-mcps”
  - mcp_available | MCP registry entry: io.github.mrfentmen/squarespace-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=squarespace&limit=60
      “https://github.com/mrfentmen/premium-mcps”

## [47] Ecwid — Ecommerce
heuristic: auth=['OAuth2'] api=['REST'] access=Unclear mcp=Official verdict=Buildable with limitations llms_txt=True
  page 200 direct 2986c https://api-docs.ecwid.com/reference/overview
  page 200 direct 2986c https://api-docs.ecwid.com/docs/get-access-token
  page 200 direct 2986c https://api-docs.ecwid.com
  page 200 render 155c https://docs.ecwid.com/~gitbook/mcp
  page 200 direct 2471c https://docs.ecwid.com/api-reference
  page 200 direct 1949c https://docs.ecwid.com/launch-apps/public-apps-overview
  page 200 direct 1923c https://docs.ecwid.com/api-reference/advanced/js-api-calls
  page 200 direct 4262c https://docs.ecwid.com/storefronts/open-page-on-the-storefront/overview-of-open-page-options
  page 200 direct 2352c https://docs.ecwid.com/api-reference/rest-api/checkout-extra-fields
  page 200 direct 2986c https://api-docs.ecwid.com/llms.txt
  - auth_methods | Supports OAuth2 | https://docs.ecwid.com/api-reference
      “ST API REST API overview Ecwid REST API allows you to access and manage any store data, payment and shipping methods, and storefront settings. We use OAuth 2.0 authorization simplified for single-store customizations, JSON-formatted data, and a clear structure”
  - api_type | REST API documented | https://api-docs.ecwid.com/reference/overview
      “. Agents can also search and read this documentation through its MCP server.Skip to content ⌘Ctrlk AskContact API support More Build apps Site Themes REST API Reference Storefronts (JS API) Webhook automations Discounts Guides Changelog AI Assistant I'm here t”
  - api_type | REST API documented | https://api-docs.ecwid.com/docs/get-access-token
      “. Agents can also search and read this documentation through its MCP server.Skip to content ⌘Ctrlk AskContact API support More Build apps Site Themes REST API Reference Storefronts (JS API) Webhook automations Discounts Guides Changelog AI Assistant I'm here t”
  - mcp_available | MCP mentioned in vendor docs | https://api-docs.ecwid.com/reference/overview
      “Markdown versions of documentation pages are available by appending .md to page URLs. Agents can also search and read this documentation through its MCP server.Skip to content ⌘Ctrlk AskContact API support More Build apps Site Themes REST API Reference Storefr”
  - mcp_available | MCP mentioned in vendor docs | https://api-docs.ecwid.com/docs/get-access-token
      “Markdown versions of documentation pages are available by appending .md to page URLs. Agents can also search and read this documentation through its MCP server.Skip to content ⌘Ctrlk AskContact API support More Build apps Site Themes REST API Reference Storefr”
  - mcp_available | MCP registry entry: io.usefulapi/ecwid | https://registry.modelcontextprotocol.io/v0/servers?search=ecwid&limit=60
      “https://github.com/m190/usefulapi-mcp”
  - mcp_available | MCP registry entry: io.usefulapi/ecwid | https://registry.modelcontextprotocol.io/v0/servers?search=ecwid&limit=60
      “https://github.com/m190/usefulapi-mcp”
  - mcp_available | MCP registry entry: io.usefulapi/ecwid | https://registry.modelcontextprotocol.io/v0/servers?search=ecwid&limit=60
      “https://github.com/m190/usefulapi-mcp”

## [48] Gumroad — Ecommerce
heuristic: auth=['OAuth2'] api=['REST'] access=Self-serve (free trial / sandbox) mcp=Third-party/community verdict=Ready to build llms_txt=True
  page 200 render 142706c https://gumroad.com/api
  page 200 render 142746c https://app.gumroad.com/api
  page 200 direct 2298c https://app.gumroad.com/llms.txt
  page 200 direct 2298c https://gumroad.com/llms.txt
  - auth_methods | Supports OAuth2 | https://gumroad.com/api
      “endpoint below shows the matching gumroad invocation next to its cURL example. Run gumroad <command> --help for the full list of flags. The Gumroad OAuth API is based around REST. We return JSON for every request, including errors. To start using the API, you'”
  - auth_methods | Supports OAuth2 | https://app.gumroad.com/api
      “endpoint below shows the matching gumroad invocation next to its cURL example. Run gumroad <command> --help for the full list of flags. The Gumroad OAuth API is based around REST. We return JSON for every request, including errors. To start using the API, you'”
  - api_type | REST API documented | https://gumroad.com/api
      “matching gumroad invocation next to its cURL example. Run gumroad <command> --help for the full list of flags. The Gumroad OAuth API is based around REST. We return JSON for every request, including errors. To start using the API, you'll need to register your ”
  - api_type | REST API documented | https://app.gumroad.com/api
      “matching gumroad invocation next to its cURL example. Run gumroad <command> --help for the full list of flags. The Gumroad OAuth API is based around REST. We return JSON for every request, including errors. To start using the API, you'll need to register your ”
  - credential_access | Access signal: trial | https://gumroad.com/api
      “made for this subscription recurrence: subscription duration - monthly/quarterly/biannually/yearly/every_two_years free_trial_ends_at: timestamp when free trial ends, if free trial is enabled for the membership custom_fields: custom fields from the original pu”
  - credential_access | Access signal: trial | https://app.gumroad.com/api
      “made for this subscription recurrence: subscription duration - monthly/quarterly/biannually/yearly/every_two_years free_trial_ends_at: timestamp when free trial ends, if free trial is enabled for the membership custom_fields: custom fields from the original pu”
  - mcp_available | MCP registry entry: io.github.marstudio360/gumroad-dna-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=gumroad&limit=60
      “https://github.com/marstudio360/gumroad-dna-mcp”
  - mcp_available | MCP registry entry: io.github.marstudio360/gumroad-dna-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=gumroad&limit=60
      “https://github.com/marstudio360/gumroad-dna-mcp”
  - mcp_available | MCP registry entry: io.github.marstudio360/gumroad-dna-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=gumroad&limit=60
      “https://github.com/marstudio360/gumroad-dna-mcp”

## [49] Amazon Selling Partner — Ecommerce
heuristic: auth=['OAuth2'] api=['REST', 'GraphQL'] access=Self-serve (free trial / sandbox) mcp=None found verdict=Ready to build llms_txt=True
  page 200 direct 22562c https://developer-docs.amazon.com/sp-api/docs/welcome
  page 200 direct 23061c https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer
  page 200 direct 6100c https://developer-docs.amazon.com/sp-api
  page 200 direct 15250c https://developer-docs.amazon.com/sp-api/reference
  page 200 direct 23571c https://developer-docs.amazon.com/sp-api/docs/application-authorization-limits
  page 200 direct 215585c https://developer-docs.amazon.com/llms.txt
  - auth_methods | Supports OAuth2 | https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer
      “re self-authorized. Public seller and vendor applications: Applications that are publicly available and are authorized by sellers or by vendors using OAuth. In accordance with the Solution Provider Portal Agreement, public developers must list their app in the”
  - auth_methods | Supports OAuth2 | https://developer-docs.amazon.com/sp-api/docs/application-authorization-limits
      “r authorizations. Authorization limit summary There are two types of authorization: self-authorization (where you authorize your own application) and OAuth authorization (where other selling partners authorize your application). The following table summarizes ”
  - api_type | REST API documented | https://developer-docs.amazon.com/sp-api/docs/welcome
      “escription API references Interactive API references for all of the SP-APIs Models Index of all SP-API models with links to API references and GitHub Swagger models Deprecation schedule A list of all SP-API deprecation and removal dates, organized by API Annou”
  - api_type | REST API documented | https://developer-docs.amazon.com/sp-api
      “HubAPI StatusSupport Selling Partner API Welcome to Selling Partner API Documentation. Learn how to get started and build applications with Amazon's REST-based SP-API. Subscribe to updates via RSS feed. HomeDocumentationAPI ReferenceAnnouncementsModelsRelease ”
  - api_type | GraphQL API documented | https://developer-docs.amazon.com/sp-api/docs/welcome
      “sights for an ASIN Get Feedback Insights for a Browse Node Customer Feedback API Rate Limits Data Kiosk Data Kiosk API Request and filter data with a GraphQL query Verify that query processing is complete Data Kiosk Schema Explorer User Guide Data Kiosk Query ”
  - api_type | GraphQL API documented | https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer
      “sights for an ASIN Get Feedback Insights for a Browse Node Customer Feedback API Rate Limits Data Kiosk Data Kiosk API Request and filter data with a GraphQL query Verify that query processing is complete Data Kiosk Schema Explorer User Guide Data Kiosk Query ”
  - credential_access | Access signal: trial | https://developer-docs.amazon.com/sp-api/docs/welcome
      “l: Automate your SP-API calls using prebuilt PHP SDK Tutorial: Automate your SP-API calls using a prebuilt Python SDK Delete an Application From Your Developer Account Calling the SP-API Configuration Details SP-API Endpoints Date and Time Formatting Grantless”
  - credential_access | Access signal: trial | https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer
      “l: Automate your SP-API calls using prebuilt PHP SDK Tutorial: Automate your SP-API calls using a prebuilt Python SDK Delete an Application From Your Developer Account Calling the SP-API Configuration Details SP-API Endpoints Date and Time Formatting Grantless”

## [50] fanbasis — Ecommerce
heuristic: auth=[] api=[] access=Unclear mcp=None found verdict=Insufficient evidence llms_txt=True
  page 200 direct 6505c https://www.fanbasis.com/
  page 200 direct 6505c https://fanbasis.com
  page 200 direct 6505c https://www.fanbasis.com/llms.txt

## [51] DataForSEO — Data, SEO and Scraping
heuristic: auth=['Basic', 'Personal Access Token'] api=['REST'] access=Admin approval / app review mcp=Third-party/community verdict=Buildable with limitations llms_txt=False
  page 200 direct 13138c https://docs.dataforseo.com/v3/
  page 200 direct 13491c https://docs.dataforseo.com/v3/auth/
  page 200 direct 13138c https://docs.dataforseo.com
  page 200 direct 10326c https://docs.dataforseo.com/v3/ai_optimization/ai_keyword_data/overview/
  page 200 direct 12102c https://docs.dataforseo.com/v3/keywords_data/overview/
  page 200 direct 11893c https://docs.dataforseo.com/v3/keywords_data/google_ads/overview/
  page 200 direct 11728c https://docs.dataforseo.com/v3/keywords_data/bing/overview/
  page 200 direct 11454c https://docs.dataforseo.com/v3/keywords_data/google_trends/overview/
  page 200 direct 10690c https://docs.dataforseo.com/v3/keywords_data/clickstream_data/overview/
  page 404 direct 0c https://docs.dataforseo.com/llms.txt ERR HTTP 404
  - auth_methods | Supports Basic | https://docs.dataforseo.com/v3/auth/
      “ForSEO APIs. Note that the API password is generated automatically by DataForSEO and is different from your account password. DataForSEO is using the Basic Authentication, which makes it possible to call our APIs with almost any programming language, Postman a”
  - auth_methods | Supports Personal Access Token | https://docs.dataforseo.com/v3/auth/
      “with almost any programming language, Postman app, REST API platforms, and all major frameworks. Regardless of the programming language, your unique API token should be passed in the ‘Authorization’ header within the request in the following format: Authorizat”
  - api_type | REST API documented | https://docs.dataforseo.com/v3/
      “DataForSEO APIs. 1. Kickstart Guide to our APIs 2. Dashboard Guide 3. Test with API Playground 4. Free Unlimited Trial Info 5. Sandbox Best Practices REST technology DataForSEO API is using the REST technology for interchanging data between your application an”
  - api_type | REST API documented | https://docs.dataforseo.com/v3/auth/
      “t password. DataForSEO is using the Basic Authentication, which makes it possible to call our APIs with almost any programming language, Postman app, REST API platforms, and all major frameworks. Regardless of the programming language, your unique API token sh”
  - credential_access | Access signal: admin_approval | https://docs.dataforseo.com/v3/
      “k POST Tasks Ready Task GET Advanced HTML App List Task POST Tasks Ready Task GET Advanced HTML App Info Task POST Tasks Ready Task GET Advanced HTML App Reviews Task POST Tasks Ready Task GET App Listings Categories Search Apple Overview Categories Locations ”
  - credential_access | Access signal: admin_approval | https://docs.dataforseo.com/v3/auth/
      “k POST Tasks Ready Task GET Advanced HTML App List Task POST Tasks Ready Task GET Advanced HTML App Info Task POST Tasks Ready Task GET Advanced HTML App Reviews Task POST Tasks Ready Task GET App Listings Categories Search Apple Overview Categories Locations ”
  - credential_access | Access signal: free | https://docs.dataforseo.com/v3/auth/
      “ew AuthenticationHeaderValue("Basic", Convert.ToBase64String(Encoding.ASCII.GetBytes("login:password"))) } }; // do something } } } Create a free account with DataForSEO, then go to the API Access tab in the account dashboard to find your API login and passwor”
  - mcp_available | MCP registry entry: com.insightfulpipe/dataforseo | https://registry.modelcontextprotocol.io/v0/servers?search=dataforseo&limit=60
      “https://github.com/Insightful-Pipe/dataforseo-mcp-server”
  - mcp_available | MCP registry entry: io.scalably/dataforseo-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=dataforseo&limit=60
      “https://github.com/scalably-io/dataforseo-mcp”
  - mcp_available | MCP registry entry: io.scalably/dataforseo-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=dataforseo&limit=60
      “https://github.com/scalably-io/dataforseo-mcp”

## [52] SE Ranking — Data, SEO and Scraping
heuristic: auth=['API Key'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=False
  page 200 direct 21466c https://seranking.com/api.html
  page 404 direct 0c https://seranking.com/api ERR HTTP 404
  page 200 direct 13267c https://seranking.com/api/data/quickstarts/domain-keyword-opportunities/
  page 200 direct 18888c https://seranking.com/api/data/quickstarts/build-authority-with-link-building/
  page 200 direct 14362c https://seranking.com/ai-overviews-tracker.html
  page 200 direct 10019c https://seranking.com/api-pricing.html
  page 200 direct 10862c https://seranking.com/mcp.html
  page 200 direct 13172c https://seranking.com/api/rate-limits/
  page 404 direct 0c https://seranking.com/llms.txt ERR HTTP 404
  - auth_methods | Supports API Key | https://seranking.com/api.html
      “sing our API is straightforward. Just log in to your SE Ranking account, navigate to the API tab under the Settings section, and retrieve your unique API key. Once you have your API key, you can use it for different purposes. For more information, refer to our”
  - auth_methods | Supports API Key | https://seranking.com/api-pricing.html
      “ueries and AI agents; use the Project API for ongoing tracking of a fixed list of keywords or sites. Show more Show less Q How quickly can I get an API key after purchase? A Instantly. Your API key is issued immediately after payment. If you are on a free tria”
  - api_type | REST API documented | https://seranking.com/api.html
      “nt dashboards your clients and stakeholders can access directly. Connect to Data Studio Make Visual no-code automation to connect SE Ranking to the rest of your stack. Use Make’s visual interface to integrate SE Ranking with CRMs, project management tools, Sla”
  - credential_access | Access signal: partner_gated | https://seranking.com/api.html
      “ing Tool Agency Pack White Label Additional Services SEO API Free SEO tools SEO Task Manager Support & Partnership Contact Help Affiliate Educational Partnership Program column Company & Resources SEO Blog About Stand with Ukraine Careers What’s New Testimonia”
  - credential_access | Access signal: partner_gated | https://seranking.com/api/data/quickstarts/domain-keyword-opportunities/
      “ing Tool Agency Pack White Label Additional Services SEO API Free SEO tools SEO Task Manager Support & Partnership Contact Help Affiliate Educational Partnership Program column Company & Resources SEO Blog About Stand with Ukraine Careers What’s New Testimonia”
  - credential_access | Access signal: trial | https://seranking.com/api.html
      “king Grow your visibility with AI SEO SE Visible Analyze AI visibility strategically Planable Manage your socials as a team See product tour Start free trial en enEnglish deDeutsch frFrançais esEspañol nlNederlands itItaliano ptPortuguês uaУкраїнська ruРусский”
  - credential_access | Access signal: trial | https://seranking.com/api/data/quickstarts/domain-keyword-opportunities/
      “king Grow your visibility with AI SEO SE Visible Analyze AI visibility strategically Planable Manage your socials as a team See product tour Start free trial en enEnglish deDeutsch frFrançais esEspañol nlNederlands itItaliano ptPortuguês uaУкраїнська ruРусский”
  - credential_access | Access signal: free | https://seranking.com/api.html
      “custom integrations and bulk processes, or via MCP to query data from inside Claude or any AI assistant. Or do both. Start free trialSee product tour No credit card required The data your workflows will run on 5.5B Keywords database 100% Accurate keyword ranki”
  - credential_access | Access signal: free | https://seranking.com/api/data/quickstarts/domain-keyword-opportunities/
      “and with Ukraine Careers What’s New Testimonials Webinars Academy Competitors FAQ Legal & Technical Privacy Statement Cookie Policy Legal Information Open Source Attributions Download enEnglish enEnglish deDeutsch frFrançais esEspañol nlNederlands itItaliano p”
  - credential_access | Access signal: enterprise | https://seranking.com/api-pricing.html
      “ng subscription? Try API Add-on! Monthly Annually Save up to 20% Add-on Requires subscription Extend your existing SE Ranking Core, Growth, or Enterprise plan with an API add-on. MCP included For SE Ranking customers who need automation Access to Data API + Pr”
  - mcp_available | MCP mentioned in vendor docs | https://seranking.com/api.html
      “ustomer Hub Agency Catalog See product tour Blog Webinars Podcast Academy Help center What’s new Case studies Pricing Platform plans API Plans API & MCP API MCP Our data API Pricing See product tour API Keyword Research API Backlinks API Domain Analysis API Ra”
  - mcp_available | MCP mentioned in vendor docs | https://seranking.com/api/data/quickstarts/domain-keyword-opportunities/
      “ustomer Hub Agency Catalog See product tour Blog Webinars Podcast Academy Help center What’s new Case studies Pricing Platform plans API Plans API & MCP API MCP Our data API Pricing See product tour API Keyword Research API Backlinks API Domain Analysis API Ra”

## [53] Ahrefs — Data, SEO and Scraping
heuristic: auth=['OAuth2', 'API Key', 'Personal Access Token'] api=['REST'] access=Enterprise-only mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 3465c https://ahrefs.com/api
  page 200 direct 4890c https://docs.ahrefs.com/docs/api/reference/introduction
  page 200 direct 2105c https://docs.ahrefs.com/en/api/docs/api-keys-creation-and-management
  page 200 direct 3502c https://docs.ahrefs.com/en/ahrefs-connect/docs/oauth-guide
  page 200 direct 4890c https://docs.ahrefs.com/en/api/docs/introduction
  page 200 direct 3931c https://docs.ahrefs.com/en/mcp/docs/introduction
  page 200 direct 4795c https://docs.ahrefs.com/en/looker-studio/docs/introduction
  page 200 direct 2941c https://docs.ahrefs.com/en/bot-analytics/docs/introduction
  page 404 direct 0c https://ahrefs.com/llms.txt ERR HTTP 404
  page 200 direct 9871c https://docs.ahrefs.com/llms.txt
  - auth_methods | Supports OAuth2 | https://ahrefs.com/api
      “party apps through our integration program. Built on API v3. Introduction Overview of the integration program How it works Architecture and data flow OAuth guide Implement OAuth 2.0 authorization How to apply Steps to join the program Introduction Overview of ”
  - auth_methods | Supports OAuth2 | https://docs.ahrefs.com/en/ahrefs-connect/docs/oauth-guide
      “worksHow to applyOAuth guideAPI guideApproval processApps galleryTerms of service For Ahrefs UsersHow to manage your integrations For App Developers/OAuth guide OAuth guide All API calls require authorization and are made on behalf of an authorized Ahrefs user”
  - auth_methods | Supports API Key | https://ahrefs.com/api
      “, authentication, and rate limits Free test queries Try API endpoints without an Enterprise plan Explore endpoints Browse all available API endpoints API keys Create and manage your API keys Changelog Latest API updates and changes OpenAPI spec Full machine-re”
  - auth_methods | Supports API Key | https://docs.ahrefs.com/docs/api/reference/introduction
      “mentary test queries for all development and testing purposes to mitigate any unintended usage of API units. We also recommend putting limits on your API keys, especially when you are in the testing and development stage. Eligible paid plans include a monthly ”
  - auth_methods | Supports Personal Access Token | https://docs.ahrefs.com/en/bot-analytics/docs/introduction
      “project settings: Go to Project Settings → Bot Analytics for your project. Select an installation method. Either use automatic setup by providing an API token, follow the manual setup instructions, authorize the Ahrefs integration (Vercel), or configure the de”
  - api_type | REST API documented | https://ahrefs.com/api
      “200 OK Domain / DRRef. Domains 1wikipedia.org98 2github.com96 3medium.com94 4stackoverflow.com93 5producthunt.com91 Output for illustration purposes. REST API Research keywords, analyze backlinks, track rankings, and monitor brand visibility across traditional”
  - api_type | REST API documented | https://docs.ahrefs.com/docs/api/reference/introduction
      “ve the fields you don't need to reduce the cost of a request. For full usage details, view our API reference in these docs. The reference contains an OpenAPI-compatible specification of each endpoint's request and response format. Rate limiting Ahrefs API is l”
  - credential_access | Access signal: enterprise | https://ahrefs.com/api
      “ity across traditional search and AI platforms. Introduction Overview, authentication, and rate limits Free test queries Try API endpoints without an Enterprise plan Explore endpoints Browse all available API endpoints API keys Create and manage your API keys ”
  - credential_access | Access signal: enterprise | https://docs.ahrefs.com/en/mcp/docs/introduction
      “that an AI agent can access. Each plan also comes with a limited amount of monthly API units. The higher your plan tier, the more units are included. Enterprise customers can purchase additional unit add-ons if needed. When a third-party app makes an API call ”
  - credential_access | Access signal: paid_plan | https://docs.ahrefs.com/docs/api/reference/introduction
      “iption information: Your API limits and usage Public endpoints: Our crawler's IP addresses and ranges Eligibility Ahrefs API is available on eligible paid plans. On all other plans, you'll still have access to a limited set of free test queries. Plan limits Al”
  - credential_access | Access signal: paid_plan | https://docs.ahrefs.com/en/api/docs/introduction
      “iption information: Your API limits and usage Public endpoints: Our crawler's IP addresses and ranges Eligibility Ahrefs API is available on eligible paid plans. On all other plans, you'll still have access to a limited set of free test queries. Plan limits Al”
  - credential_access | Access signal: admin_approval | https://docs.ahrefs.com/en/mcp/docs/introduction
      “ed API key (tagged with MCP scope). New keys created through OAuth for MCP or Ahrefs Connect default to a monthly limit of 200,000 API units per key. Workspace admins can change or remove this limit in the API keys report. Manually created keys have no per-key”
  - mcp_available | MCP mentioned in vendor docs | https://ahrefs.com/api
      “ndpoints API keys Create and manage your API keys Changelog Latest API updates and changes OpenAPI spec Full machine-readable spec for every endpoint MCP Connect your Ahrefs data to AI assistants and agents to enhance their answers with real marketing insights”
  - mcp_available | MCP mentioned in vendor docs | https://docs.ahrefs.com/en/mcp/docs/introduction
      “ool Categories Setup GuidesClaude Desktop/WebClaude MobileClaude CodeCopilot StudioChatGPT WebLovablen8nManusMistral's Le ChatOpenClaw What is Ahrefs MCP Ahrefs MCP lets AI agents securely access the Ahrefs API and enrich their answers with real Ahrefs data. M”
  - mcp_available | MCP registry entry: com.ahrefs/mcp | https://registry.modelcontextprotocol.io/v0/servers?search=ahrefs&limit=60
      “”
  - mcp_available | MCP registry entry: com.jojapi/ahrefs | https://registry.modelcontextprotocol.io/v0/servers?search=ahrefs&limit=60
      “”
  - mcp_available | MCP registry entry: com.mcparmory/ahrefs | https://registry.modelcontextprotocol.io/v0/servers?search=ahrefs&limit=60
      “https://github.com/mcparmory/registry”

## [54] MrScraper — Data, SEO and Scraping
heuristic: auth=['API Key', 'Personal Access Token'] api=[] access=Enterprise-only mcp=Official verdict=Insufficient evidence llms_txt=True
  page 200 direct 5723c https://docs.mrscraper.com/
  page 200 direct 5723c https://docs.mrscraper.com
  page 200 direct 7424c https://docs.mrscraper.com/docs/getting-started/api-token
  page 200 direct 8969c https://docs.mrscraper.com/docs/residential-proxy/configuration/authentication
  page 200 direct 5723c https://docs.mrscraper.com/docs/getting-started/overview
  page 200 direct 16822c https://docs.mrscraper.com/docs/getting-started/quickstart
  page 200 direct 6807c https://docs.mrscraper.com/docs/getting-started/web-search
  page 200 direct 9200c https://docs.mrscraper.com/docs/getting-started/scraper-api
  page 200 direct 25668c https://docs.mrscraper.com/llms.txt
  - auth_methods | Supports API Key | https://docs.mrscraper.com/docs/getting-started/quickstart
      “s you how to make your first scraping request with MrScraper. Make Your First API Request Before You Start Create a MrScraper account and obtain your API key from the Scraper API before following this guide. In this quickstart, you'll scrape a Walmart product ”
  - auth_methods | Supports Personal Access Token | https://docs.mrscraper.com/
      “and sources. Scraper API Test API requests, explore features, and generate code without writing code. Token Plan Learn how tokens work and create an API token for authentication. CLI Retrieve pages, search the web, and check usage from your terminal. MCP Serve”
  - auth_methods | Supports Personal Access Token | https://docs.mrscraper.com
      “and sources. Scraper API Test API requests, explore features, and generate code without writing code. Token Plan Learn how tokens work and create an API token for authentication. CLI Retrieve pages, search the web, and check usage from your terminal. MCP Serve”
  - credential_access | Access signal: enterprise | https://docs.mrscraper.com/docs/residential-proxy/configuration/authentication
      “the sub-user in the table. Click the edit icon (pencil) next to the Bandwidth Limit value. Enter the new bandwidth amount (in MB). Note For user with Enterprise plan you can select Unlimited to pay as you go. Confirm the change. The updated allocation is refle”
  - mcp_available | MCP mentioned in vendor docs | https://docs.mrscraper.com/
      “Token Plan Learn how tokens work and create an API token for authentication. CLI Retrieve pages, search the web, and check usage from your terminal. MCP Server Connect AI clients to MrScraper for page retrieval, web search, and usage. Billing Understand subscr”
  - mcp_available | MCP mentioned in vendor docs | https://docs.mrscraper.com
      “Token Plan Learn how tokens work and create an API token for authentication. CLI Retrieve pages, search the web, and check usage from your terminal. MCP Server Connect AI clients to MrScraper for page retrieval, web search, and usage. Billing Understand subscr”
  - mcp_available | MCP registry entry: io.github.mrscraper-com/mrscraper-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=mrscraper&limit=60
      “https://github.com/mrscraper-com/mrscraper-mcp”
  - mcp_available | MCP registry entry: io.github.mrscraper-com/mrscraper-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=mrscraper&limit=60
      “https://github.com/mrscraper-com/mrscraper-mcp”
  - mcp_available | MCP registry entry: io.github.mrscraper-com/mrscraper-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=mrscraper&limit=60
      “https://github.com/mrscraper-com/mrscraper-mcp”

## [55] Apify — Data, SEO and Scraping
heuristic: auth=['API Key', 'Personal Access Token'] api=['REST'] access=Self-serve (free) mcp=Official verdict=Ready to build llms_txt=True
  page 200 direct 30384c https://docs.apify.com/api/v2
  page 200 direct 15730c https://docs.apify.com/platform/integrations/api
  page 200 direct 26937c https://docs.apify.com
  page 200 direct 26937c https://docs.apify.com/llms.txt
  - auth_methods | Supports API Key | https://docs.apify.com/api/v2
      “rs.md) - [Datasets](https://docs.apify.com/api/v2/actor-runtime-api-datasets.md) - [Key-value stores](https://docs.apify.com/api/v2/actor-runtime-api-key-value-stores.md) - [Request queues](https://docs.apify.com/api/v2/actor-runtime-api-request-queues.md) - [”
  - auth_methods | Supports Personal Access Token | https://docs.apify.com/api/v2
      “ET` requests. For example, to call a `POST` endpoint, append `?method=POST` to the URL of your `GET` request. ## Authentication **You can create an API token on the [Integrations](https://console.apify.com/settings/integrations) page in the Apify Console.** Th”
  - auth_methods | Supports Personal Access Token | https://docs.apify.com/platform/integrations/api
      “- the REST API works with any HTTP client - but the official API clients implement best practices such as exponential backoff and rate limiting. ## API token To access the Apify API in your integrations, you need to authenticate using your secret API token. Yo”
  - api_type | REST API documented | https://docs.apify.com/api/v2
      “: https://docs.apify.com/llms.txt > Use this file to discover all available pages before exploring further. Version: v2-2026-11-18T151559Z Download OpenAPI * [YAML](https://docs.apify.com/api/openapi.yaml) * [JSON](https://docs.apify.com/api/openapi.json) # Ap”
  - api_type | REST API documented | https://docs.apify.com/platform/integrations/api
      “Use this file to discover all available pages before exploring further. # API integration All aspects of the Apify platform can be controlled via a REST API, which is described in detail in the [API Reference](https://docs.apify.com/api/v2.md). If you want to ”
  - credential_access | Access signal: free | https://docs.apify.com
      “ability disclosure policy](https://docs.apify.com/security/vulnerability-disclosure.md): Apify's vulnerability disclosure policy for the platform and open-source projects, including scope, testing guidelines, safe harbor, and how to report one. ## storage - [S”
  - mcp_available | MCP mentioned in vendor docs | https://docs.apify.com
      “etize them in Apify Store. ## agents - [Connect your AI agent to Apify](https://docs.apify.com/agents.md): Connect an AI agent to Apify through the MCP server, a plugin, or Agent Skills, then pick the setup guide for Claude Code, Codex, Cursor, and more. - [Le”
  - mcp_available | MCP registry entry: ai.xomia/xomiadata-apify-actors | https://registry.modelcontextprotocol.io/v0/servers?search=apify&limit=60
      “”
  - mcp_available | MCP registry entry: com.apify/apify-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=apify&limit=60
      “https://github.com/apify/apify-mcp-server”
  - mcp_available | MCP registry entry: com.apify/apify-mcp-server | https://registry.modelcontextprotocol.io/v0/servers?search=apify&limit=60
      “https://github.com/apify/apify-mcp-server”

## [56] Firecrawl — Data, SEO and Scraping
heuristic: auth=['OAuth2', 'API Key', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 176711c https://docs.firecrawl.dev/introduction
  page 200 direct 80686c https://docs.firecrawl.dev/mcp-server
  page 200 direct 22458c https://firecrawl.dev
  page 200 direct 849c https://www.firecrawl.dev/app/api-keys
  page 200 direct 10928c https://www.firecrawl.dev/auth.md
  page 200 direct 47976c https://docs.firecrawl.dev/sdks/overview
  page 200 direct 71704c https://docs.firecrawl.dev/api-reference/v2-introduction
  page 200 direct 77524c https://docs.firecrawl.dev/quickstarts/claude-code
  page 200 direct 77707c https://docs.firecrawl.dev/quickstarts/claude-desktop
  page 200 direct 4106c https://docs.firecrawl.dev/llms.txt
  - auth_methods | Supports OAuth2 | https://docs.firecrawl.dev/introduction
      “pied=false}document.body.removeChild(textarea);return copied}};const isHuman=variant===`human`;const mcpUrl=isHuman?`https://mcp.firecrawl.dev/v2/mcp-oauth`:`https://mcp.firecrawl.dev/v2/mcp`;const cursorInstallUrl=`cursor://anysphere.cursor-deeplink/mcp/insta”
  - auth_methods | Supports OAuth2 | https://docs.firecrawl.dev/mcp-server
      “e Claude Desktop guide to connect once under the server name firecrawl. Setting up Grok Bot? See the Grok Bot guide. Sign in Point your client at the OAuth server URL. Your client opens a browser window where you sign in to Firecrawl and approve a team: { "mcp”
  - auth_methods | Supports API Key | https://docs.firecrawl.dev/introduction
      “nteract with the live web to get clean Markdown or structured data. Get started Build directly with the API Scrape your first page now. No account or API key is required for this request. cURL # No API key needed to get started — add -H "Authorization: Bearer ”
  - auth_methods | Supports API Key | https://docs.firecrawl.dev/mcp-server
      “ting On this pageBack to top Sign in Client setup MCP Get Started Copy pageCopy page Set up Firecrawl MCP with keyless access, account sign-in, or an API key. Copy pageCopy page Choose how the connection will authenticate. Signing in and adding an API key are ”
  - auth_methods | Supports Other | https://docs.firecrawl.dev/introduction
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - auth_methods | Supports Other | https://docs.firecrawl.dev/mcp-server
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - api_type | REST API documented | https://firecrawl.dev
      “are available? Firecrawl has official SDKs for Python, Node.js, Go, Rust, Java, and Elixir, plus a CLI for terminal workflows. You can also call the REST API directly from any language. All SDKs support search, scrape, interact, and crawl. Where can I find my ”
  - api_type | REST API documented | https://docs.firecrawl.dev/api-reference/v2-introduction
      “e, what causes it, how to remedy it, and whether to retry.","href":"/api-reference/errors"}]},{"group":"Search Endpoints","pages":[{"title":"Search","openapi":"api-reference/v2-openapi.json POST /search","href":"/api-reference/endpoint/search"},{"title":"Searc”
  - credential_access | Access signal: enterprise | https://docs.firecrawl.dev/introduction
      “including eligibility, expiration, and plan limits","href":"/partner-credits"}]},{"group":"Enterprise","pages":[{"title":"Enterprise","description":"Enterprise plans, security, and features for Firecrawl at scale","href":"/enterprise"},{"title":"Security overv”
  - credential_access | Access signal: enterprise | https://docs.firecrawl.dev/mcp-server
      “including eligibility, expiration, and plan limits","href":"/partner-credits"}]},{"group":"Enterprise","pages":[{"title":"Enterprise","description":"Enterprise plans, security, and features for Firecrawl at scale","href":"/enterprise"},{"title":"Security overv”
  - credential_access | Access signal: free | https://docs.firecrawl.dev/introduction
      “pes Security Testing Use Cases Overview AI Platforms Lead Enrichment SEO Platforms Deep Research View more Other Overview Debug with Ask Contributing Open Source vs Cloud Contributor Setup Self-hosting On this pageBack to top Get started Build directly with th”
  - credential_access | Access signal: free | https://docs.firecrawl.dev/mcp-server
      “pes Security Testing Use Cases Overview AI Platforms Lead Enrichment SEO Platforms Deep Research View more Other Overview Debug with Ask Contributing Open Source vs Cloud Contributor Setup Self-hosting On this pageBack to top Sign in Client setup MCP Get Start”
  - credential_access | Access signal: partner_gated | https://firecrawl.dev
      “Marketplace, so the charges go on your AWS or Google Cloud bill. On Google Cloud, a private offer also draws down your Google Cloud spend commitment. Contact sales for a private offer with custom pricing and terms. Why am I being charged VAT (or any local tax)”
  - credential_access | Access signal: paid_plan | https://firecrawl.dev
      “tool from Apify to Firecrawl because it benchmarked 50x faster with AgentOps." Pranav Pai Vernekar@ppv999"Finally upgraded my plan of @firecrawl to a paid plan. Totally worth it. One of the best products for your AI workflows." Tom - Morpho@TomReppelin"I found”
  - mcp_available | MCP mentioned in vendor docs | https://docs.firecrawl.dev/introduction
      “ayground Blog Community Changelog Get Started Introduction ChatGPT & Codex Claude & Claude Code Claude Desktop & Cowork Cursor Grok Bot Factory Droid MCP CLI Firecrawl Local Advanced Scraping Guide Plans and Billing Enterprise Core Endpoints Alexandria Search ”
  - mcp_available | MCP mentioned in vendor docs | https://docs.firecrawl.dev/mcp-server
      “ip to main content Firecrawl Docs home page v2English Search...⌘K Status Support Sign Up firecrawl/firecrawl firecrawl/firecrawl Search... Navigation MCP Get Started Documentation SDKs API Reference Build with AI Playground Blog Community Changelog Get Started”
  - mcp_available | MCP registry entry: co.civai.nova/mcp-firecrawl | https://registry.modelcontextprotocol.io/v0/servers?search=firecrawl&limit=60
      “”
  - mcp_available | MCP registry entry: com.mcparmory/firecrawl | https://registry.modelcontextprotocol.io/v0/servers?search=firecrawl&limit=60
      “https://github.com/mcparmory/registry”
  - mcp_available | MCP registry entry: com.mcparmory/firecrawl | https://registry.modelcontextprotocol.io/v0/servers?search=firecrawl&limit=60
      “https://github.com/mcparmory/registry”

## [57] Bright Data — Data, SEO and Scraping
heuristic: auth=['API Key', 'Personal Access Token', 'Other'] api=['REST'] access=Partnership / contact-sales gated mcp=Official verdict=Requires outreach / partnership llms_txt=True
  page 200 direct 136301c https://docs.brightdata.com/api-reference/introduction
  page 200 direct 66733c https://docs.brightdata.com/mcp-server/overview
  page 200 direct 13480c https://brightdata.com
  page 200 direct 136301c https://docs.brightdata.com/api-reference/authentication
  page 200 direct 101734c https://docs.brightdata.com/introduction
  page 200 direct 47180c https://docs.brightdata.com/integrations/introduction
  page 200 direct 39695c https://docs.brightdata.com/general/account/overview
  page 200 direct 103093c https://docs.brightdata.com/api-reference/terminology
  page 200 direct 308074c https://docs.brightdata.com/api-reference/SDK
  page 200 direct 17161c https://docs.brightdata.com/llms.txt
  - auth_methods | Supports API Key | https://docs.brightdata.com/api-reference/introduction
      “I Media Data API Proxy Proxy Networks Proxy Manager API Administrative APIs Account Management API On this pageBack to top How do I authenticate with API Key? How do I relay the API key within a request? How do I authenticate with the CLI, Python SDK and JavaS”
  - auth_methods | Supports API Key | https://docs.brightdata.com/mcp-server/overview
      “g?fit=max\u0026auto=format\u0026n=5sJgYq9iW-Vo_7rr\u0026q=85\u0026s=1b96b56f36033019c22871f4799240b0","api":{"mdx":{"auth":{"method":"bearer","name":"API_KEY"}}},"navbar":{"links":[{"href":"https://help.brightdata.com/hc/en-us/requests/new","label":"Support"}]”
  - auth_methods | Supports Personal Access Token | https://docs.brightdata.com/introduction
      “sse?token=YOUR_API_KEY" { "mcpServers": { "brightdata-mcp": { "command": "npx", "args": ["-y", "@brightdata/mcp"], "env": { "API_TOKEN": "<your API token>" } } } } codex mcp add brightdata --env API_TOKEN=YOUR_API_KEY -- npx -y @brightdata/mcp npx -p @brightda”
  - auth_methods | Supports Other | https://docs.brightdata.com/api-reference/introduction
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - auth_methods | Supports Other | https://docs.brightdata.com/mcp-server/overview
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - api_type | REST API documented | https://docs.brightdata.com/api-reference/introduction
      “-JS"}]},{"group":"Data extraction","pages":[{"group":"Scraper API","pages":[{"title":"Scraper async requests","sidebarTitle":"Asynchronous requests","openapi":"api-reference/rest-api/scraper/scraper-rest-api.json POST /datasets/v3/trigger","href":"/api-referen”
  - api_type | REST API documented | https://docs.brightdata.com/mcp-server/overview
      “/products/scrapers/limits"},{"title":"Scraper API reference","sidebarTitle":"API reference","icon":"arrow-up-right-from-square","url":"/api-reference/rest-api/scraper/asynchronous-requests","href":"/products/scrapers/scrapers-library/api-reference"}]},{"group"”
  - credential_access | Access signal: free | https://docs.brightdata.com/api-reference/introduction
      “export","openapi":"api-reference/openapi POST /costs/export/json","href":"/api-reference/account-management-api/Export_cost_breakdown"},{"title":"Get free tier credits","sidebarTitle":"Free tier credits","openapi":"api-reference/openapi GET /trials/free_tier",”
  - credential_access | Access signal: free | https://docs.brightdata.com/mcp-server/overview
      “new account includes 5,000 free requests per month. You can run the server two ways: a fully managed remote server, or a self-hosted local instance. Get started for free Start using the Bright Data MCP server with 5,000 requests per month, completely free. Sig”
  - credential_access | Access signal: partner_gated | https://brightdata.com
      “3/IP Resources Tools Integrations Browser Extension Network Status Learning Hub Blog Case Studies Webinars Proxy Locations Masterclass Videos Company Partner Program Trust Center Bright SDK Bright Initiative Docs Log in User Dashboard Contact sales Start free ”
  - credential_access | Access signal: trial | https://brightdata.com
      “Accessibility Menu skip to content en English Español Deutsch Français 日本語 Português 简体中文 한국어 Start free trial User Dashboard Products Web Access APIs Unlocker APISay goodbye to blocks and CAPTCHAs SERP APIGet multi-engine search results on-demand Google Bi”
  - credential_access | Access signal: trial | https://docs.brightdata.com/general/account/overview
      “ial restrictions","pages":[{"title":"Free tier","sidebarTitle":"Free tier","href":"/general/account/billing-and-pricing/free-tier"},{"title":"Limited trial account restrictions","icon":"shield-exclamation","href":"/general/account/limited-trial-restrictions"}]”
  - mcp_available | MCP mentioned in vendor docs | https://docs.brightdata.com/api-reference/introduction
      “gs and configuration? You can view and manage your API Keys in Account settings. What are Agent API keys? Agent API keys authenticate the Bright Data MCP server and AI agents. Bright Data lists them in a separate Agent API keys table in Account settings, under”
  - mcp_available | MCP mentioned in vendor docs | https://docs.brightdata.com/mcp-server/overview
      “efore exploring further. Skip to main content Bright Data Docs home page English Search...⌘K Support Sign up Sign up Search... Navigation Bright Data MCP MCP server overview Documentation API reference Integrations Account Management Get started Introduction Q”
  - mcp_available | MCP registry entry: ai.smithery/luminati-io-brightdata-mcp | https://registry.modelcontextprotocol.io/v0/servers?search=bright&limit=60
      “https://github.com/brightdata/brightdata-mcp-sse”
  - mcp_available | MCP registry entry: co.brightkey/education-data | https://registry.modelcontextprotocol.io/v0/servers?search=bright&limit=60
      “”
  - mcp_available | MCP registry entry: co.brightkey/education-data | https://registry.modelcontextprotocol.io/v0/servers?search=bright&limit=60
      “”

## [58] Sherlock — Data, SEO and Scraping
heuristic: auth=[] api=[] access=Unclear mcp=Third-party/community verdict=Insufficient evidence llms_txt=True
  page 200 direct 6914c https://github.com/sherlock-project/sherlock
  page 200 direct 28650c https://github.com/llms.txt
  - mcp_available | MCP registry entry: com.hostsherlock/mcp | https://registry.modelcontextprotocol.io/v0/servers?search=sherlock&limit=60
      “”
  - mcp_available | MCP registry entry: com.hostsherlock/mcp | https://registry.modelcontextprotocol.io/v0/servers?search=sherlock&limit=60
      “”
  - mcp_available | MCP registry entry: com.hostsherlock/mcp | https://registry.modelcontextprotocol.io/v0/servers?search=sherlock&limit=60
      “https://github.com/Emailsherlock1/hostsherlock-mcp”

## [59] Waterfall.io — Data, SEO and Scraping
heuristic: auth=['API Key', 'Other'] api=['REST'] access=Unclear mcp=Official verdict=Buildable with limitations llms_txt=True
  page 200 direct 8401c https://waterfall.io/
  page 200 direct 8401c https://waterfall.io
  page 200 direct 44210c https://docs.waterfall.io/v1/introduction
  page 200 direct 4617c https://waterfall.io/llms.txt
  - auth_methods | Supports API Key | https://waterfall.io/
      “ing and outreach Preview curl --location 'https://api.waterfall.io/v1/prospector' \ --header 'Content-Type: application/json' \ --header 'x-waterfall-api-key: YOURKEY' \ --data '{ "domain": "stripe.com", "title_filter": "(marketing director)", "verified_only":”
  - auth_methods | Supports API Key | https://waterfall.io
      “ing and outreach Preview curl --location 'https://api.waterfall.io/v1/prospector' \ --header 'Content-Type: application/json' \ --header 'x-waterfall-api-key: YOURKEY' \ --data '{ "domain": "stripe.com", "title_filter": "(marketing director)", "verified_only":”
  - auth_methods | Supports Other | https://docs.waterfall.io/v1/introduction
      “:"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature_enabled":true},"impressionData":fals”
  - api_type | REST API documented | https://docs.waterfall.io/v1/introduction
      “rfall/PF-aiLCRZlfb8d2k/images/Favicon.png?fit=max\u0026auto=format\u0026n=PF-aiLCRZlfb8d2k\u0026q=85\u0026s=71cc616c96f9b07780b577a1b43acfbe","api":{"openapi":"api_specs.yaml"},"navbar":{"links":[{"href":"https://www.waterfall.io","label":"Waterfall.io"},{"hre”
  - mcp_available | MCP mentioned in vendor docs | https://docs.waterfall.io/v1/introduction
      “seo":{"indexing":"navigable"},"integrations":{"gtm":{"tagId":"GTM-PKXXGFQZ"}},"contextual":{"options":["copy","view","chatgpt","claude","perplexity","mcp","cursor","vscode"],"display":"header"},"styling":{"latex":false},"navigation":{"pages":[]}},"deployment":”
  - mcp_available | MCP registry entry: com.mambabuilt/mcp-email-waterfall-orchestrator | https://registry.modelcontextprotocol.io/v0/servers?search=waterfall&limit=60
      “https://github.com/mambalabsdev/mcp-email-waterfall-orchestrator”
  - mcp_available | MCP registry entry: com.mambabuilt/mcp-email-waterfall-orchestrator | https://registry.modelcontextprotocol.io/v0/servers?search=waterfall&limit=60
      “https://github.com/mambalabsdev/mcp-email-waterfall-orchestrator”
  - mcp_available | MCP registry entry: com.mambabuilt/mcp-email-waterfall-orchestrator | https://registry.modelcontextprotocol.io/v0/servers?search=waterfall&limit=60
      “https://github.com/mambalabsdev/mcp-email-waterfall-orchestrator”

## [60] Clay — Data, SEO and Scraping
heuristic: auth=['API Key', 'Other'] api=[] access=Partnership / contact-sales gated mcp=Official verdict=Insufficient evidence llms_txt=False
  page 200 direct 12531c https://www.clay.com/
  page 200 direct 24352c https://university.clay.com/docs/http-api-integration-overview
  page 200 direct 12531c https://clay.com
  page 200 direct 27084c https://www.clay.com/pricing
  page 200 direct 8389c https://www.clay.com/mcp
  page 200 direct 9493c https://university.clay.com/
  page 200 direct 8757c https://university.clay.com/docs-topics/getting-started
  page 200 direct 12489c https://university.clay.com/docs/clay-mcp-in-chatgpt
  page 404 direct 0c https://university.clay.com/llms.txt ERR HTTP 404
  page 404 direct 0c https://www.clay.com/llms.txt ERR HTTP 404
  - auth_methods | Supports API Key | https://university.clay.com/docs/http-api-integration-overview
      “enrichment. Need to pull a list from an external API? → Use as source. Storing authentication credentials at the workspace level Instead of entering API keys or bearer tokens manually in the Headers field each time, you can save your auth credentials in an HTT”
  - auth_methods | Supports API Key | https://www.clay.com/pricing
      “Enrich with Claygent Claygent is Clay's AI agent with access to web research. You can generate any custom data points using Claygent. Bring your own API key Start 14-day trial or buy now Launch For small teams building and automating prospecting workflows $167”
  - auth_methods | Supports Other | https://university.clay.com/docs/http-api-integration-overview
      “uth will return an error (e.g., access denied) if no account is selected and no headers are passed manually. If you're connecting to an API that uses JWT authentication (dynamically issued tokens), use the HTTP API with JWT Authentication action instead, which”
  - auth_methods | Supports Other | https://university.clay.com/docs-topics/getting-started
      “ing overview Write personalized message sequences with AI, conditionals and more. View article View articleView article Getting started HTTP API with JWT authentication Use HTTP API connections authenticated securely with JWT tokens. View article View articleV”
  - credential_access | Access signal: partner_gated | https://www.clay.com/
      “Link long form description will go in this slot here. GTM Engineer job board Link long form description will go in this slot here. Partner with Clay Become a partner Link long form description will go in this slot here. Solution partners Link long form descrip”
  - credential_access | Access signal: partner_gated | https://clay.com
      “Link long form description will go in this slot here. GTM Engineer job board Link long form description will go in this slot here. Partner with Clay Become a partner Link long form description will go in this slot here. Solution partners Link long form descrip”
  - credential_access | Access signal: trial | https://www.clay.com/
      “load brand assetsDownloaded! Back Product Product Solutions Solutions Resources Resources Company Company Pricing Pricing ⌘ K Log in Get a demo Start free trial Product Product Solutions Solutions Resources Resources Company Company Pricing Pricing Log in Star”
  - credential_access | Access signal: trial | https://clay.com
      “load brand assetsDownloaded! Back Product Product Solutions Solutions Resources Resources Company Company Pricing Pricing ⌘ K Log in Get a demo Start free trial Product Product Solutions Solutions Resources Resources Company Company Pricing Pricing Log in Star”
  - credential_access | Access signal: free | https://www.clay.com/
      “pen roles Blog How to hire a go-to-market engineer for the agentic GTM era Read story Turn your growth ideas into reality today Start for free today. No credit card required. Start free trial Get a demo Use cases Automated inbound Account research ABM PLG assi”
  - credential_access | Access signal: free | https://clay.com
      “pen roles Blog How to hire a go-to-market engineer for the agentic GTM era Read story Turn your growth ideas into reality today Start for free today. No credit card required. Start free trial Get a demo Use cases Automated inbound Account research ABM PLG assi”
  - credential_access | Access signal: enterprise | https://www.clay.com/pricing
      “Launch and Growth plans, unused credits can accumulate up to 2x your monthly credit amount (e.g., a 10,000 credit plan can bank up to 20,000 total). Enterprise customers can roll over up to 15% of their prior year's purchased credits, provided they renew at an”
  - credential_access | Access signal: enterprise | https://university.clay.com/docs/clay-mcp-in-chatgpt
      “ogic, ask for a workflow instead. Listing tables and reading rows need a paid or trial plan. Queries that combine several tables need API table sync, available on Enterprise plans. "Show me the first 20 rows of our Inbound Leads table." Sequencer Build and edi”
  - credential_access | Access signal: admin_approval | https://university.clay.com/docs/clay-mcp-in-chatgpt
      “ChatGPT workspace. Clay shows No workspaces available, or your workspace isn't in the list: you need Editor or Admin access in that workspace. Ask a workspace admin to change your role. You connected the wrong workspace: disconnect Clay in ChatGPT's settings, ”
  - credential_access | Access signal: paid_plan | https://university.clay.com/docs/clay-mcp-in-chatgpt
      “ts for changes such as job changes, new hires, and funding news. You can also edit, pause, resume, or delete a signal. Signals are available on every paid plan except Flex, and during a trial. "Watch our target accounts for funding news." Plan availability and”
  - mcp_available | MCP mentioned in vendor docs | https://www.clay.com/
      “n this slot here. Activation Ads Sync targeted ad audiences to Linkedin, Meta, and Google Sequencer Use Clay's native sequencer or automate messaging MCP for reps Track job changes promotions or other signals New: Clay’s global agent Build GTM plays for long-r”
  - mcp_available | MCP mentioned in vendor docs | https://university.clay.com/docs/http-api-integration-overview
      “. Using HTTP API enrichment on an existing list instead of as a source. Table of contents TOC Heading TOC Heading Plan Explore other docs Gen AI Clay MCP in ChatGPT Connect the Clay MCP to ChatGPT, sign in to your workspace, and see what you can build and run ”
  - mcp_available | MCP registry entry: app.clayware/clayware | https://registry.modelcontextprotocol.io/v0/servers?search=clay&limit=60
      “https://github.com/noajp/clayware”
  - mcp_available | MCP registry entry: app.clayware/clayware | https://registry.modelcontextprotocol.io/v0/servers?search=clay&limit=60
      “https://github.com/noajp/clayware”
  - mcp_available | MCP registry entry: com.mambabuilt/mcp-clay-to-instantly-smartlead-push | https://registry.modelcontextprotocol.io/v0/servers?search=clay&limit=60
      “https://github.com/mambalabsdev/mcp-clay-to-instantly-smartlead-push”