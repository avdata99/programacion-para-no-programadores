"""
Clase Carta para juegos de cartas
"""

class Carta:
    def __init__(self, numero, palo):
        self._numero = numero
        self._palo = palo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if type(value) != int:
            raise Exception('Solo están permitidos numeros')
        self._numero = value

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, value):
        self._palo = value

    def __str__(self):
        return f'{self.numero} de {self.palo}'

    def __add__(self, otro):
        """ La suma de cartas devuelve el envido entre ellas dos """
        p1 = self._numero if self._numero < 10 else 0
        p2 = otro.numero if otro.numero < 10 else 0
        # if p1 >= 10:
        #     p1 = 0
        # if p2 >= 10:
        #     p2 = 0

        if self._palo == otro.palo:
            return p1 + p2 + 20
        else:
            return max([p1, p2])



# Pruebas

carta1 = Carta(3, 'espada')
carta2 = Carta(2, 'espada')
carta3 = Carta(2, 'oro')
carta4 = Carta(12, 'oro')
carta5 = Carta(11, 'oro')
carta6 = Carta(11, 'copa')

assert carta1 + carta2 == 25, "carta1 + carta2 esta mal"
assert carta1 + carta3 == 3, "carta1 + carta3 esta mal"
assert carta1 + carta4 == 3, f"carta1 + carta4 == {carta1 + carta4} != 3"
assert carta3 + carta4 == 22, f"carta3 + carta4 == {carta3 + carta4} != 22"
assert carta4 + carta5 == 20, f"carta4 + carta5 == {carta4 + carta5} != 20"
assert carta5 + carta6 == 0, f"carta5 + carta6 == {carta4 + carta5} != 20"

print('OK')
