import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load variables from .env

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print("❌ API key not found. Make sure it's set in the .env file.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"\n🌤️ Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°F")
        print(f"Feels like: {data['main']['feels_like']}°F")
        print(f"Weather: {data['weather'][0]['description'].title()}")
    else:
        print("❌ Could not retrieve weather data. Please check the city name.")

if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    get_weather(city_name)