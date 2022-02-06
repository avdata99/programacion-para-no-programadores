import os
import random


class Celda:
    def __init__(self, char=' '):
        self.char = char

class Mundo:
    def __init__(self, ancho=30, alto=15):
        self.ancho = ancho
        self.alto = alto
        self.celdas = []
        for x in range(alto):
            self.celdas.append([])
            for y in range(ancho):
                self.celdas[x].append(Celda())

    def show(self):
        
        os.system('cls||clear')

        for x in range(self.alto):
            print()
            for y in range(self.ancho):
                print(self.celdas[x][y].char, end=' | ')
        print()
        print()

m = Mundo()
m.show()
