from evaluation.retrieval_quality import score_retrieval
from evaluation.sql_validation import validate_sql

def compute_confidence(sql: str, context: str) -> float:
    scores = []
    retrieval_score = score_retrieval(context)
    sql_validity = validate_sql(sql, context)
    
    confidence = (
        0.6 * retrieval_score +
        0.4 * sql_validity
    )
    scores.append({"Retrieval Score":retrieval_score})
    scores.append({"SQL Validity": sql_validity})
    scores.append({"Overall Confidence": confidence})
    return scores
