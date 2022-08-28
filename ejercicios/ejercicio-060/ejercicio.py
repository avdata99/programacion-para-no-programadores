"""
Tarea: escribir la función "devolver_mayor_par" para que
devuelva el mayor numero par de la "lista" pasada como parámetro
"""


def es_par(n):
    """
    Dado un numero "n", indicar si es par (mayor a cero) o no
    """
    return n > 0 and n % 2 == 0


def devolver_mayor_par(lista):
    pass


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


assert devolver_mayor_par([-1, 3, 6, 9]) == 6
assert devolver_mayor_par([21, 34, -6, 9]) == 34

print('Ejercicio terminado OK')
