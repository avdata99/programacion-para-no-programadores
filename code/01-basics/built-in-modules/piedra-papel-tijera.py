# dos jugadores aleatorios compitiendo

from random import choice

opciones = ["piedra", "papel", "tijeras"]

def ganador(op1, op2):
    """ devuelve 0 en empate, 1 si gana op1 y 2 si gana op2 """
    if op1 == op2:
        return 0
    if   (op1, op2) == ("piedra", "tijeras"): return 1
    elif (op1, op2) == ("piedra", "papel"): return 2
    elif (op1, op2) == ("tijeras", "piedra"): return 2
    elif (op1, op2) == ("tijeras", "papel"): return 1
    elif (op1, op2) == ("papel", "tijeras"): return 2
    elif (op1, op2) == ("papel", "piedra"): return 1

    elif (op2, op1) == ("piedra", "papel"): return 1
    elif (op2, op1) == ("tijeras", "piedra"): return 1
    elif (op2, op1) == ("tijeras", "papel"): return 2
    elif (op2, op1) == ("papel", "tijeras"): return 1
    elif (op2, op1) == ("papel", "piedra"): return 2
    
    else:
        raise ValueError(f"No se puede determinar ganador entre {op1} y {op2}")

puntos_jugador_1 = 0
puntos_jugador_2 = 0
empates = 0
for rondas in range(100):
    opcion_elegida1 = choice(opciones)
    opcion_elegida2 = choice(opciones)
    print(f"Jugador 1: {opcion_elegida1} - Jugador 2: {opcion_elegida2}: ", end="")
    resultado = ganador(opcion_elegida1, opcion_elegida2)
    if resultado == 0:
        print("empate")
        empates += 1
    elif resultado == 1:
        print("Gana 1")
        puntos_jugador_1 += 1
    elif resultado == 2:
        print("Gana 2")
        puntos_jugador_2 += 1
    
print(f"Gana Jugador 1: {puntos_jugador_1} - Gana Jugador 2: {puntos_jugador_2} - Empates: {empates}")
