from sql_generator import generate_sql

def main():
    print("🚀 SQL Analyst Copilot (RAG-powered)")
    print("Type 'exit' to quit\n")

    while True:
        question = input("Ask your SQL question: ")

        if question.lower() == "exit":
            break

        sql = generate_sql(question)
        print("\n🧠 Generated SQL:\n")
        print(sql)
        print("\n" + "-"*80 + "\n")

if __name__ == "__main__":
    main()
