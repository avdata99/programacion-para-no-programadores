"""
Tarea: completar la funcion para que dado el parametro "data"
lo separe en líneas (quitando las vacias) y lo transforme en
una lista de diccionarios cuyas llaves son los elementos (separados
por ";") de la primera fila y los valores son los datos de cada fila
(también separados por ";")

Por ejemplo, dados los datos

nombre;edad;pais
juan;22;Argentina
pedro;36;Peru
Laura;29;Chile

Se espera como resultado:
[
    {"nombre": "juan", "edad": "22", "pais": "Argentina"},
    {"nombre": "pedro", "edad": "36", "pais": "Peru"}
    {"nombre": "Laura", "edad": "29", "pais": "Chile"}
]
"""


def process_data(data):
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


data = """
nombre;edad;pais
juan;22;Argentina
pedro;36;Peru
Laura;29;Chile
"""
f1 = process_data(data)
assert f1[0]['nombre'] == 'juan'
assert f1[1]['edad'] == '36'
assert f1[2]['pais'] == 'Chile'

print('Ejercicio terminado OK')