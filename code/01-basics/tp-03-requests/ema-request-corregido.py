from bs4 import BeautifulSoup  # pip install bs4
from time import sleep
import csv
import os
import requests


# URL con la pagina pendiente de carga para paginar
url = 'http://volta.net.ar/registro?gd=&categoria=&nombre=&cuil=&registro=&localidad=CORDOBA&page={npage}'

# Agregar headers al request para que parezca hecho por un humano
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
}

# preparar un archivo CSV para guardar los datos
final_csv_file = open('final.csv', 'w', encoding='utf-8')
fieldnames = ['nro', 'cuil', 'nombre', 'categoria', 'registro',
              'localidad', 'barrio', 'contacto']
writer = csv.DictWriter(final_csv_file, fieldnames=fieldnames)
writer.writeheader()

# son 201 páginas
for page in range(1, 202):
    paginated_url = url.format(npage=page)
    print(f'Revisando {paginated_url}')

    # para evitar que cada ejecucion haga 200 request a la página,
    # grabamos los HTMLs localmente y los usamos cuando sea necesario
    # solo hacemos el request si no está descargado el HTML
    html_file = f'pagina-{page}.html'
    if not os.path.exists(html_file):
        print(f' - Descargando {paginated_url}')
        response = requests.get(paginated_url, headers=headers)
        f = open(html_file, 'w', encoding='utf-8')
        f.write(response.text)
        f.close()

    # abrimos el archivo local que ya está descargado
    f = open(html_file, 'r', encoding='utf-8')
    texto_pagina = f.read()
    f.close()

    soup = BeautifulSoup(texto_pagina, 'html.parser')

    # ejemplo de como ver las clases de todas las tablas del HTML
    # Sirve para ver que elementos están en el HTML y BS4 ve
    # for table in soup.find_all('table'):
    #     print(table.get('class'))

    # la pagina tiene una tabla con ID
    # eso simplifica ubiucarla
    tabla_id = 'tblResultados'
    table = soup.find('table', id=tabla_id)
    for row in table.tbody.find_all('tr'):
        # mirar los rows (filas) de la tabla 
        # print(row)
        tds = row.find_all('td')
        """ Ejemplo de celdas (td) de la fila 
            #	CUIL	Nombre	Categoría	Registro	Localidad	Barrio	Contacto
            1	20338305851	AGUSTIN ANDRES DE LA COLINA	PROFESIONAL	5325/x	CORDOBA	GRANJA DE FUNES	 03543-423885
            157-913035
            agus_dlc5@hotmail.com
            """
        matriculado = {
            'nro': tds[0].text,
            'cuil': tds[1].text,
            'nombre': tds[2].text,
            'categoria': tds[3].text,
            'registro': tds[4].text,
            'localidad': tds[5].text,
            'barrio': tds[6].text,
            'contacto': tds[7].text,
        }
        writer.writerow(matriculado)
    sleep(1)