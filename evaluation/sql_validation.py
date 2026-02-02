import re

def extract_tables(sql: str) -> set:
    matches = re.findall(r'FROM\s+([\w\.]+)|JOIN\s+([\w\.]+)', sql, re.IGNORECASE)
    tables = set(filter(None, sum(matches, ())))
    table_names = {name.split('.')[-1] for name in tables}
    return table_names


def validate_sql(sql: str, context: str) -> float:
    
    used_tables = extract_tables(sql)
    allowed_tables = set()

    for line in context.splitlines():
        if line.startswith("TABLE:"):
            allowed_tables.add(line.split(":")[1].strip())
    return 1.0 if used_tables.issubset(allowed_tables) else 0.0                 #Returns 1.0 if SQL only uses tables in context, else 0.0

