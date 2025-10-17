"""
🌦️ Simple Weather App
----------------------
Author: Mahvil
GitHub: https://github.com/Mahvil
Project: Hacktoberfest 2025 Contribution
Description:
    This Python script fetches and displays real-time weather information
    for any city using the OpenWeatherMap API.
    It shows the temperature, humidity, and weather condition
    in an easy-to-read format.
"""

import requests

def get_weather(city_name, api_key):
    """
    Fetches weather data for a given city using OpenWeatherMap API.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            print("\n🌤️ Weather Report:")
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Condition: {data['weather'][0]['description'].capitalize()}")
        elif response.status_code == 404:
            print("⚠️ City not found. Please check the name and try again.")
        else:
            print("❌ Unable to fetch weather data. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("=== 🌦️ Simple Weather App ===")
    city = input("Enter city name: ").strip()

    # 🔑 Replace with your own API key from https://openweathermap.org/api
    api_key = "YOUR_API_KEY_HERE"

    if not city:
        print("⚠️ Please enter a valid city name.")
    else:
        get_weather(city, api_key)
