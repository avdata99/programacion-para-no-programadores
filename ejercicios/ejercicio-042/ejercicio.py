"""

La funcion "crear_mazo_cartas_poker" esta incompleta y necesita ser completada para
devolver una lista de diccionarios con todas las cartas disponibles en un mazo de poker.

Nota: El ejercicio 041* ya muestra una función similar que puede usarse como ayuda

* https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-041/ejercicio.py

"""


def crear_mazo_cartas_poker():
    palos = ['pica', 'trebol', 'corazon', 'diamante']
    mazo = []

    # COMPLETAR la lista con un diccionario por cada carta de
    # la forma {'numero': X, 'palo': Y}
    # El test de la parte inferior de este archivo ayuda a validar
    # el resultado esperado

    return mazo

# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.

mazo_esp = crear_mazo_cartas_poker()

assert {'numero': 9, 'palo': 'pica'} in mazo_esp
assert {'numero': 10, 'palo': 'pica'} in mazo_esp
assert {'numero': 'J', 'palo': 'pica'} in mazo_esp
assert {'numero': 'Q', 'palo': 'pica'} in mazo_esp
assert {'numero': 'K', 'palo': 'pica'} in mazo_esp

assert {'numero': 9, 'palo': 'diamante'} in mazo_esp
assert {'numero': 10, 'palo': 'diamante'} in mazo_esp
assert {'numero': 'J', 'palo': 'diamante'} in mazo_esp
assert {'numero': 'Q', 'palo': 'diamante'} in mazo_esp
assert {'numero': 'K', 'palo': 'diamante'} in mazo_esp

print('Ejercicio terminado OK')
