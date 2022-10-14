from random import randint, choice


f = open("random.csv", "w")
f.write('Nombre;Apellido;Edad;Pais;DNI;Tiene tarjeta;Empresa;Email\n')
nombres = [
    'Juan', 'Pedro', 'Maria', 'Jose', 'Luis',
    'Ana', 'Marta', 'Lorena', 'Sofia', 'Lucia'
]
apellidos = [
    'Perez', 'Gomez', 'Fernandez', 'Rodriguez', 'Lopez',
    'Martinez', 'Garcia', 'Sanchez', 'Diaz', 'Alvarez'
]
paises = [
    'Argentina', 'Brasil', 'Chile', 'Uruguay', 'Paraguay',
    'Bolivia', 'Peru', 'Colombia', 'Venezuela', 'Ecuador'
]
empresas = [
    'Google', 'Facebook', 'Amazon', 'Microsoft', 'Apple',
    'Tesla', 'SpaceX', 'Oracle', 'IBM', 'Intel',
    'Samsung', 'Sony', 'Nintendo', 'Sony', 'Disney',
    'Netflix', 'Spotify', 'Uber', 'Airbnb', 'Mercado Libre',
    'Walmart', 'Coca Cola', 'Pepsi', 'McDonalds', 'Burger King',
]

for r in range(200_000):
    nombre = choice(nombres)
    apellido = choice(apellidos)
    edad = randint(1, 75)
    pais = choice(paises)
    dni = randint(10_000_000, 99_999_999)
    tiene_tarjeta = choice(["Si", "No"])
    empresa = choice(empresas)
    user = f"{nombre.lower()}.{apellido.lower()}"
    dominio = f"{empresa.lower().replace(' ', '-')}.com"
    email = f"{user}@{dominio}"
    linea = f'{nombre};{apellido};{edad};{pais};{dni};{tiene_tarjeta};{empresa};{email}\n'
    f.write(linea)
    print(r, end='\r')

f.close()

# ============
# Parte 2
# Abrir el archivo, crear un diccionario solo con los datos deseados y grabarlo como JSON
# ============

import json

f = open("random.csv", "r")
f.readline()  # Saltear la primera linea
data = {}
for linea in f:
    datos = linea.strip().split(";")
    nombre = datos[0]
    apellido = datos[1]
    edad = int(datos[2])
    pais = datos[3]
    dni = int(datos[4])
    tiene_tarjeta = datos[5]
    empresa = datos[6]
    email = datos[7]

    if edad >= 18 and edad < 40 and tiene_tarjeta == "Si":
        data[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "pais": pais,
            "tiene_tarjeta": tiene_tarjeta,
            "empresa": empresa,
            "email": email
        }

f.close()
f2 = open('resultados.json', 'w')
f2.write(json.dumps(data, indent=4))
f2.close()

print(f'Se encontraton {len(data)} personas mayores de edad con tarjeta')
