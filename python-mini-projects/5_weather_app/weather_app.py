#!/usr/bin/env python3
"""Weather App - Get Weather Data"""

import urllib.request
import json

class Weather:
    def __init__(self):
        self.key = "5a2101621fa43f3106d384f24940c088"   # <-- put your API key here
        self.url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch(self, city):
        try:
            u = f"{self.url}?q={city}&appid={self.key}&units=metric"
            with urllib.request.urlopen(u) as r:
                return json.loads(r.read().decode())
        except:
            return None

    def show(self, d):
        if not d:
            print("\n❌ City not found or API error!")
            return

        c = d["name"]
        t = d["main"]["temp"]
        ds = d["weather"][0]["description"]
        h = d["main"]["humidity"]

        print(f"\n🌤️  {c}")
        print(f"Temp     : {t}°C")
        print(f"Condition: {ds}")
        print(f"Humidity : {h}%")

def main():
    print("=" * 60)
    print("WEATHER APP".center(60))
    print("=" * 60)

    app = Weather()

    while True:
        city = input("\nCity (type 'quit' to exit): ").strip()

        if city.lower() == "quit":
            print("\n👋 Goodbye!")
            break

        d = app.fetch(city)
        app.show(d)

if __name__ == "__main__":
    main()
