class Carta:
    def __init__(self, numero, palo):
        self._numero = numero
        self._palo = self._validar_palo(palo)
        self.palos_validos = ['oro', 'copa', 'basto', 'espada']

    def _validar_palo(self, value):
        """ Devuelve el valor limpio o lanza un error si no es un palo valido """
        if type(value) != str:
            raise Exception ('Solo están permitidas letras')
        if value.lower() not in self.palos_validos:
            raise Exception('Palo invalido')
        return value.lower()

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
        self._palo = self._validar_palo(value)

    def __str__(self):
        return f'{self.numero} de {self.palo}'

# Pruebas

carta1 = Carta(3, 'espada')
print(str(carta1))

carta1.palo = 'Pooo'
