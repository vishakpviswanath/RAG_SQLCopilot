<div align ="center">
SQL Analyst Copilot
</div>

A Retrieval Augmented Generation (RAG) based SQL Copilot that generates accurate, production grade Spark SQL by grounding LLM outputs in Databricks Unity Catalog metadata.

This project demonstrates how to build a hallucination-resistant SQL generation system by combining vector search, schema metadata retrieval and constrained LLM prompting.

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
    



