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
        elif value > 0 and value <= 12:
            self._numero = value
        else:
            raise Exception('Solo están permitidos numeros del 1 al 12')

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, value):
        self._palo = value

    def __str__(self):
        return f'{self.numero} de {self.palo}'

# Pruebas

carta1 = Carta(3, 'espada')
print(str(carta1))

carta1.numero = -17
