from bs4 import BeautifulSoup  # pip install bs4
import requests
import re

url = 'http://volta.net.ar/registro?gd=&categoria=&nombre=&cuil=&registro=&localidad=CORDOBA'

"""
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
resultado = soup.find_all("tr", class_="danger")
resultado = soup.get_text()
print(resultado)
"""

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for tag in soup.find_all(re.compile("^td")):
    print(tag)
