"""
puse para sumar los dos palos + 20 y llegar al puntaje exacto de el envido
"""

class Carta:
    def __init__(self, numero, palo):
        self._numero = numero
        self.palos_espaniola= ['copa', 'oro', 'espada', 'basto']
        self._palo = palo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if type(value) != int:
            raise Exception('Solo están permitidos numeros')
        if value >=1:
            if value <= 7:
                return True 
        if value >=10:
            if value <=12:
                return True                  
        self._numero = value

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, value):
        if type(value) != str:
            raise Exception (f'solo esta permitido {self.palo_espaniola}')
        self._palo = value

    def __eq__ (self, otro):
        if type(otro) == Carta:
            if self._palo == otro.palo:
                    return True
            return False


    def __add__ (self, otro):
        if type(otro) == int:
            self._numero += otro
            self._numero += 20
            return self._numero    

    def __str__(self):
        return f'{self.numero} de {self.palo}'

# Pruebas
envido1 = Carta(5, 'espada') + Carta(6, 'espada')
envido2=   Carta(3, 'copa') + Carta(7, 'copa')
print(str(envido1))
print(str(envido2))