from bs4 import BeautifulSoup  # pip install bs4
from time import sleep
import requests


url = 'https://www.promiedos.com.ar/club={}'

for n in range(2, 40):
    response = requests.get(url.format(n))
    soup = BeautifulSoup(response.text, 'html.parser')
    club = soup.find('title').text
    club = club.replace(' - Fixture, Titulos y Plantel en Promiedos', '')
    club = club.replace('\n', '')
    club = club.replace('\r', '')
    
    print(f'Club {n} - {club}')
    sleep(2)

""" 

...

Club 32 - Ind Rivadavia
Club 33 - Instituto
Club 34 - Patronato
Club 35 - Rosario Central
Club 36 - San Martin (SJ)
Club 37 - San Martin (T)

...

"""