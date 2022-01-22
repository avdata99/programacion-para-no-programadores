import requests

url = 'https://cordobus.apps.cordoba.gob.ar/tracking/api/internos-activos-ahora/'
response = requests.get(url)

data = response.json()
print(f'Hay {data["count"]} bondis en circulación en la ciudad de Córdoba')

bondis = data['results']['features']

bondis_mas_rapido = None

for bondi in bondis:
    """ data sample
        {
            'id': 1359,
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [-64.263954, -31.433514]
            },
            'properties': {
                'nombre': '3871',
                'linea': '42',
                'ultima_posicion_time': '2022-01-21T21:16:47-03:00',
                'recorrido_actual': 1088,
                'recorrido_nombre': 'eba42',
                'ultimas_velocidades_promedio': '49.00',
                'ultimas_variaciones_latitud': '0.00684400',
                'ultimas_variaciones_longitud': '0.00009100',
                'adaptado': False,
                'piso_bajo': False,
                'articulado': False,
                'empresa': 2,
                'color': '#ff0000'
            }
        }
        """

    if bondis_mas_rapido is None:
        bondis_mas_rapido = bondi
    else:
        if float(bondi['properties']['ultimas_velocidades_promedio']) > float(bondis_mas_rapido['properties']['ultimas_velocidades_promedio']):
            bondis_mas_rapido = bondi

maxima_velocidad = float(bondis_mas_rapido['properties']['ultimas_velocidades_promedio'])
print(f'El bondi más rápido ahora va a {maxima_velocidad} km/h')
