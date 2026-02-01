def score_retrieval(context: str) -> float:

    signals = [
        "FACT",
        "JOIN LOGIC",
        "PRIMARY KEY"
    ]

    hits = sum(1 for s in signals if s in context)
    return hits / len(signals)
