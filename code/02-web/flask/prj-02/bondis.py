import requests


def get_bondis_info():
    """ obtener informacion de los colectivos de la ciudad de Córdoba """
    url = 'https://cordobus.apps.cordoba.gob.ar/tracking/api/internos-activos-ahora/'
    response = requests.get(url)

    data = response.json()
    activos = data["count"]

    bondis = data['results']['features']
    bondis_mas_rapido = None
    adaptados = 0
    for bondi in bondis:
        if bondi['properties']['adaptado']:
            adaptados += 1
        if bondis_mas_rapido is None:
            bondis_mas_rapido = bondi
        else:
            if float(bondi['properties']['ultimas_velocidades_promedio']) > float(bondis_mas_rapido['properties']['ultimas_velocidades_promedio']):
                bondis_mas_rapido = bondi

    maxima_velocidad = float(bondis_mas_rapido['properties']['ultimas_velocidades_promedio'])
    
    results = {
        'bondis_activos': activos,
        'bondi_mas_rapido': maxima_velocidad,
        'adaptados': adaptados,
    }

    return results
