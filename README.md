<div align="center">

# Architecture Overview
## **High-level Flow**

```mermaid
graph TD
    A[Unity Catalog Metadata] --> B(Document Preparation: Schema + KPIs)
    B --> C(Embeddings: Vector Store)
    C --> D(Retriever)
    D --> E(GPT-5-nano: SQL Generator)
    E --> F[Validated SQL Query]
    
