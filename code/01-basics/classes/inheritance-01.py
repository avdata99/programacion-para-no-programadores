from random import choice

opciones = ["piedra", "papel", "tijeras"]

class PiedraPapelTijerasPlayer:
    jugados = 0
    ganados = 0
    empatados = 0
    perdidos = 0

    def name(self):
        raise NotImplementedError("Debe darle un nombre")

    def move(self):
        raise NotImplementedError("Debe implementar el metodo move")

class AzarPlayer(PiedraPapelTijerasPlayer):

    def name(self):
        return "Azar"
    def move(self):
        return choice(opciones)

class PiedraPlayer(PiedraPapelTijerasPlayer):

    def name(self):
        return "Piedra"
    def move(self):
        return "piedra"

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

def competir(jugador1, jugador2):
    """ Los jugadores deben ser alguna clase heredada de PiedraPapelTijerasPlayer """
    if not isinstance(jugador1, PiedraPapelTijerasPlayer):
        raise TypeError("jugador1 debe ser una instancia de PiedraPapelTijerasPlayer")
    if not isinstance(jugador2, PiedraPapelTijerasPlayer):
        raise TypeError("jugador2 debe ser una instancia de PiedraPapelTijerasPlayer")

def competir(jugador1, jugador2):
    for rondas in range(100):
        opcion_elegida1 = jugador1.move()
        opcion_elegida2 = jugador2.move()

        resultado = ganador(opcion_elegida1, opcion_elegida2)
        if resultado == 0:
            jugador1.empatados += 1
            jugador2.empatados += 1
        elif resultado == 1:
            jugador1.ganados += 1
            jugador2.perdidos += 1
        elif resultado == 2:
            jugador1.perdidos += 1
            jugador2.ganados += 1
        
    print(f"Gana Jugador {jugador1.name()}: {jugador1.ganados} - Gana Jugador {jugador2.name()}: {jugador2.ganados} - Empates: {jugador1.empatados}")
    
competir(jugador1=AzarPlayer(), jugador2=PiedraPlayer())
