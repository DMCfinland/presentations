---
id: BP_05_RAG_LIBRARIAN
title: RAG Librarian & Knowledge Base
type: Data
priority: High
complexity: L
dependencies: [BP_10_INFRA_SECURITY]
tags: [azure-ai-search, vector-db, embeddings, ingestion]
context_source: docs/architecture/PROJECT_CONTEXT.md
---

## 1. Purpose & Business Value

Tämä moduuli on järjestelmän "kirjasto". Se indeksoi tuotteet, ohjeet ja kulttuurisisällön vektori-tietokantaan, jotta agentit voivat hakea relevanttia tietoa.

[cite_start]**Business Value:** Mahdollistaa "Scrape First" -strategian (kaiken tiedon imurointi) ja takaa, että vastaukset perustuvat ajantasaiseen dataan [cite: 6180-6185].

## 2. Agentic Flow (Logic)

* **Trigger:** Ajastettu ajo (Batch) tai `NEW_DOCUMENT_UPLOAD` -tapahtuma.

* **Process:**

    1.  **Ingest:** Lue lähde (PDF, Web Scrape JSON, Partner API).

    2.  **Chunking:** Pilko teksti semanttisiin osiin (esim. max 500 tokenia).

    3.  **Enrichment:** Lisää metadata: `shelf`, `tenant_id`, `valid_until`.

    4.  **Embedding:** Generoi vektorit (text-embedding-3-small).

    5.  **Indexing:** Tallenna Azure AI Searchiin.

    6.  **Sanity Check:** Vertaa uutta hintaa vanhaan. Jos ero > 20% -> Luo `CONFLICT_TICKET` Staff Dashboardille.

## 3. Data Contracts (Schema Definition)

### Vector Index Schema (Azure AI Search)

* `id` (String, Unique)
* `content` (String, Searchable)
* `vector` (Collection(Single), 1536 dims)
* `metadata` (ComplexType):
    * `shelf`: "Commercial" | "Cultural" | "Practical" | "Internal"
    * `tenant_id`: "jarvisydan"
    * `product_id`: Optional(Link to SQL)
    * `last_updated`: DateTime

### [cite_start]The Shelves (Hyllyt) [cite: 6181-6185]

1.  **Commercial:** Tuotteet, hinnat, aukioloajat.
2.  **Cultural:** Tarinat, historia.
3.  **Practical:** WiFi, pysäköinti, check-in.
4.  **Internal:** Brändiohjeet, Optimizerin säännöt.

## 4. Edge Cases & Resilience

* **Vanhentunut data:** Haku suodattaa automaattisesti `valid_until` < NOW.

* **Tenant Isolation:** Haku vaatii AINA `filter=tenant_id eq 'current'` (RLS).

* **Roskadata:** Scraperin output ajetaan LLM-siivoojan läpi ennen indeksointia.

## 5. Success Criteria (Sub-Boss Checklist)

- [ ] Vektorihaku palauttaa relevantit chunkit < 500ms.
- [ ] Metadata-filtteröinti toimii (Shelf/Tenant).
- [ ] Conflict detection estää virheellisten hintojen automaattisen julkaisun.

