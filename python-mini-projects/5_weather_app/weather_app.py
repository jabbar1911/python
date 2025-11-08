#!/usr/bin/env python3
"""Weather App - Get Weather Data"""

import urllib.request
import json
import os

class WeatherApp:
    def __init__(self, api_key=None):
        self.api_key = api_key or "YOUR_API_KEY"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        try:
            url = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
            with urllib.request.urlopen(url) as response:
                return json.loads(response.read().decode())
        except:
            return None

    def display(self, data):
        if not data:
            return

        city = data['name']
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f"\n🌤️  {city}")
        print(f"Temp: {temp}°C")
        print(f"Condition: {desc}")
        print(f"Humidity: {humidity}%")

def main():
    print("WEATHER APP")
    print("\n⚠️  Get free API key from openweathermap.org")

    api_key = input("\nAPI Key (or press Enter): ").strip()
    app = WeatherApp(api_key)

    while True:
        city = input("\nCity (quit to exit): ").strip()

        if city.lower() == 'quit':
            print("Goodbye!")
            break

        data = app.get_weather(city)
        app.display(data)

if __name__ == "__main__":
    main()
