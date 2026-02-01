# n8n Nodes Master List

## Overview

This reference document provides a comprehensive list of n8n nodes organized by category. Use this to identify the best nodes for building automation workflows.

**Usage:** Feed this to an AI agent to help build custom n8n flows, research nodes for specific use cases, or perform quick lookups.

---

## Core Nodes

Core nodes handle fundamental workflow operations like triggers, data transformation, and flow control.

| Node | Description | Documentation |
|------|-------------|---------------|
| Activation Trigger | Triggers workflow on activation | [Docs](https://n8n.io/integrations/activation-trigger) |
| Aggregate | Combines multiple items into groups | [Docs](https://n8n.io/integrations/aggregate) |
| Code | Execute custom JavaScript or Python | [Docs](https://n8n.io/integrations/code) |
| Compare Datasets | Compare two datasets | [Docs](https://n8n.io/integrations/compare-datasets) |
| Crypto | Encrypt and hash data | [Docs](https://n8n.io/integrations/crypto) |
| Date & Time | Parse and manipulate dates | [Docs](https://n8n.io/integrations/date-and-time) |
| Edit Fields | Set, rename, or remove fields | [Docs](https://n8n.io/integrations/edit-fields) |
| Execute Command | Run shell commands | [Docs](https://n8n.io/integrations/execute-command) |
| Execute Workflow | Run another workflow | [Docs](https://n8n.io/integrations/execute-workflow) |
| Filter | Filter items based on conditions | [Docs](https://n8n.io/integrations/filter) |
| Function | Run custom JavaScript code | [Docs](https://n8n.io/integrations/function) |
| HTML | Parse and extract HTML data | [Docs](https://n8n.io/integrations/html) |
| HTTP Request | Make HTTP API calls | [Docs](https://n8n.io/integrations/http-request) |
| If | Conditional branching | [Docs](https://n8n.io/integrations/if) |
| Item Lists | Work with lists of items | [Docs](https://n8n.io/integrations/item-lists) |
| Loop Over Items | Iterate through items | [Docs](https://n8n.io/integrations/loop-over-items) |
| Manual Trigger | Start workflow manually | [Docs](https://n8n.io/integrations/manual-trigger) |
| Markdown | Convert HTML to Markdown | [Docs](https://n8n.io/integrations/markdown) |
| Merge | Combine data from multiple branches | [Docs](https://n8n.io/integrations/merge) |
| Move Binary Data | Move binary data between fields | [Docs](https://n8n.io/integrations/move-binary-data) |
| No Operation | Placeholder node | [Docs](https://n8n.io/integrations/no-operation) |
| Read Binary Files | Read files from disk | [Docs](https://n8n.io/integrations/read-binary-files) |
| Rename Keys | Rename object keys | [Docs](https://n8n.io/integrations/rename-keys) |
| RSS Feed Read | Read RSS feeds | [Docs](https://n8n.io/integrations/rss-feed-read) |
| Schedule Trigger | Run workflow on schedule | [Docs](https://n8n.io/integrations/schedule-trigger) |
| Set | Set field values | [Docs](https://n8n.io/integrations/set) |
| Sort | Sort items | [Docs](https://n8n.io/integrations/sort) |
| Split In Batches | Process items in batches | [Docs](https://n8n.io/integrations/split-in-batches) |
| Split Out | Split arrays into items | [Docs](https://n8n.io/integrations/split-out) |
| SSH | Execute SSH commands | [Docs](https://n8n.io/integrations/ssh) |
| Stop And Error | Stop workflow with error | [Docs](https://n8n.io/integrations/stop-and-error) |
| Summarize | Aggregate and summarize data | [Docs](https://n8n.io/integrations/summarize) |
| Switch | Route items to different branches | [Docs](https://n8n.io/integrations/switch) |
| Wait | Pause workflow execution | [Docs](https://n8n.io/integrations/wait) |
| Webhook | Receive HTTP webhooks | [Docs](https://n8n.io/integrations/webhook) |
| Write Binary File | Write files to disk | [Docs](https://n8n.io/integrations/write-binary-file) |
| XML | Parse and create XML | [Docs](https://n8n.io/integrations/xml) |

---

## AI & Language Models

Nodes for AI, machine learning, and language model integrations.

| Node | Description | Documentation |
|------|-------------|---------------|
| AI Agent | Create AI agents with tools | [Docs](https://n8n.io/integrations/ai-agent) |
| AI Transform | Transform data using AI | [Docs](https://n8n.io/integrations/ai-transform) |
| Anthropic | Claude AI models | [Docs](https://n8n.io/integrations/anthropic) |
| AWS Bedrock Chat Model | AWS Bedrock LLMs | [Docs](https://n8n.io/integrations/aws-bedrock-chat-model) |
| AWS Comprehend | NLP text analysis | [Docs](https://n8n.io/integrations/aws-comprehend) |
| Azure OpenAI Chat Model | Azure-hosted OpenAI | [Docs](https://n8n.io/integrations/azure-openai-chat-model) |
| Cohere | Cohere language models | [Docs](https://n8n.io/integrations/cohere) |
| Google AI | Google AI models | [Docs](https://n8n.io/integrations/google-ai) |
| Google Gemini Chat Model | Google Gemini | [Docs](https://n8n.io/integrations/google-gemini-chat-model) |
| Google Vertex AI | Google Vertex AI | [Docs](https://n8n.io/integrations/google-vertex-ai) |
| Groq Chat Model | Groq fast inference | [Docs](https://n8n.io/integrations/groq-chat-model) |
| Hugging Face | Hugging Face models | [Docs](https://n8n.io/integrations/hugging-face) |
| Mistral Cloud Chat Model | Mistral AI | [Docs](https://n8n.io/integrations/mistral-cloud-chat-model) |
| Ollama Chat Model | Local Ollama models | [Docs](https://n8n.io/integrations/ollama-chat-model) |
| OpenAI | OpenAI GPT models | [Docs](https://n8n.io/integrations/openai) |
| OpenAI Chat Model | OpenAI chat completions | [Docs](https://n8n.io/integrations/openai-chat-model) |
| OpenRouter Chat Model | OpenRouter multi-model | [Docs](https://n8n.io/integrations/openrouter-chat-model) |
| Perplexity Chat Model | Perplexity AI | [Docs](https://n8n.io/integrations/perplexity-chat-model) |
| Replicate | Replicate ML models | [Docs](https://n8n.io/integrations/replicate) |
| Text Classifier | Classify text with AI | [Docs](https://n8n.io/integrations/text-classifier) |
| Sentiment Analysis | Analyze text sentiment | [Docs](https://n8n.io/integrations/sentiment-analysis) |

---

## Vector Stores & Embeddings

Nodes for vector databases, embeddings, and RAG workflows.

| Node | Description | Documentation |
|------|-------------|---------------|
| Embeddings AWS Bedrock | AWS Bedrock embeddings | [Docs](https://n8n.io/integrations/embeddings-aws-bedrock) |
| Embeddings Cohere | Cohere embeddings | [Docs](https://n8n.io/integrations/embeddings-cohere) |
| Embeddings Google AI | Google AI embeddings | [Docs](https://n8n.io/integrations/embeddings-google-ai) |
| Embeddings Hugging Face | Hugging Face embeddings | [Docs](https://n8n.io/integrations/embeddings-hugging-face) |
| Embeddings Mistral Cloud | Mistral embeddings | [Docs](https://n8n.io/integrations/embeddings-mistral-cloud) |
| Embeddings Ollama | Ollama embeddings | [Docs](https://n8n.io/integrations/embeddings-ollama) |
| Embeddings OpenAI | OpenAI embeddings | [Docs](https://n8n.io/integrations/embeddings-openai) |
| Pinecone Vector Store | Pinecone database | [Docs](https://n8n.io/integrations/pinecone) |
| Qdrant Vector Store | Qdrant database | [Docs](https://n8n.io/integrations/qdrant) |
| Supabase Vector Store | Supabase pgvector | [Docs](https://n8n.io/integrations/supabase-vector-store) |
| Weaviate Vector Store | Weaviate database | [Docs](https://n8n.io/integrations/weaviate) |
| Zep Vector Store | Zep memory store | [Docs](https://n8n.io/integrations/zep) |
| In-Memory Vector Store | Temporary vector store | [Docs](https://n8n.io/integrations/in-memory-vector-store) |
| Document Default Data Loader | Load documents | [Docs](https://n8n.io/integrations/document-default-data-loader) |
| Recursive Character Text Splitter | Split text into chunks | [Docs](https://n8n.io/integrations/recursive-character-text-splitter) |
| Token Splitter | Split by tokens | [Docs](https://n8n.io/integrations/token-splitter) |
| Vector Store Retriever | Query vector stores | [Docs](https://n8n.io/integrations/vector-store-retriever) |

---

## CRM & Sales

Customer relationship management and sales tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| ActiveCampaign | Marketing automation CRM | [Docs](https://n8n.io/integrations/activecampaign) |
| Affinity | Relationship intelligence | [Docs](https://n8n.io/integrations/affinity) |
| Agile CRM | Sales and marketing CRM | [Docs](https://n8n.io/integrations/agile-crm) |
| Close | Sales CRM | [Docs](https://n8n.io/integrations/close) |
| Copper | Google-integrated CRM | [Docs](https://n8n.io/integrations/copper) |
| Freshsales | Freshworks CRM | [Docs](https://n8n.io/integrations/freshsales) |
| Freshworks CRM | Customer engagement | [Docs](https://n8n.io/integrations/freshworks-crm) |
| HubSpot | Inbound CRM platform | [Docs](https://n8n.io/integrations/hubspot) |
| Intercom | Customer messaging | [Docs](https://n8n.io/integrations/intercom) |
| Keap | Small business CRM | [Docs](https://n8n.io/integrations/keap) |
| Lemlist | Sales engagement | [Docs](https://n8n.io/integrations/lemlist) |
| Mailchimp | Email marketing | [Docs](https://n8n.io/integrations/mailchimp) |
| Pipedrive | Sales CRM | [Docs](https://n8n.io/integrations/pipedrive) |
| Salesforce | Enterprise CRM | [Docs](https://n8n.io/integrations/salesforce) |
| Zendesk | Customer service | [Docs](https://n8n.io/integrations/zendesk) |
| Zoho CRM | Zoho CRM suite | [Docs](https://n8n.io/integrations/zoho-crm) |

---

## Marketing & Email

Email marketing, automation, and outreach tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| AWeber | Email marketing | [Docs](https://n8n.io/integrations/aweber) |
| Brevo | Email and SMS marketing | [Docs](https://n8n.io/integrations/brevo) |
| Campaign Monitor | Email campaigns | [Docs](https://n8n.io/integrations/campaign-monitor) |
| Constant Contact | Email marketing | [Docs](https://n8n.io/integrations/constant-contact) |
| ConvertKit | Creator email marketing | [Docs](https://n8n.io/integrations/convertkit) |
| Customer.io | Messaging automation | [Docs](https://n8n.io/integrations/customerio) |
| Drip | Ecommerce CRM | [Docs](https://n8n.io/integrations/drip) |
| EmailOctopus | Email marketing | [Docs](https://n8n.io/integrations/emailoctopus) |
| GetResponse | Marketing automation | [Docs](https://n8n.io/integrations/getresponse) |
| Instantly | Cold email outreach | [Docs](https://n8n.io/integrations/instantly) |
| Iterable | Growth marketing | [Docs](https://n8n.io/integrations/iterable) |
| Klaviyo | Ecommerce marketing | [Docs](https://n8n.io/integrations/klaviyo) |
| Mailchimp | Email marketing | [Docs](https://n8n.io/integrations/mailchimp) |
| Mailerlite | Email marketing | [Docs](https://n8n.io/integrations/mailerlite) |
| Mailgun | Email API | [Docs](https://n8n.io/integrations/mailgun) |
| Mailjet | Email delivery | [Docs](https://n8n.io/integrations/mailjet) |
| Mautic | Open source marketing | [Docs](https://n8n.io/integrations/mautic) |
| Postmark | Transactional email | [Docs](https://n8n.io/integrations/postmark) |
| SendGrid | Email API | [Docs](https://n8n.io/integrations/sendgrid) |
| Sendinblue | Marketing platform | [Docs](https://n8n.io/integrations/sendinblue) |

---

## Project Management

Task and project management tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| Asana | Work management | [Docs](https://n8n.io/integrations/asana) |
| Basecamp | Project management | [Docs](https://n8n.io/integrations/basecamp) |
| ClickUp | Productivity platform | [Docs](https://n8n.io/integrations/clickup) |
| Jira | Issue tracking | [Docs](https://n8n.io/integrations/jira) |
| Linear | Issue tracking | [Docs](https://n8n.io/integrations/linear) |
| Monday.com | Work OS | [Docs](https://n8n.io/integrations/mondaycom) |
| Notion | Workspace | [Docs](https://n8n.io/integrations/notion) |
| Todoist | Task management | [Docs](https://n8n.io/integrations/todoist) |
| Trello | Kanban boards | [Docs](https://n8n.io/integrations/trello) |
| Wrike | Work management | [Docs](https://n8n.io/integrations/wrike) |

---

## Communication

Messaging and communication platforms.

| Node | Description | Documentation |
|------|-------------|---------------|
| Discord | Gaming community platform | [Docs](https://n8n.io/integrations/discord) |
| Gmail | Google email | [Docs](https://n8n.io/integrations/gmail) |
| Google Chat | Google workspace chat | [Docs](https://n8n.io/integrations/google-chat) |
| IMAP | Email retrieval | [Docs](https://n8n.io/integrations/imap) |
| Matrix | Decentralized chat | [Docs](https://n8n.io/integrations/matrix) |
| Microsoft Outlook | Microsoft email | [Docs](https://n8n.io/integrations/microsoft-outlook) |
| Microsoft Teams | Team collaboration | [Docs](https://n8n.io/integrations/microsoft-teams) |
| Slack | Team messaging | [Docs](https://n8n.io/integrations/slack) |
| Telegram | Messaging app | [Docs](https://n8n.io/integrations/telegram) |
| Twilio | SMS and voice | [Docs](https://n8n.io/integrations/twilio) |
| WhatsApp Business Cloud | WhatsApp messaging | [Docs](https://n8n.io/integrations/whatsapp-business-cloud) |

---

## Databases

Database connections and operations.

| Node | Description | Documentation |
|------|-------------|---------------|
| Airtable | Spreadsheet database | [Docs](https://n8n.io/integrations/airtable) |
| AWS DynamoDB | NoSQL database | [Docs](https://n8n.io/integrations/aws-dynamodb) |
| Azure Cosmos DB | Multi-model database | [Docs](https://n8n.io/integrations/azure-cosmos-db) |
| Baserow | Open source Airtable | [Docs](https://n8n.io/integrations/baserow) |
| Coda | Doc-database hybrid | [Docs](https://n8n.io/integrations/coda) |
| CrateDB | Distributed SQL | [Docs](https://n8n.io/integrations/cratedb) |
| Elasticsearch | Search engine | [Docs](https://n8n.io/integrations/elasticsearch) |
| Firebase Realtime Database | Google realtime DB | [Docs](https://n8n.io/integrations/firebase-realtime-database) |
| Google BigQuery | Data warehouse | [Docs](https://n8n.io/integrations/google-bigquery) |
| Google Sheets | Spreadsheets | [Docs](https://n8n.io/integrations/google-sheets) |
| MariaDB | MySQL fork | [Docs](https://n8n.io/integrations/mariadb) |
| Microsoft SQL | SQL Server | [Docs](https://n8n.io/integrations/microsoft-sql) |
| MongoDB | NoSQL database | [Docs](https://n8n.io/integrations/mongodb) |
| MySQL | Relational database | [Docs](https://n8n.io/integrations/mysql) |
| NocoDB | Open source Airtable | [Docs](https://n8n.io/integrations/nocodb) |
| Postgres | PostgreSQL database | [Docs](https://n8n.io/integrations/postgres) |
| QuestDB | Time series database | [Docs](https://n8n.io/integrations/questdb) |
| Redis | In-memory data store | [Docs](https://n8n.io/integrations/redis) |
| Snowflake | Cloud data warehouse | [Docs](https://n8n.io/integrations/snowflake) |
| SQLite | Embedded database | [Docs](https://n8n.io/integrations/sqlite) |
| Supabase | Postgres platform | [Docs](https://n8n.io/integrations/supabase) |
| TimescaleDB | Time series database | [Docs](https://n8n.io/integrations/timescaledb) |

---

## Cloud & Infrastructure

Cloud services and infrastructure tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| AWS Certificate Manager | SSL/TLS certificates | [Docs](https://n8n.io/integrations/aws-certificate-manager) |
| AWS Cognito | User authentication | [Docs](https://n8n.io/integrations/aws-cognito) |
| AWS IAM | Identity management | [Docs](https://n8n.io/integrations/aws-iam) |
| AWS Lambda | Serverless functions | [Docs](https://n8n.io/integrations/aws-lambda) |
| AWS Rekognition | Image analysis | [Docs](https://n8n.io/integrations/aws-rekognition) |
| AWS S3 | Object storage | [Docs](https://n8n.io/integrations/aws-s3) |
| AWS SES | Email service | [Docs](https://n8n.io/integrations/aws-ses) |
| AWS SNS | Notifications | [Docs](https://n8n.io/integrations/aws-sns) |
| AWS SQS | Message queuing | [Docs](https://n8n.io/integrations/aws-sqs) |
| AWS Textract | Document OCR | [Docs](https://n8n.io/integrations/aws-textract) |
| AWS Transcribe | Speech to text | [Docs](https://n8n.io/integrations/aws-transcribe) |
| Azure Storage | Blob storage | [Docs](https://n8n.io/integrations/azure-storage) |
| Cloudflare | CDN and security | [Docs](https://n8n.io/integrations/cloudflare) |
| DigitalOcean | Cloud infrastructure | [Docs](https://n8n.io/integrations/digitalocean) |
| Docker | Container management | [Docs](https://n8n.io/integrations/docker) |
| Google Cloud Storage | Object storage | [Docs](https://n8n.io/integrations/google-cloud-storage) |
| Kubernetes | Container orchestration | [Docs](https://n8n.io/integrations/kubernetes) |
| Minio | S3-compatible storage | [Docs](https://n8n.io/integrations/minio) |
| Terraform | Infrastructure as code | [Docs](https://n8n.io/integrations/terraform) |

---

## Social Media

Social media platforms and management.

| Node | Description | Documentation |
|------|-------------|---------------|
| Facebook | Social platform | [Docs](https://n8n.io/integrations/facebook) |
| Instagram | Photo sharing | [Docs](https://n8n.io/integrations/instagram) |
| LinkedIn | Professional network | [Docs](https://n8n.io/integrations/linkedin) |
| Medium | Publishing platform | [Docs](https://n8n.io/integrations/medium) |
| Pinterest | Visual discovery | [Docs](https://n8n.io/integrations/pinterest) |
| Reddit | Social news | [Docs](https://n8n.io/integrations/reddit) |
| TikTok | Video platform | [Docs](https://n8n.io/integrations/tiktok) |
| Twitter | Microblogging | [Docs](https://n8n.io/integrations/twitter) |
| YouTube | Video platform | [Docs](https://n8n.io/integrations/youtube) |

---

## E-commerce

E-commerce platforms and payment processing.

| Node | Description | Documentation |
|------|-------------|---------------|
| Chargebee | Subscription billing | [Docs](https://n8n.io/integrations/chargebee) |
| Magento | E-commerce platform | [Docs](https://n8n.io/integrations/magento) |
| Paddle | SaaS payments | [Docs](https://n8n.io/integrations/paddle) |
| PayPal | Payment processing | [Docs](https://n8n.io/integrations/paypal) |
| Recurly | Subscription management | [Docs](https://n8n.io/integrations/recurly) |
| Shopify | E-commerce platform | [Docs](https://n8n.io/integrations/shopify) |
| Stripe | Payment processing | [Docs](https://n8n.io/integrations/stripe) |
| WooCommerce | WordPress commerce | [Docs](https://n8n.io/integrations/woocommerce) |

---

## Developer Tools

Development, version control, and DevOps tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| Bitbucket | Git hosting | [Docs](https://n8n.io/integrations/bitbucket) |
| CircleCI | CI/CD platform | [Docs](https://n8n.io/integrations/circleci) |
| GitHub | Git hosting | [Docs](https://n8n.io/integrations/github) |
| GitLab | DevOps platform | [Docs](https://n8n.io/integrations/gitlab) |
| Jenkins | CI/CD server | [Docs](https://n8n.io/integrations/jenkins) |
| PagerDuty | Incident management | [Docs](https://n8n.io/integrations/pagerduty) |
| Sentry | Error tracking | [Docs](https://n8n.io/integrations/sentry) |

---

## Files & Documents

File storage, document processing, and content management.

| Node | Description | Documentation |
|------|-------------|---------------|
| Box | Cloud storage | [Docs](https://n8n.io/integrations/box) |
| Dropbox | Cloud storage | [Docs](https://n8n.io/integrations/dropbox) |
| FTP | File transfer | [Docs](https://n8n.io/integrations/ftp) |
| Google Drive | Cloud storage | [Docs](https://n8n.io/integrations/google-drive) |
| Microsoft OneDrive | Cloud storage | [Docs](https://n8n.io/integrations/microsoft-onedrive) |
| Microsoft SharePoint | Enterprise content | [Docs](https://n8n.io/integrations/microsoft-sharepoint) |
| Nextcloud | Self-hosted cloud | [Docs](https://n8n.io/integrations/nextcloud) |
| PDF Extract | Parse PDF files | [Docs](https://n8n.io/integrations/pdf-extract) |

---

## Analytics & Monitoring

Analytics, tracking, and monitoring tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| Google Analytics | Web analytics | [Docs](https://n8n.io/integrations/google-analytics) |
| Grafana | Observability | [Docs](https://n8n.io/integrations/grafana) |
| Matomo | Analytics platform | [Docs](https://n8n.io/integrations/matomo) |
| Mixpanel | Product analytics | [Docs](https://n8n.io/integrations/mixpanel) |
| Plausible | Privacy analytics | [Docs](https://n8n.io/integrations/plausible) |
| Prometheus | Monitoring | [Docs](https://n8n.io/integrations/prometheus) |
| Segment | Customer data | [Docs](https://n8n.io/integrations/segment) |

---

## Forms & Surveys

Form builders and survey tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| Cognito Forms | Form builder | [Docs](https://n8n.io/integrations/cognito-forms) |
| Formstack | Form builder | [Docs](https://n8n.io/integrations/formstack) |
| Google Forms | Google forms | [Docs](https://n8n.io/integrations/google-forms) |
| JotForm | Form builder | [Docs](https://n8n.io/integrations/jotform) |
| SurveyMonkey | Survey platform | [Docs](https://n8n.io/integrations/surveymonkey) |
| Tally | Form builder | [Docs](https://n8n.io/integrations/tally) |
| Typeform | Interactive forms | [Docs](https://n8n.io/integrations/typeform) |

---

## HR & Recruiting

Human resources and recruiting tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| BambooHR | HR software | [Docs](https://n8n.io/integrations/bamboohr) |
| Greenhouse | Recruiting | [Docs](https://n8n.io/integrations/greenhouse) |
| Lever | Recruiting | [Docs](https://n8n.io/integrations/lever) |
| Personio | HR platform | [Docs](https://n8n.io/integrations/personio) |
| Workable | Recruiting | [Docs](https://n8n.io/integrations/workable) |

---

## Scheduling & Calendar

Calendar and scheduling tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| Acuity Scheduling | Appointment scheduling | [Docs](https://n8n.io/integrations/acuity-scheduling-trigger) |
| Cal.com | Open source scheduling | [Docs](https://n8n.io/integrations/calcom) |
| Calendly | Meeting scheduling | [Docs](https://n8n.io/integrations/calendly) |
| Google Calendar | Google calendar | [Docs](https://n8n.io/integrations/google-calendar) |
| Microsoft Outlook Calendar | Outlook calendar | [Docs](https://n8n.io/integrations/microsoft-outlook-calendar) |

---

## Support & Helpdesk

Customer support and helpdesk tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| Crisp | Customer messaging | [Docs](https://n8n.io/integrations/crisp) |
| Freshdesk | Helpdesk | [Docs](https://n8n.io/integrations/freshdesk) |
| Help Scout | Customer support | [Docs](https://n8n.io/integrations/help-scout) |
| Zendesk | Customer service | [Docs](https://n8n.io/integrations/zendesk) |
| Zoho Desk | Helpdesk | [Docs](https://n8n.io/integrations/zoho-desk) |

---

## Web Scraping & Data Extraction

Web scraping and data extraction tools.

| Node | Description | Documentation |
|------|-------------|---------------|
| AI Scraper | AI-powered scraping | [Docs](https://n8n.io/integrations/ai-scraper) |
| Apify | Web scraping platform | [Docs](https://n8n.io/integrations/apify) |
| Bright Data | Proxy and scraping | [Docs](https://n8n.io/integrations/bright-data) |
| Firecrawl | Web crawling | [Docs](https://n8n.io/integrations/firecrawl) |
| Spider | Web scraping | [Docs](https://n8n.io/integrations/spider) |

---

## Automation & Integration

General automation and integration platforms.

| Node | Description | Documentation |
|------|-------------|---------------|
| AMQP | Message queuing | [Docs](https://n8n.io/integrations/amqp-sender) |
| GraphQL | GraphQL API calls | [Docs](https://n8n.io/integrations/graphql) |
| MQTT | IoT messaging | [Docs](https://n8n.io/integrations/mqtt) |
| RabbitMQ | Message broker | [Docs](https://n8n.io/integrations/rabbitmq) |
| Webhook | HTTP webhooks | [Docs](https://n8n.io/integrations/webhook) |
| Zapier | Automation platform | [Docs](https://n8n.io/integrations/zapier) |

---

## Additional Resources

- **Full Integration List:** [n8n.io/integrations](https://n8n.io/integrations)
- **n8n Documentation:** [docs.n8n.io](https://docs.n8n.io)
- **Community Templates:** [n8n.io/workflows](https://n8n.io/workflows)
- **Community Forum:** [community.n8n.io](https://community.n8n.io)

---

*This document provides a curated overview of commonly used n8n nodes. For the complete list of 500+ integrations, visit the official n8n integrations page.*
