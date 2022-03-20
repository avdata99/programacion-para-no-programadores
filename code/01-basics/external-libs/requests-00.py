import requests

url = 'https://mendiolaza.gob.ar/'
response = requests.get(url)
codigo = response.text

print(f'Codigo de estado de la respuesta para {url}: {response.status_code}')
print(f'Primeros caracteres de la respuesta {codigo[:180]}')

# grabar el HTML resultante a disco
f = open('web.html', 'w')
f.write(codigo)
f.close()
