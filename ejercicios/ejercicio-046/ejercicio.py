"""
La siguiente funcion pretende ser usada para generar
10 numeros como resultados del sorteo de quiniela.
Como podrán notar es bastante mala.
Tarea:
 - Asegurarse que los resultados sean aleatorios
 - Asegurarse que la función respete los tres parametros

"""


from random import random


def generar_quiniela(minimo=0, maximo=9999, total_numeros=10):
    """ Generar varios numeros al azar definidos
        entre máximo y minimo (sin numeros duplicados) """
    return random[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_quiniela = generar_quiniela()
print(f'Numeros resultantes {numeros_quiniela}')

# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.

# Prueba de resultados basicos
assert type(numeros_quiniela) == list
assert len(numeros_quiniela) == 10
for n in numeros_quiniela:
    assert type(n) == int
    assert n >= 0
    assert n <= 9999

# Pruebas con otros parametros
minimo = 90
maximo = 200
total_numeros = 7
numeros_quiniela = generar_quiniela(minimo=minimo, maximo=maximo, total_numeros=total_numeros)
assert type(numeros_quiniela) == list
assert len(numeros_quiniela) == total_numeros
for n in numeros_quiniela:
    assert type(n) == int
    assert n >= minimo
    assert n <= maximo

minimo = 0
maximo = 100
total_numeros = 3
numeros_quiniela = generar_quiniela(minimo=minimo, maximo=maximo, total_numeros=total_numeros)
assert type(numeros_quiniela) == list
assert len(numeros_quiniela) == total_numeros
for n in numeros_quiniela:
    assert type(n) == int
    assert n >= minimo
    assert n <= maximo

print('Ejercicio terminado OK')
