"""
Clase Carta para juegos de cartas
"""

from random import choice, randint


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

    def __repr__(self):
        return self.__str__()

    def __add__(self, otro):
        if type(otro) == int:
            return self._numero + otro
            # nuevo_numero = self._numero + otro
            # return Carta(nuevo_numero, self._palo)

    def __eq__(self, otro):
        if type(otro) == Carta:
            if self._numero == otro.numero:
                if self._palo == otro.palo:
                    return True
            return False
        elif type(otro) == int:
            return self._numero == otro
        elif type(otro) == str:
            return self._palo == otro


class Mazo:
    def __init__(self):
        self._cartas = []
    
    def append(self, value):
        if type(value) != Carta:
            raise Exception('Solo cartas')
        self._cartas.append(value)

    @property
    def cartas(self):
        return self._cartas
    
    def __str__(self):
        return f'<Mazo {self._cartas}>'

    def agregar_carta_al_azar(self):
        while True:
            numero = randint(1, 12)
            palo = choice(['palo', 'oro', 'copa'])
            carta = Carta(numero, palo)
            if carta not in self._cartas:
                self.append(carta)
                break

    def __len__(self):
        return len(self._cartas)


# Pruebas

carta1 = Carta(1, 'espada')
carta2 = Carta(2, 'espada')

mazo = Mazo()
mazo.append(carta1)
mazo.append(carta2)

for n in range(30):
    mazo.agregar_carta_al_azar()

print(len(mazo))
print(mazo)

