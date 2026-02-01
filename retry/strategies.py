def original_query(q: str) -> str:
    return q


def expanded_query(q: str) -> str:
    return f"{q}. Include joins, fact tables, and metrics."


def schema_explicit_query(q: str) -> str:
    return f"{q}. Use fact tables and provided join logic only."


RETRY_STRATEGIES = [
    original_query,
    expanded_query,
    schema_explicit_query
]
