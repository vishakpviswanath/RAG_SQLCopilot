import json
from datetime import datetime

LOG_FILE = "feedback/failures.jsonl"

def log_failure(question, sql, confidence, reason):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "sql": sql,
        "confidence": confidence,
        "reason": reason
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")
