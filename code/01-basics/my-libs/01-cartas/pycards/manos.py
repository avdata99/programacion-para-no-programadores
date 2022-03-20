""" 
Manos
"""

from pycards.cartas import Carta


class Mano:
    """ Una mano de cartas de cualquier juego """
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, otro):
        """ Agregar una carta (no puede agregarse otra cosa) a la mano
            Las manos de juegos específicos deberán validar la cantidad de cartas u otros detalles """
        if type(otro) != Carta:
            raise ValueError('Solo se le pueden sumar Cartas')
        self.cartas.append(otro)

    def __add__(self, otro):
        """ La funcion suma es agregar una carta a esta mano
            """
        self.agregar_carta(otro)
        return self
