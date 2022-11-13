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

def __add__(self, value1, value2):
        if type(value1) != Carta or type(value2) != Carta:
            raise Exception (f'Los objetos del tipo {type(Carta)} sólo pueden sumarse con objetos de la misma clase')
        elif self._palo == value1.palo and self._palo != value2.palo:
            value2.numero = 20
            envido = self._numero + value1.numero + value2.numero
            print(f'Tengo {envido} de envido')
            return envido
        elif self._palo == value2.palo and self._palo != value1.palo:
            value1.numero = 20
            envido = self._numero + value2.numero + value1.numero
            print(f'Tengo {envido} de envido')
            return envido
        elif self._palo != value2.palo and self._palo != value1.palo:
            if self._numero > value1.numero and self._numero > value2.numero:
                return self._numero
            elif value1.numero > value2.numero and value1.numero > self._numero:
                return value1.numero
            else:
                return value2.numero
        elif self._palo == value2.palo and self._palo != value1.palo:
            return print('Flor!')
        else:
            raise Exception('Algo hiciste mal pero no sé qué')

def __eq__(self, value):
    if type(value) != Carta:
        raise Exception (f'Los objetos del tipo {type(Carta)} sólo pueden igualarse con objetos de la misma clase')
    elif self._numero == value.numero and self._palo == value.palo:
        return True
    else:
        return False

# Pruebas

carta1 = Carta(7, 'espada')
carta2 = Carta(6, 'espada')
carta3 = Carta(1, 'palo')
carta4 = Carta(7, 'espada')

#assert print(carta1 != carta2)
assert print(carta1 == carta4)