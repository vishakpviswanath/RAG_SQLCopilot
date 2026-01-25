from openai import OpenAI
from dotenv import load_dotenv
from retriever import retrieve_context

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are a senior SQL analyst.

You generate accurate, production-grade SQL queries
using ONLY the provided schema metadata.

Rules:
- Use fully qualified table names: PySpark_dbt.Gold.<table>
- Use ONLY columns explicitly listed
- Use JOIN LOGIC exactly as provided
- Do NOT infer relationships
- Prefer FACT tables as the base table
- Use Spark SQL syntax
"""

def generate_sql(user_question: str) -> str:
    context = retrieve_context(user_question)

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"""
SCHEMA CONTEXT:
{context}

QUESTION:
{user_question}

Generate SQL:
"""}
        ]
    )

    return response.choices[0].message.content
