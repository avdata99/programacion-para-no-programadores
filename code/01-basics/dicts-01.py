
data = {
    'edad': 32,
    'nombre': 'Juan',
    'educacion': {
        'secundario': 'Monserrat',
        'universidad': 'UNC',
    }
}

nombre = data['nombre']
edad = data['edad']
universidad = data['educacion']['universidad']

print(f'Nombre: {nombre}, edad {edad} años. Universidad: {universidad}')
# Nombre: Juan, edad 32 años. Universidad: UNC

# Agregarle datos
data['ocupacion'] = 'Desarrollador'
data['educacion']['primario'] = 'San Juan'

print(data)
# {'edad': 32, 'nombre': 'Juan', 'educacion': {'secundario': 'Monserrat', 'universidad': 'UNC', 'primario': 'San Juan'}, 'ocupacion': 'Desarrollador'}
