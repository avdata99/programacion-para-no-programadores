"""
Clase Carta para juegos de cartas
"""

class Carta:
    def __init__(self, numero, palo):
        self._numero = numero
        self._palo = palo
        self.palo_espaniola= ['oro', 'copa', 'espada', 'basto']

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if type(value) != int:
            raise Exception('Solo están permitidos numeros')
        if value >=1:
            if value<=12:
                return True
        self._numero = value

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, value):
        if type(value) != str:
            raise Exception ('Solo se permiten letras')
        if value != self.palo_espaniola:
            raise Exception ( f'solo esta permitido {self.palo_espaniola}')   
        self._palo = value

    def __add__ (self, otro):
        if type(otro) == Carta:
            if self._palo == otro.palo:
                if self._numero == otro.numero:
                    return True
            else:
                return False

    def __eq__ (self, otro):
        if type(otro) == Carta:
            if self._numero == otro.numero:
                if self._palo == otro.palo:
                    return True
            else:
                 return False

    def __str__(self):
        return f'{self.numero} de {self.palo}'

# Pruebas

carta1 = Carta(3, 'espada')
carta2 = Carta(3, 'oro')
carta3 = Carta(9, 'oro')
carta4 = Carta(5, 'basto')
carta5 = Carta(3, 'espada')
carta6 = Carta(5, 'basto')

print(str(carta1 + carta2))
print(str(carta1 + carta3))
print(str(carta1 + carta5))
print(str(carta4 + carta1))
print(str(carta4 + carta6))
print(str(carta4 + carta2))

