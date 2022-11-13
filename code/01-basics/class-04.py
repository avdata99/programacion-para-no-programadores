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

    def __add__(self, value):
        if type(value) != Carta:
            raise Exception (f'Los objetos del tipo {type(Carta)} sólo pueden sumarse con objetos de la misma clase')
        elif self._palo == value.palo:
            print(f'Usted tiene {self._numero + value.numero} de envido')
            return self._numero + value.numero
        else:
            pass


# Pruebas

carta1 = Carta(3, 'espada')
carta2 = Carta(5, 'espada')

assert carta1 + carta2 == 8
