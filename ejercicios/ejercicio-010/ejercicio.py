"""
Completar la funcion para que devuelva la tercera
letra de la "palabra" (string) que se pasa como parametro.
"""


def tercera_letra(palabra):
    return palabra[2] 


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


assert tercera_letra("hola") == "l"
assert tercera_letra("Es facil") == " "
assert tercera_letra("341A") == "1"

print('Ejercicio terminado OK')