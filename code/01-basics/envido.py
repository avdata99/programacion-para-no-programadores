"""
La funcion envido, dada una lista de (estrictamente) tres cartas,
me devuelve el envido de esa mano de truco.
Cada elemento de la lista es de la forma:
    carta = {'palo': 'xxx', 'numero': N}
"""


def carta_simple_envido(carta):
    """ de una carta data obtiene cuanto suma al envido
        De un 2 devuelve 2, de un 10 cero y de un 7, devuelve 7"""
    return carta['numero'] if carta['numero'] < 10 else 0

def envido_dos_cartas(carta1, carta2):
    """ Aqui las dos cartas finales se suman luego de detectar palos iguales """
    return 20 + carta_simple_envido(carta1) + carta_simple_envido(carta2)

def envido(cartas):
    """ Calcular el envido dadas 3 cartas """
    # Asegurarse que tiene 3 cartas
    if len(cartas) != 3:
        raise Exception('Se requieren 3 cartas')

    # ###############################################    
    # ver todos los envidos posibles y elegir el mejor
    # ###############################################

    # aun si las tres cartas fueran de distinto palo, 
    #   la carta que sea mayor de ellas sería un envido posible
    envidos = [
        max([carta_simple_envido(carta) for carta in cartas])
    ]

    # ver ahora los envidos formados por dos cartas del mismo palo
    palos = [carta['palo'] for carta in cartas]
    # Si hay otros envidos ponerlos en la lista para ver cual es el mejor
    if palos[0] == palos[1]:
        envidos.append(envido_dos_cartas(cartas[0], cartas[1]))
    if palos[0] == palos[2]:
        envidos.append(envido_dos_cartas(cartas[0], cartas[2]))
    if palos[1] == palos[2]:
        envidos.append(envido_dos_cartas(cartas[1], cartas[2]))

    # devolver el mas alto de todos
    return max(envidos)

assert 33 == envido([{'palo': 'A', 'numero':  7}, {'palo': 'A', 'numero':  1}, {'palo': 'A', 'numero':  6}])
assert  6 == envido([{'palo': 'A', 'numero':  4}, {'palo': 'B', 'numero':  1}, {'palo': 'C', 'numero':  6}])
assert  0 == envido([{'palo': 'A', 'numero': 10}, {'palo': 'B', 'numero': 10}, {'palo': 'C', 'numero': 10}])
assert 24 == envido([{'palo': 'A', 'numero': 10}, {'palo': 'A', 'numero':  4}, {'palo': 'C', 'numero':  7}])
assert 27 == envido([{'palo': 'A', 'numero': 11}, {'palo': 'C', 'numero': 10}, {'palo': 'C', 'numero':  7}])
assert 20 == envido([{'palo': 'A', 'numero': 11}, {'palo': 'C', 'numero': 10}, {'palo': 'A', 'numero': 12}])

print('Todo OK')
