# FinnConcierge

AI-powered serverless concierge platform for Finnish tourism destinations.

## 🎯 Vision

FinnConcierge transforms destination management through an AI-powered, white-label concierge system that delivers hyper-personalized experiences while maintaining operational efficiency. Built on Azure serverless architecture, it enables "Win-Win-Win" outcomes for travelers, destinations, and service providers.

## 📦 Monorepo Structure

```
finnconcierge/
├── apps/                        # Frontend Applications
│   └── traveler-pwa/            # Next.js 15 PWA (BP_11)
├── services/                    # Backend Services
│   └── ingestion/               # Azure Functions - Webhook & Identity (BP_01)
├── packages/                    # Shared Packages
│   └── shared-types/            # TypeScript type definitions
├── database/                    # Database Schemas
│   ├── sql/                     # Azure SQL (BP_01, BP_07)
│   └── cosmos/                  # Cosmos DB definitions
├── infrastructure/              # Infrastructure as Code
│   ├── event-grid/              # Event subscriptions
│   └── apim/                    # API Management policies
├── docs/                        # Documentation
│   ├── architecture/            # Architecture documents
│   └── blueprints/              # Module specifications (BP_01-11)
└── tests/                       # E2E & Integration Tests

```

## 🏗️ Architecture

### Technology Stack

- **Frontend**: Next.js 15, React 19, TypeScript, Tailwind CSS
- **Backend**: Azure Functions (Python v2), Node.js/TypeScript
- **Databases**: 
  - Azure SQL (transactional data, Shadow Ledger)
  - Cosmos DB (sessions, hot storage)
  - Azure AI Search (vector search, RAG)
- **Event Bus**: Azure Event Grid
- **AI/ML**: OpenAI GPT-4, Azure OpenAI Service
- **Infrastructure**: Azure (serverless, PaaS)

### Key Patterns

- **Microservices**: Event-driven, loosely coupled
- **RAG (Retrieval-Augmented Generation)**: Grounded AI responses
- **Multi-tenancy**: White-label for multiple destinations
- **Polyglot Persistence**: SQL + NoSQL + Vector DB

## 🚀 Getting Started

### Prerequisites

- Node.js 20+
- Python 3.11+
- Azure Functions Core Tools v4
- Azure CLI
- Docker (optional, for local SQL)

### Installation

```bash
# Install dependencies
npm install

# Build shared types
npm run types:build

# Start Traveler PWA
npm run traveler:dev

# Start Ingestion Service
cd services/ingestion
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
func start
```

### Development Workflow

```bash
# Run all services in dev mode
npm run dev

# Build all packages
npm run build

# Run tests
npm run test

# Lint code
npm run lint
```

## 📋 Module Roadmap (Blueprints)

| Blueprint | Module | Priority | Status |
|-----------|--------|----------|--------|
| BP_01 | Ingestion & Identity | CRITICAL | 🏗️ Scaffolded |
| BP_02 | Master Agent | CRITICAL | 📝 Planned |
| BP_03 | Mood Evaluator | CRITICAL | 📝 Planned |
| BP_04 | Suggestion Chef | CRITICAL | 📝 Planned |
| BP_05 | RAG Librarian | HIGH | 📝 Planned |
| BP_06 | Booker Agent | CRITICAL | 📝 Planned |
| BP_07 | Shadow Ledger | HIGH | 🏗️ Schema Ready |
| BP_08 | Staff Dashboard | CRITICAL | 📝 Planned |
| BP_09 | Watchdog & Insight | MEDIUM | 📝 Planned |
| BP_10 | Infra & Security | CRITICAL | 📝 Planned |
| BP_11 | Traveler UI | HIGH | 🏗️ Scaffolded |

## 🔑 Key Features

### For Travelers
- 🔐 **Passwordless Access**: Magic Link authentication
- 🎨 **Chameleon UI**: Dynamic branding per destination
- 💬 **AI Chat**: 24/7 intelligent assistance
- 📅 **Smart Timeline**: Itinerary management
- 🌍 **Hyper-Personalization**: Mood-based recommendations

### For Destinations (DMCs)
- 👥 **White-Label**: Custom branding and domain
- 📊 **Analytics Dashboard**: Real-time insights
- 🤝 **Whisper Mode**: Staff can guide AI responses
- 💰 **Revenue Tracking**: Commission management
- 🔔 **Smart Alerts**: Proactive issue detection

### For Service Providers
- 🔌 **API Integration**: Seamless booking automation
- 📈 **Exposure**: AI-powered recommendations
- 💳 **Flexible Commission**: Transparent revenue sharing

## 📚 Documentation

- [Master Architecture Map](./docs/architecture/MASTER_MAP.md)
- [Blueprints](./docs/blueprints/) - Detailed module specifications
- [Database Schema](./database/README.md)
- [Shared Types](./packages/shared-types/README.md)

## 🔐 Security & Compliance

- **GDPR Compliant**: PII hashing, RLS, data retention policies
- **Zero Trust**: API key authentication, HMAC signatures
- **Audit Trail**: Immutable Shadow Ledger for all transactions
- **Tenant Isolation**: Row-Level Security (RLS) in Azure SQL

## 🌍 Environment Variables

### Frontend (Traveler PWA)
```env
NEXT_PUBLIC_API_URL=https://api.finnconcierge.com
NEXT_PUBLIC_WS_URL=wss://api.finnconcierge.com
```

### Backend (Ingestion Service)
```env
SQL_CONNECTION_STRING=<Azure SQL connection>
COSMOS_CONNECTION_STRING=<Cosmos DB connection>
EVENT_GRID_TOPIC_ENDPOINT=<Event Grid endpoint>
JWT_SECRET_KEY=<secret>
SENDGRID_API_KEY=<SendGrid key>
```

## 🧪 Testing

```bash
# Unit tests
npm run test

# E2E tests
npm run test:e2e

# Integration tests
npm run test:integration
```

## 📦 Deployment

### Azure Resources Required

1. **Compute**: Azure Functions (Premium Plan)
2. **Databases**: Azure SQL, Cosmos DB
3. **Storage**: Azure Blob Storage, AI Search
4. **Messaging**: Event Grid, Service Bus
5. **Networking**: API Management, Front Door
6. **Monitoring**: Application Insights, Log Analytics

### Deployment Commands

```bash
# Deploy infrastructure
cd infrastructure
terraform apply

# Deploy functions
func azure functionapp publish fn-ingestion-prod

# Deploy frontend
cd apps/traveler-pwa
npm run build
# Deploy to Azure Static Web Apps or App Service
```

## 🤝 Contributing

This is a private project. For questions or collaboration, contact the project team.

## 📄 License

Proprietary - All Rights Reserved

## 🎯 Current Phase: VAIHE 1 - SCAFFOLDING ✅

Phase 1 (Scaffolding) is **COMPLETE**:

- ✅ Monorepo structure with workspaces
- ✅ Next.js 15 Traveler PWA skeleton
- ✅ Azure Functions Python v2 Ingestion service
- ✅ Shared TypeScript types package
- ✅ SQL database schema (BP_01, BP_07)
- ✅ Cosmos DB collection definitions
- ✅ Development tooling (Turbo, ESLint, TypeScript)

**Next Steps**: Proceed to VAIHE 2 - Implementation of critical modules (BP_01, BP_02, BP_03)

---

Built with ❤️ for Finnish destinations
