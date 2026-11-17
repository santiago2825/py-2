import requests
url = "https://api.open-meteo.com/v1/forecast"

parametros= {
    "latitude": 2.4419,
    "longitude": -76.6063,
    "current": "temperature_2m,wind_speed_10m"
}

response = requests.get(url, params=parametros)
data = response.json()

temp = data["current"]["temperature_2m"]
temp_unidad = data["current_units"]["temperature_2m"]

viento = data["current"]["wind_speed_10m"]
viento_unidad = data["current_units"]["wind_speed_10m"]

print(f"Temperatura actual: {temp} {temp_unidad}")
print(f"Velocidad del viento actual: {viento} {viento_unidad}")