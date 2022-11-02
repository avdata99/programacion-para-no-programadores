# traer del paquete random las funciones randint y choice
# randint genera un número aleatorio entre dos valores
# choice elige un elemento al azar de una lista
from random import randint, choice


f = open("random.csv", "w")
f.write('Nombre;Segundo nombre;Apellido;Edad;Pais;DNI;Tiene tarjeta;Empresa;Email\n')
# Tarea, asegurarse que los nombres sean masculinos o femeninos
nombres = [
    'Juan', 'Pedro', 'Maria', 'Jose', 'Luis',
    'Ana', 'Marta', 'Lorena', 'Sofia', 'Lucia',
     'Juana', 'Felipe', 'Mariela', 'Nelson'
]
apellidos = [
    'Perez', 'Gomez', 'Fernandez', 'Rodriguez', 'Lopez',
    'Martinez', 'Garcia', 'Sanchez', 'Diaz', 'Alvarez', 
    'Dominguez', 'Roldan', 'Gonzalez', 'Torres'
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
feme = []
masc = []
for fem in nombres:
    fe= fem[-1]
    if fe == "a":
       feme.append(fem)
for m in nombres:
    ma = m[-1]
    if ma == "o, s, n, e":

       masc.append(nombres)   
for r in range(200_000):
    nombre = choice(feme or masc)
    segundo_nombre = choice(feme or masc)
    apellido = choice(apellidos)
    edad = randint(1, 75)
    pais = choice(paises)
    dni = randint(10_000_000, 99_999_999)
    tiene_tarjeta = choice(["Si", "No"])
    empresa = choice(empresas)
    user = f"{nombre.lower()}.{segundo_nombre.lower()}.{apellido.lower()}"
    dominio = f"{empresa.lower().replace(' ', '-')}.com"
    email = f"{user}@{dominio}"
    linea = f'{nombre};{segundo_nombre};{apellido};{edad};{pais};{dni};{tiene_tarjeta};{empresa};{email}\n'
    f.write(linea)
    
    # tarea, imprimir el % de avance en lugar del numero de fila
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
duplicados = []
for linea in f:
    datos = linea.strip().split(";")
    nombre = datos[0]
    segundo_nombre = datos[1]
    apellido = datos[2]
    edad = int(datos[3])
    pais = datos[4]
    dni = int(datos[5])
    tiene_tarjeta = datos[6]
    empresa = datos[7]
    email = datos[8]

    if edad >= 18 and edad < 40 and tiene_tarjeta == "Si":
        key = dni
        if dni in data.keys():
            duplicados.append(dni)
            print(f'Duplicados encontrado {dni}')
            c = 1
            while True:
                c += 1
                key = f'{dni}-{c}'
                if key not in data.keys():
                    break
                
        
        data[key] = {
            "nombre": nombre,
            "segundo_nombre": segundo_nombre,
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
print(data)

print(f'Se encontraton {len(data)} personas mayores de edad con tarjeta')