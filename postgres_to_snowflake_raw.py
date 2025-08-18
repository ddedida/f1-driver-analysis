import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DBNAME = os.getenv('DBNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')
SNOWFLAKE_ROLE = os.getenv('SNOWFLAKE_ROLE')

pg_engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}")
df = pd.read_sql_query("SELECT * FROM drivers", pg_engine)

snowflake_url = f"snowflake://{SNOWFLAKE_USER}:{quote_plus(SNOWFLAKE_PASSWORD)}@{SNOWFLAKE_ACCOUNT}/{SNOWFLAKE_DATABASE}/{SNOWFLAKE_SCHEMA}?warehouse={SNOWFLAKE_WAREHOUSE}&role={SNOWFLAKE_ROLE}"
sf_engine = create_engine(snowflake_url)

tables = [
    'circuits',
    'constructors',
    'constructor_results',
    'constructor_standings',
    'drivers',
    'driver_standings',
    'lap_times',
    'qualifying',
    'races',
    'results',
    'sprint_results',
    'status'
]

try:
    for table in tables:
        df.to_sql(
            name=table,
            con=sf_engine,
            if_exists='replace',
            index=False,
            method='multi',
            chunksize=1000
        )
        print(f"Successfully uploaded data to Snowflake table: {table}")

except Exception as e:
    print(f"SQLAlchemy method failed: {e}")
    
    try:
        for table in tables:
            df.to_sql(
                name=table,
                con=sf_engine,
                if_exists='replace',
                index=False,
                method='multi',
                chunksize=1000
            )
            print(f"Successfully uploaded data to Snowflake table: {table}")

    except Exception as e2:
        print(f"Fallback method also failed: {e2}")

pg_engine.dispose()
sf_engine.dispose()