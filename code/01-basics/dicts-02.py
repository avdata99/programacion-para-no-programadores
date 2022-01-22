# lista de diccionarios
data = {
    'personas': [
        {'nombre': 'Juan', 'edad': 20},
        {'nombre': 'Pedro', 'edad': 30},
        {'nombre': 'María', 'edad': 40},
    ]
}

print('PERSONAS:')
for persona in data['personas']:
    nombre = persona['nombre']
    edad = persona['edad']
    print(f' - Nombre: {nombre}, edad {edad} años')

""" resultados

PERSONAS:
 - Nombre: Juan, edad 20 años
 - Nombre: Pedro, edad 30 años
 - Nombre: María, edad 40 años

"""