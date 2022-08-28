"""
**************************
**************************
Este archivo contiene un generador infinito. Si lo ejecutas antes
de resolver la tarea tu computador podría clavarse.
**************************
**************************
Tarea: Agregar un parámetro opcional a la función "generador_de_primos"
para que tenga un limite de respuestas devueltas igual a 10.
"""


def es_primo(n):
    """
    Dado un numero "n", indicar si es primo o no
    """

    # Fijarse si es divisible por los numeros inferiores a si mismo
    for div in range(2, n):
        if n % div == 0:
            return False
    return True


def generador_de_primos(desde=1):
    """ Generador de nuemeros primos """
    while True:
        if es_primo(desde):
            yield desde
        desde += 1


print('Generando numeros primos a partir de 200')
c = 1
for n in generador_de_primos(200):
    print(f' {c}°: {n}')
    c += 1
    if c > 10:
        break


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


# Probar el parametro opcional predeterminado
diez_desde_200 = [211, 223, 227, 229, 233, 239, 241, 251, 257, 263]
diez_desde_200_fn = list(generador_de_primos(200))
assert diez_desde_200_fn == diez_desde_200, f"{diez_desde_200_fn} != {diez_desde_200}"

# Probar el parametro opcional definido
cinco_desde_300 = [307, 311, 313, 317, 331] 
cinco_desde_300_fn = list(generador_de_primos(300, 5))
assert cinco_desde_300_fn == cinco_desde_300, f"{cinco_desde_300_fn} != {cinco_desde_300}"

print('Ejercicio terminado OK')
