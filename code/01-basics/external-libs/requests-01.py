import requests

# -----------------------------------------------
# Probar con pagina que no existe

url = 'https://pagina-que-no-existe.com'
try:
    response = requests.get(url)
except Exception as e:
    print(f'Error consultando {url}:\n\t{e}')
    quit()

print(f'Codigo de estado de la respuesta para {url}: {response.status_code}')
