"""
La siguiente funcion busca contar cuantas veces se repite cada palabra.
Por ejemplo de "Hola Juan. Hola Pedro" devuelve {"Hola": 2, "Juan.": 1, "Pedro": 1}
Tarea: Corregir el error de la función para que devuelva el resultado correcto.
Se espera que los signos de puntuacion no afecten el resultado y que las mayusculas
y minusculas no cuenten como palabras diferentes.
"""


def contar_palabras(frase):
    """ 
    Esta funcion toma una frase y devuelve un diccionario
    con una llave por cada palabra y un valor igual a la
    cantidad de veces que aparece en la frase
    """
    palabras = frase.split()
    resultados = {}
    for palabra in palabras:
        if palabra in resultados.keys():
            # si existe, sumarle 1
            resultados[palabra] += 1
        else:
            # si no existe, inicializarla
            resultados[palabra] = 0
    return resultados


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


f1 = contar_palabras("Hola dijo Juan. Hola dijo pedro")
assert f1['Hola'] == 2

himno = "Oid mortales el grito sagrado. Libertad, libertad, libertad. Oid el ruido de rotas cadenas"
palabras_himno = contar_palabras(himno)
assert palabras_himno['Oid'] == 2
assert palabras_himno['libertad'] == 3

print('Ejercicio terminado OK')
