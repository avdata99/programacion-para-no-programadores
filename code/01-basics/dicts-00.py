data = {
    'edad': 32,
    'nombre': 'Juan'
}

nombre = data['nombre']  # equivalente a data.get('nombre)
edad = data['edad']
print(f'Nombre: {nombre}, edad {edad} años')

"""
data['algo-que-no-existe']
# genera un error 
# KeyError: 'algo-que-no-existe'
# mientras que 
data.get('algo-que-no-existe')
devuelve None
"""

# Nombre: Juan, edad 32 años

for k, v in data.items():
    print(f'Item encontrado: Key:{k}, Value: {v}')

# Item encontrado: Key:edad, Value: 32
# Item encontrado: Key:nombre, Value: Juan
