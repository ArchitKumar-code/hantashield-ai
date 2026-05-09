from utils.weather import get_weather_data
from utils.vegetation import get_vegetation_index
from utils.floods import get_flood_risk
from utils.rodents import estimate_rodent_population


def calculate_hantavirus_risk(city):

    weather = get_weather_data(city)

    humidity = weather["humidity"]
    precipitation = weather["precipitation"]
    aqi = weather["aqi"]

    lat = weather["lat"]
    lon = weather["lon"]

    vegetation = get_vegetation_index(lat, lon)

    flood_risk = get_flood_risk(precipitation)

    rodent_risk = estimate_rodent_population(
        humidity,
        vegetation,
        precipitation
    )

    risk_score = (
        humidity * 0.25 +
        precipitation * 0.20 +
        vegetation * 0.20 +
        rodent_risk * 0.25 +
        flood_risk * 0.10
    )

    risk_score = min(round(risk_score, 2), 100)

    if risk_score < 35:
        category = "LOW"

    elif risk_score < 50:
        category = "MODERATE"

    else:
        category = "HIGH"

    explanation = []

    if humidity > 70:
        explanation.append(
            "High humidity may increase rodent survival."
        )

    if vegetation > 60:
        explanation.append(
            "Dense vegetation supports rodent habitats."
        )

    if precipitation > 50:
        explanation.append(
            "Heavy rainfall may elevate environmental risk."
        )

    if flood_risk > 50:
        explanation.append(
            "Recent flood-like conditions can increase exposure risk."
        )

    return {
        "city": city,

        "coordinates": {
            "latitude": lat,
            "longitude": lon
        },

        "aqi": aqi,

        "humidity": humidity,

        "precipitation": precipitation,

        "vegetation_index": vegetation,

        "estimated_rodent_risk": rodent_risk,

        "flood_risk": flood_risk,

        "vulnerability_percentage": risk_score,

        "risk_category": category,

        "explanation": explanation
    }
