import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def create_table(max_repeats, databasefile="flights.db"):
    if max_repeats == 0:
        return  # Nie twórz tabeli, jeśli nie pozyskujemy nowych danych

    connection = sqlite3.connect(databasefile)
    cursor = connection.cursor()

    # Usuń tabelę, jeśli istnieje, i utwórz nową
    cursor.execute('''DROP TABLE IF EXISTS airport_atl''')
    cursor.execute('''CREATE TABLE airport_atl (
                        icao24 TEXT,
                        callsign TEXT,
                        origin_country TEXT,
                        time_position TEXT,
                        last_contact TEXT,
                        long REAL,
                        lat REAL,
                        baro_altitude REAL,
                        on_ground TEXT,
                        velocity REAL,
                        true_track REAL,
                        vertical_rate REAL,
                        sensors TEXT,
                        geo_altitude REAL,
                        squawk TEXT,
                        spi TEXT,
                        position_source INTEGER
                    )''')

    connection.commit()
    connection.close()


def save_to_db(flight_df, databasefile="flights.db"):
    connection = sqlite3.connect(databasefile)
    flight_df.to_sql("airport_atl", connection, if_exists="append", index=False)
    connection.close()


def load_flight_data(databasefile="flights.db"):
    connection = sqlite3.connect(databasefile)
    flight_df = pd.read_sql_query("SELECT * FROM airport_atl", connection)
    connection.close()
    return flight_df
