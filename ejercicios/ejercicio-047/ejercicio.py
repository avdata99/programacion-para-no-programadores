"""
La funcion "detectar_escaleras" funciona bastante bien.
Toma una lista de numeros y busca escaleras ascendentes
dentro de la secuencia de numeros.
Esta funcion detecta casi todas las secuencias pero no todas
Tarea:
 - Arreglar la funcion para que pase los tests y encuentre
   todas las escaleras existentes
Nota: probablemente vas a necesitar depurar el código para
entender como funciona y por que falla.
"""

from random import randint

def tirar_dados(lados=6, veces=100):
    """ Generar aleatoriamente los tiros de un lado de cantidad
        de lados variable.
    """
    
    tiros = []
    for _ in range(veces):
        numero = randint(1, lados)
        tiros.append(numero)
    
    return tiros

def detectar_escaleras(lista_tiros):
    """ Detectar las escaleras ascendentes encontradas
        en los tiros de al menos 3 elementos """
    
    # aqui guardamos las escaleras que se consiguieron con 3 o más elementos
    escaleras_buenas = []
    # lista temporal para ir testeando todos los tiros
    escalera = []
    for tiro in lista_tiros:
        if len(escalera) == 0:
            # recien empiezo a buscar
            escalera.append(tiro)
        elif escalera[-1] == tiro - 1:
            # La escalera de prueba ya empezo y el numero actual
            # esta en escalera con el ultimo encontrado
            escalera.append(tiro)
        else:
            # este tiro no esta en escalera con el anterior
            # ver si la escalera conseguida tiene 3 o mas elementos
            # para guardarle
            if len(escalera) >= 3:
                escaleras_buenas.append(escalera)
            # como este número no sirve para la escalera anterior
            # es el que inicializa la deteccion de la nueva
            escalera = [tiro]

    return escaleras_buenas


tiros = tirar_dados(veces=10000)
escaleras = detectar_escaleras(tiros)
print(f'Escaleras encontradas {len(escaleras)}')


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.

# Probar tiros donde yo ya conozco los resultados
tiros_test = [1, 5, 2, 3, 2, 1, 4, 5, 5, 1, 2, 6, 3, 3, 3, 1, 2, 5, 5, 2, 4,
              3, 4, 5,
              2, 3, 4, 5,
              1, 5, 2, 4, 2, 5, 6, 6, 5, 5, 4, 2, 6, 1, 4, 5, 3, 1, 6, 2, 2,
              1, 2, 3, 4, 5,
              3, 1, 2, 6, 5, 6, 2, 5, 1, 4, 4, 5, 4, 3, 2, 1, 1, 3, 5, 6, 1,
              1, 2, 3]

escaleras = detectar_escaleras(tiros_test)
assert escaleras == [
    [3, 4, 5],
    [2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3]
]

tiros_test = [1, 2, 3]
escaleras = detectar_escaleras(tiros_test)
assert escaleras == [[1, 2, 3]]

print('Ejercicio terminado OK')
