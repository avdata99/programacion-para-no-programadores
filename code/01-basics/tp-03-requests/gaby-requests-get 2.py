# Tarea de requests, .get, traer informacion de pagina web

import requests
from requests import get

url ='https://www.makro.com.ar/'

response = ("resp")

response = requests.get(url)

datos = response.text
print(f'Primeros caracteres de la respuesta {datos[:15]}')
for d in response:
    print(d)
