import json
import requests

ciudades = {
    "Popayán": (2.4419, -76.6063),
    "Bogotá": (4.7110, -74.0721),
    "Cali": (3.4516, -76.5320),
    "Medellín": (6.2442, -75.5812),
}

def consultar_clima(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    return requests.get(url, timeout=10).json()["current"]["temperature_2m"]

# 1. Consultar el clima de cada ciudad (con manejo de errores global)
clima_resultados = {}
for ciudad, (lat, lon) in ciudades.items():
    try:
        clima_resultados[ciudad] = consultar_clima(lat, lon)
    except Exception as e:
        print(f"[Aviso] Falló {ciudad}: {e}")

# 2. Guardar resultados en el archivo JSON
with open("clima_ciudades.json", "w", encoding="utf-8") as f:
    json.dump(clima_resultados, f, ensure_ascii=False, indent=4)

# 3. Leer el archivo y mostrar la ciudad más calurosa
with open("clima_ciudades.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

if datos:
    mas_calurosa = max(datos, key=datos.get)
    print(f"\nLa ciudad más calurosa es {mas_calurosa} con {datos[mas_calurosa]}°C")