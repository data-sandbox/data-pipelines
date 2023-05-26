import os
import requests
import argparse
from dotenv import load_dotenv, find_dotenv


def get_temperature(lat, lon):
    """
    Get current temperature for location based on input
    latitude and longitude.
    """

    _ = load_dotenv(find_dotenv())
    api_key = os.getenv('OPENWEATHER_KEY')

    params = {'lat': lat,
              'lon': lon,
              'appid': api_key,
              'units': 'imperial'}
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?', params=params)

    # Send to stdout
    print(response.json()['main']['temp'])

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--lat', help="Latitude of location.")
    parser.add_argument(
        '--lon', help="Longitude of location.")
    args = parser.parse_args()

    get_temperature(args.lat, args.lon)
