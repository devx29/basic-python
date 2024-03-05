import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def get_weather_now():
    city = input("\nEnter city name: ")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    weather_data = requests.get(request_url).json()
    pprint(weather_data)
    print(f"Current temperature in {city.capitalize()} is {weather_data['main']['temp']:.2f} degrees farenheit")

if __name__ == "__main__":
    get_weather_now()