import requests

url = 'https://api.github.com/'
response = requests.get(url)
data = response.json()
print(f'Datos: {data}')

issues_url = data['issues_url']
response = requests.get(issues_url)
data = response.json()
print(f'Datos en issues_url: {data}')
