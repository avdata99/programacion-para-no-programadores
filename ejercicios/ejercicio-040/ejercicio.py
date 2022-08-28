"""
Tarea: corregir la funcion para que dado el parametro "data"
lo separe en líneas y lo transforme en una lista sin elementos vacios.
La función esta incompleta y necesita corregirse.
¿Cuál es la falla?
"""


def process_data(data):
    return data.split('\n')


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


data = """
juan
pedro
Laura
"""
f1 = process_data(data)
assert f1 == ['juan', 'pedro', 'Laura']


print('Ejercicio terminado OK')