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
    
    def competir(self, oponente):
        """ ver si mi movida es mejor que la del oponente """
        op1 = self.move()  # opcion_mia
        op2 = oponente.move()  # opcion_oponente

        if op1 == op2: resultado = 0
        elif (op1, op2) == ("piedra", "tijeras"): resultado = 1
        elif (op1, op2) == ("piedra", "papel"): resultado = 2
        elif (op1, op2) == ("tijeras", "piedra"): resultado = 2
        elif (op1, op2) == ("tijeras", "papel"): resultado = 1
        elif (op1, op2) == ("papel", "tijeras"): resultado = 2
        elif (op1, op2) == ("papel", "piedra"): resultado = 1

        elif (op2, op1) == ("piedra", "papel"): resultado = 1
        elif (op2, op1) == ("tijeras", "piedra"): resultado = 1
        elif (op2, op1) == ("tijeras", "papel"): resultado = 2
        elif (op2, op1) == ("papel", "tijeras"): resultado = 1
        elif (op2, op1) == ("papel", "piedra"): resultado = 2
        
        else:
            raise ValueError(f"No se puede determinar ganador entre {op1} y {op2}")

        if resultado == 0:
            self.empatados += 1
            oponente.empatados += 1
        elif resultado == 1:
            self.ganados += 1
            oponente.perdidos += 1
        elif resultado == 2:
            self.perdidos += 1
            oponente.ganados += 1
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
