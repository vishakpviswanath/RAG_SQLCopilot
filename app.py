from retriever import retrieve_context
from sql_generator import generate_sql
from evaluation.confidence import compute_confidence
from retry.strategies import RETRY_STRATEGIES
from feedback.logger import log_failure

CONFIDENCE_THRESHOLD = 0.75


def main():
    print("Self-Healing SQL Analyst Copilot")
    print("Type 'exit' to quit\n")

    while True:
        question = input("Ask your SQL question: ")
        if question.lower() == "exit":
            break

        for attempt, strategy in enumerate(RETRY_STRATEGIES, start=1):
            rewritten_question = strategy(question)
            context = retrieve_context(rewritten_question)
            sql = generate_sql(question, context)

            confidence = compute_confidence(sql, context)

            print(f"\nAttempt {attempt} | Confidence: {confidence:.2f}")

            if confidence >= CONFIDENCE_THRESHOLD:
                print("\n✅ Final SQL:\n")
                print(sql)
                break
            else:
                if attempt == len(RETRY_STRATEGIES):
                    log_failure(
                        question=question,
                        sql=sql,
                        confidence=confidence,
                        reason="Low confidence after retries"
                    )
                    print("\n❌ Unable to generate confident SQL. Logged for review.\n")


if __name__ == "__main__":
    main()
