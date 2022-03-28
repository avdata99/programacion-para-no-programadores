""" 
Manos
"""

from pycards.manos import Mano


class ManoTruco(Mano):
    """ Una mano en el juego de truco """

    def agregar_carta(self, carta):
        """ Solo para llamar internalemte """
        if len(self.cartas) >= 3:
            raise ValueError('Una mano de truco no puede tener mas de tres cartas')
        super().agregar_carta(carta)

    def _validate_mano_completa(self):
        """ Completa = tengo 3 cartas.
            Esta funcion da error si la mano no esta completa """
        if not len(self.cartas) == 3:
            raise ValueError('Mano incompleta')

    def _carta_cuenta_envido(self, carta):
        """ de una carta data obtiene cuanto suma al envido
            De un 12 devuelve 2, de un 10 cero y de un 7, devuelve 7"""
        return carta.numero if carta.numero < 10 else 0

    def _sumar_envido(self, carta1, carta2):
        """ Aqui las dos cartas finales se suman luego de detectar palos iguales """
        return 20 + self._carta_cuenta_envido(carta1) + self._carta_cuenta_envido(carta2)

    def envido(self):
        """ Carlcular el envido dadas 3 cartas """

        # Asegurarse que tiene 3 cartas
        self._validate_mano_completa()
        # ver todos los envidos posibles y elegir el mejor
        # aun si las tres cartas fueran de distinto palo, 
        #   la carta que sea mayor de ellas sería un envido posible
        envidos = [
            max([self._carta_cuenta_envido(carta) for carta in self.cartas])
        ]
        palos = [carta.palo for carta in self.cartas]
        # Si hay otros envidos ponerlos en la lista para ver cual es el mejor
        if palos[0] == palos[1]:
            envidos.append(self._sumar_envido(self.cartas[0], self.cartas[1]))
        if palos[0] == palos[2]:
            envidos.append(self._sumar_envido(self.cartas[0], self.cartas[2]))
        if palos[1] == palos[2]:
            envidos.append(self._sumar_envido(self.cartas[1], self.cartas[2]))

        # devolver el mas alto de todos
        return max(envidos)

    def __str__(self):
        return ', '.join(map(str, self.cartas))
