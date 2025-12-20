import json
from urllib.request import urlopen, Request

# Datos de estaciones meteorológicas de Buenos Aires
url = "https://ws.smn.gob.ar/map_items/weather"
headers = {
    "Content-Type": "application/json",
    # si se quita la siguiente línea, no funciona!
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = urlopen(Request(url, headers=headers))
estaciones = json.load(response)

print("===============================================")
print(f'Total de estaciones meteorológicas: {len(estaciones)}')

for estacion in estaciones:
    nombre_estacion = estacion.get("name", "Desconocida")
    provincia = estacion.get("province", "Desconocida")
    clima = estacion.get("weather", {})
    temperatura = clima.get("temp", "N/A")
    print(f" - Estación: {nombre_estacion}, Provincia: {provincia}, Temperatura: {temperatura}°C")
