# Databricks notebook source
# MAGIC %md
# MAGIC #RAG DOC PREPARATION

# COMMAND ----------

# MAGIC %md
# MAGIC ### Table Retrieval

# COMMAND ----------

CATALOG = "PySpark_dbt"
SCHEMA = "Gold"

tables_df = spark.sql(f"""
SHOW TABLES IN {CATALOG}.{SCHEMA}
""")

tables = [row.tableName for row in tables_df.collect()]

# COMMAND ----------

def get_table_columns(table):
    return spark.sql(f"""
    DESCRIBE TABLE {CATALOG}.{SCHEMA}.{table}
    """)

metadata = {}

for table in tables:
    metadata[table] = get_table_columns(table).toPandas()


# COMMAND ----------

# MAGIC %md
# MAGIC ### Defining Business Semantics

# COMMAND ----------

TRIPS_DOC = """
TABLE: fact_trips
TYPE: FACT
GRAIN: One row per completed trip

PRIMARY KEY:
- trip_id

FOREIGN KEYS:
- customer_id → dim_customers.customer_id
- driver_id → dim_drivers.driver_id
- vehicle_id → dim_vehicles.vehicle_id
MEASURES:
- trip_start_time
- trip_end_time
- distance_km
- trip_duration_minutes
- fare_amount

COMMON KPIs:
- Total Trips = COUNT(trip_id)
- Total Revenue = SUM(total_amount)
- Average Fare = AVG(fare_amount)
- Average Trip Distance = AVG(distance_km)
- Revenue per Trip = SUM(fare_amount) / COUNT(trip_id)

"""


# COMMAND ----------

CUSTOMERS_DOC = """
TABLE: dim_customers
TYPE: DIMENSION

PRIMARY KEY:
- customer_id

ATTRIBUTES:
- first_name
- last_name
- email
- phone_number
- city
- signup_date

JOIN LOGIC:
- fact_trips.customer_id = dim_customers.customer_id
"""


# COMMAND ----------

DRIVERS_DOC = """
TABLE: dim_drivers
TYPE: DIMENSION

PRIMARY KEY:
- driver_id

FOREIGN KEYS:
- vehicle_id → dim_vehicles.vehicle_id

ATTRIBUTES:
- first_name
- last_name
- phone_number
- driver_rating
- city

JOIN LOGIC:
- fact_trips.driver_id = dim_drivers.driver_id

"""


# COMMAND ----------

VEHICLES_DOC = """
TABLE: dim_vehicles
TYPE: DIMENSION

PRIMARY KEY:
- vehicle_id

ATTRIBUTES:
- license_plate
- make
- model
- year
- vehicle_type

JOIN LOGIC:
- fact_trips.vehicle_id = dim_vehicles.vehicle_id
"""


# COMMAND ----------

LOCATIONS_DOC = """
TABLE: dim_locations
TYPE: DIMENSION

PRIMARY KEY:
- location_id

ATTRIBUTES:
- city
- state
- country
- latitude
- longitude


"""


# COMMAND ----------

PAYMENTS_DOC = """
TABLE: dim_payments
TYPE: DIMENSION

PRIMARY KEY:
- payment_id

FOREIGN KEYS:
- customer_id → dim_customers.customer_id
- trip_id → fact_trips.trip_id

ATTRIBUTES:
- payment_method
- payment_status
- transaction_time
- amount

JOIN LOGIC:
- fact_trips.trip_id = dim_payments.trip_id
"""


# COMMAND ----------

documents = [
    TRIPS_DOC,
    CUSTOMERS_DOC,
    DRIVERS_DOC,
    VEHICLES_DOC,
    LOCATIONS_DOC,
    PAYMENTS_DOC
]


# COMMAND ----------

rag_docs = [
    {
        "doc_id": "fact_trips",
        "table": "fact_trips",
        "type": "FACT",
        "content": TRIPS_DOC
    },
    {
        "doc_id": "dim_customers",
        "table": "dim_customers",
        "type": "DIMENSION",
        "content": CUSTOMERS_DOC
    },
    {
        "doc_id": "dim_drivers",
        "table": "dim_drivers",
        "type": "DIMENSION",
        "content": DRIVERS_DOC
    },
    {
        "doc_id": "dim_vehicles",
        "table": "dim_vehicles",
        "type": "DIMENSION",
        "content": VEHICLES_DOC
    },
    {
        "doc_id": "dim_locations",
        "table": "dim_locations",
        "type": "DIMENSION",
        "content": LOCATIONS_DOC
    },
    {
        "doc_id": "dim_payments",
        "table": "dim_payments",
        "type": "DIMENSION",
        "content": PAYMENTS_DOC
    }
]


# COMMAND ----------

# DBTITLE 1,Cell 15
import json

workspace_path = "/Workspace/Users/user@gmail.com/RAG_Project/sql_metadata_docs.json"

with open(workspace_path, "w") as f:
    json.dump(rag_docs, f, indent=2)

print("Saved to Workspace Files")



# COMMAND ----------

