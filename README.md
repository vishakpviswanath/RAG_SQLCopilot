<div align="center">

# Architecture Overview
## **High-level Flow**

```mermaid
graph TD
    A[Unity Catalog Metadata] --> B(Document Preparation)
    B --> C(Embeddings: Vector Store)
    C --> D(Retriever)
    D --> E(GPT-5-nano: SQL Generator)
    E --> F[Validated SQL Query]
    

