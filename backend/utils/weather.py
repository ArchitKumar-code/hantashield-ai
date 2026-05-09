import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather_data(city):

    weather_url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    )

    weather_response = requests.get(weather_url).json()

    print(weather_response)

    if "coord" not in weather_response:

        raise Exception(
            f"City not found or API error: {weather_response}"
        )

    lat = weather_response["coord"]["lat"]
    lon = weather_response["coord"]["lon"]

    humidity = weather_response["main"]["humidity"]

    precipitation = 0

    if "rain" in weather_response:
        precipitation = weather_response["rain"].get("1h", 0)

    aqi_url = (
        f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    aqi_response = requests.get(aqi_url).json()

    aqi = aqi_response["list"][0]["main"]["aqi"] * 20

    return {
        "humidity": humidity,
        "precipitation": precipitation,
        "aqi": aqi,
        "lat": lat,
        "lon": lon
    }