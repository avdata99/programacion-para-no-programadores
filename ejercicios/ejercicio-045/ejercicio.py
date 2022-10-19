"""
La funcion "carta_poker_al_azar" ya funciona como es esperado
La tarea aquí es completar la funcion "carta_espaniola_al_azar"
para que devuleva resultados válidos.
Nota: se debe importar y usar la funcion "randint" de "random"
"""

from random import choice

def carta_poker_al_azar():
    palos = ['pica', 'trebol', 'corazon', 'diamante']
    numeros = list(range(1, 11)) + ['J', 'Q', 'K']
    nro = choice(numeros)
    palo = choice(palos)

    carta = {"numero": nro, "palo": palo}
    return carta

def carta_espaniola_al_azar():
    palos = ['oro', 'basto', 'espada', 'copa']
    numeros= range(1,13)
    # corregir estas dos lineas para devolver valores válidos
    nro = choice(numeros)
    palo = choice(palos)

    carta = {"numero": nro, "palo": palo}
    return carta

# mirar ejemplos de ambas funciones
for n in range(20):
    carta1 = carta_poker_al_azar()
    carta2 = carta_espaniola_al_azar()
    print(carta1, carta2)


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.

carta = carta_espaniola_al_azar()
assert type(carta['numero']) == int
assert carta['numero'] > 0
assert carta['numero'] <= 12
assert carta['palo'] in ['oro', 'basto', 'espada', 'copa']

print('Ejercicio terminado OK')
