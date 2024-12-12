"""
Completar la funcion para que devuelva "Hola NOMBRE"
segun el "nombre" (string) que se pasa como parametro.
"""


def hola(nombre):
    return (f'Hola {nombre}')
    

# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.

assert hola("Juan") == "Hola Juan"
assert hola("Pedro") == "Hola Pedro"

print('Ejercicio terminado OK')
