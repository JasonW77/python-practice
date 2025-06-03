import requests

API_KEY = "",
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
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