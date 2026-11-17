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
        print(f"error en el servidor {e}")
        return None

# Prueba
resultado = consultar_clima(2.4419, -76.6063)
if resultado:
    print("Conexión exitosa.")
    #mostramos los datos
    temp = resultado["current"]["temperature_2m"]
    t_unidad = resultado["current_units"]["temperature_2m"]
    
    viento = resultado["current"]["wind_speed_10m"]
    v_unidad = resultado["current_units"]["wind_speed_10m"]
    
    print(f"Temperatura actual: {temp} {t_unidad}")
    print(f"Velocidad del viento: {viento} {v_unidad}")