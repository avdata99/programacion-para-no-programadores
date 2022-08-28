"""
La funcion "sumarial" devuelve la suma de todos los
numeros iguales o menores a un numero "n" dado.
Esta función es correcta, no tiene errores.
Nota: esta funcion solo trabaja con números positivos.
Por ejemplo:
 - sumarial(3) es igual a 6 (1 + 2 + 3)
 - sumarial(7) es igual a 28 (1 + 2 + 3 + 4 + 5 + 6 + 7)

Tarea: Agregar la funcion "sumarial_impar" parecida a "sumarial"
pero que solo se sumen los numeros imapres, ignorar todos los
pares en este proceso.

De esta forma:
 - sumarial_impar(3) deberá ser igual a 4 (1 + 3)
 - sumarial_impar(7) deberá ser igual a 16 (1 + 3 + 5 + 7)
 - sumarial_impar(8) deberá ser igual a 16 (1 + 3 + 5 + 7)
"""

def sumarial(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumarial(n-1)


def sumarial_impar(n):
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


assert sumarial(3) == 6
assert sumarial(7) == 28
assert sumarial_impar(3) == 4
assert sumarial_impar(7) == 16
assert sumarial_impar(8) == 16

print('Ejercicio terminado OK')
