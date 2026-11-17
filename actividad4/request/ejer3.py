import json
import requests

def consultar_clima(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"¡Aviso! Error de conexión: {e}")
        return None

# Coordenadas de Popayán
latitud = 2.4419
longitud = -76.6063

# 1. Obtener los datos usando la función
datos_clima = consultar_clima(latitud, longitud)

if datos_clima:
    # 2. Guardar la respuesta
    with open("clima.json", "w", encoding="utf-8") as f:
        json.dump(datos_clima, f, indent=4, ensure_ascii=False)
    print("guardado exitosamente.")

    # 3. Leer el archivo JSON 
    with open("clima.json", "r", encoding="utf-8") as f:
        clima_leido = json.load(f)
    
    temperatura = clima_leido["current"]["temperature_2m"]
    unidad_temp = clima_leido["current_units"]["temperature_2m"]
    
    print(f"Temperatura actual leída desde el archivo: {temperatura} {unidad_temp}")
else:
    print("No se pudo completar el proceso debido a un error en la consulta.")