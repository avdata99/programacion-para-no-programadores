"""
Tarea: corregir la función para que devuelva el resultado correcto
Por una falla, se indica siempre que ningun numero es primo
Solo UNA linea de codigo necesita corregirse
"""


def es_primo(n):
    """
    Dado un numero "n", indicar si es primo o no
    """

    # Fijarse si es divisible por los numeros inferiores a si mismo
    for div in range(n-1, 0, -1):
        if n % div == 0:
            print(f'{n} no es primo, es divisible por {div}')
            return False
    print(f'{n} sí es primo')
    return True


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


assert es_primo(7)
assert es_primo(17)
assert not es_primo(8)

print('Ejercicio terminado OK')
