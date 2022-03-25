# Tarea de requests, .get, traer informacion de pagina web
from urllib import response
import requests
from requests import get

url = "https://www.smn.gob.ar"
response = ("resp")

response = requests.get(url)

resp = response.text
for d in response:
    print(d)
    print("********************************")
