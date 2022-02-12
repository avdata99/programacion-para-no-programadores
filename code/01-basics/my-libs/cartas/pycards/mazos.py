from random import choice
from pycards.cartas import Carta


class Mazo:
    """ Mazo general de cartas de tipo no especificado """

    def __init__(self, palos):
        self.cartas = []
        self.palos = palos
        self.cargar_cartas()

    def cargar_cartas(self):
        """ No esta definido de que tipo es, no se sabe que cartas cargar
            Forzar a las clases hijas a que implementen esta función """
        raise NotImplementedError

    def entregar_carta(self):
        """ Entregaer una carta al azar (y quitarla del mazo) """
        carta = choice(self.cartas)
        self.cartas.remove(carta)
        return carta


class MazoEspaniola(Mazo):
    """ Mazo de cartas españolas """

    def __init__(self):
        super().__init__(palos=['Oro', 'Copa', 'Espada', 'Basto'])

    def cargar_cartas(self):
        """ Crear todas las cartas de este mazo """
        
        # Agregar dos comodines
        self.cartas.append(Carta(numero=0, palo='Comodin'))
        self.cartas.append(Carta(numero=0, palo='Comodin'))

        # Agregar las cartas de cada palo
        for n in range(1, 13):
            for p in self.palos:
                self.cartas.append(Carta(numero=n, palo=p))
