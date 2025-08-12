import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DBNAME = os.getenv('DBNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

conn = psycopg2.connect(
    host=HOST,
    port=PORT,
    dbname=DBNAME,
    user=USER,
    password=PASSWORD
)
cur = conn.cursor()

csv_file = [
    'data/seasons.csv',
    'data/circuits.csv',
    'data/constructors.csv',
    'data/drivers.csv',
    'data/status.csv',
    'data/races.csv',
    'data/constructor_results.csv',
    'data/constructor_standings.csv',
    'data/driver_standings.csv',
    'data/lap_times.csv',
    'data/pit_stops.csv',
    'data/qualifying.csv',
    'data/results.csv',
    'data/sprint_results.csv',
]

query_list = [
    "INSERT INTO seasons (year, url) VALUES (%s, %s)",
    "INSERT INTO circuits (circuit_id, circuit_ref, name, location, country, lat, lng, alt, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO constructors (constructor_id, constructor_ref, name, nationality, url) VALUES (%s, %s, %s, %s, %s)",
    "INSERT INTO drivers (driver_id, driver_ref, number, code, forename, surname, dob, nationality, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO status (status_id, status) VALUES (%s, %s)",
    "INSERT INTO races (race_id, year, round, circuit_id, name, date, time, url, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO constructor_results (constructor_result_id, race_id, constructor_id, points, status) VALUES (%s, %s, %s, %s, %s)",
    "INSERT INTO constructor_standings (constructor_standing_id, race_id, constructor_id, points, position, position_text, wins) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO driver_standings (driver_standing_id, race_id, driver_id, points, position, position_text, wins) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO lap_times (race_id, driver_id, lap, position, time, milliseconds) VALUES (%s, %s, %s, %s, %s, %s)",
    "INSERT INTO pit_stops (race_id, driver_id, stop, lap, time, duration, milliseconds) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO qualifying (qualifying_id, race_id, driver_id, constructor_id, number, position, q1, q2, q3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO results (result_id, race_id, driver_id, constructor_id, number, grid, position, position_text, position_order, points, laps, time, milliseconds, fastest_lap, rank, fastest_lap_time, fastest_lap_speed, status_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "INSERT INTO sprint_results (result_id, race_id, driver_id, constructor_id, number, grid, position, position_text, position_order, points, laps, time, milliseconds, fastest_lap, fastest_lap_time, status_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
];

for csv, query in zip(csv_file, query_list):
    print(f"Processing {csv}")
    df = pd.read_csv(csv)
    for index, row in df.iterrows():
        values = list(row)
        cur.execute(query, values)
        conn.commit()

cur.close()
conn.close()