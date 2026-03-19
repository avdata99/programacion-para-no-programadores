"""
La siguiente funcion toma como parámetro una lista de diccionarios
y cuenta la cantidad de elementos que tiene un valor especifico en
una propiedad definida.
Por ejemplo de la lista
lista = [
    {"genero": "M", "nombre": "Juan"},
    {"genero": "F", "nombre": "Pablo"},
    {"genero": "F", "nombre": "Juana", "apellido": "Gomez"},
    {"genero": "M", "nombre": "Victor"},
    {"genero": "M", "nombre": "Juan Pablo", "apellido": "Velez"},
    {"genero": "F", "nombre": "Juana"},
    {"genero": "F", "nombre": "Victoria"}
]
Se esperan estos posibles resultados

contar_si(lista, "genero", "M") == 3
contar_si(lista, "genero", "F") == 4
contar_si(lista, "nombre", "Juana") == 2

pero la funcion da error en algunos casos como
contar_si(lista, "apellido", "Gomez")
donde en realidad esperamos que devuelva 1

Tarea: Mejorar la función para que no de errores cuando una clave no existe
"""


def contar_si(lista, propiedad, valor):
    """ 
    Esta funcion cuenta la cantidad de elementos (diccionarios) en "lista"
    que tiene una "propiedad" con un "valor" específico.
    """
    contador = 0
    for elemento in lista:
        if elemento[propiedad] == valor:
            contador += 1

    return contador

# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


lista = [
    {"genero": "M", "nombre": "Juan", "apellido": None},
    {"genero": "F", "nombre": "Pablo", "apellido": None},
    {"genero": "F", "nombre": "Juana", "apellido": "Gomez"},
    {"genero": "M", "nombre": "Victor", "apellido":None},
    {"genero": "M", "nombre": "Juan Pablo", "apellido": "Velez"},
    {"genero": "F", "nombre": "Juana", "apellido": None},
    {"genero": "F", "nombre": "Victoria", "apellido": None}
]

assert contar_si(lista, "genero", "M") == 3
assert contar_si(lista, "genero", "F") == 4
assert contar_si(lista, "nombre", "Juana") == 2
assert contar_si(lista, "apellido", "Gomez") == 1
assert contar_si(lista, "apellido", "Perez") == 0

print('Ejercicio terminado OK')
