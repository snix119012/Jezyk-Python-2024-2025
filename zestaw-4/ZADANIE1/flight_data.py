import pandas as pd
import matplotlib.pyplot as plt
import requests
from ZADANIE1.database import save_to_db, load_flight_data


def fetch_flight_data(databasefile="flights.db"):
    lon_min, lat_min = -85.4277, 32.6407
    lon_max, lat_max = -83.4277, 34.6407

    user_name = "your_username"
    password = "your_password"
    url_data = (
        f"https://{user_name}:{password}@opensky-network.org/api/states/all?"
        f"lamin={lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}"
    )
    try:
        response = requests.get(url_data)
        response.raise_for_status()
        data = response.json()
        col_name = [
            'icao24', 'callsign', 'origin_country', 'time_position', 'last_contact',
            'long', 'lat', 'baro_altitude', 'on_ground', 'velocity',
            'true_track', 'vertical_rate', 'sensors', 'geo_altitude',
            'squawk', 'spi', 'position_source'
        ]
        flight_df = pd.DataFrame(data['states'], columns=col_name).fillna('No Data')
        save_to_db(flight_df, databasefile)
        print("Data saved to database successfully!")

    except requests.RequestException as e:
        print(f"Error fetching data from OpenSky API: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def plot_flight_data(databasefile="flights.db", show_plot=True):
    flight_df = load_flight_data(databasefile)

    flight_df = flight_df.dropna(subset=['velocity', 'geo_altitude'])
    flight_df['velocity'] = pd.to_numeric(flight_df['velocity'], errors='coerce')
    flight_df['geo_altitude'] = pd.to_numeric(flight_df['geo_altitude'], errors='coerce')
    flight_df['velocity'] = flight_df['velocity'] * 3.6
    flight_df['geo_altitude'] = flight_df['geo_altitude'] / 1000
    flight_df = flight_df.sort_values(by='velocity', ascending=False).drop_duplicates(subset='icao24', keep='first')

    plt.figure(figsize=(10, 6))
    plt.scatter(flight_df['velocity'], flight_df['geo_altitude'], alpha=0.6, s=50, c='blue', marker='o')
    plt.title("Wysokość geograficzna (km) w funkcji prędkości (km/h)")
    plt.xlabel("Prędkość (km/h)")
    plt.ylabel("Wysokość geograficzna (km)")
    plt.xlim(0, 1200)
    plt.ylim(0, 14)
    plt.grid(True)
    plt.tight_layout()

    if show_plot:
        plt.show()
