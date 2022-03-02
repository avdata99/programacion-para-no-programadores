from random import choice

class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return f'{self.numero} de {self.palo}'

    def __repr__(self):
        return f'<Carta {self.numero} de {self.palo}>'


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

    def entregar_cartas(self):
        """ Entrega 3 cartas al azar y las quita del mazo """
        mano = []
        for carta in range(1,4):#modifico para entregar 3 cartas, y no llamar a la funcion 3 veces
            carta = choice(self.cartas)
            mano.append(carta)
            self.cartas.remove(carta)
        return mano #retorno un array de 3 cartas aleatorias


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


class MazoTruco(MazoEspaniola):
    """ Mazo de cartas truco (españolas quitando comodines, ochos y nueves) """

    def cargar_cartas(self):
        """ Cargar las cartas del mazo español
            y quitar las que no usamos para el truco
            """
        super().cargar_cartas()
        to_remove = []
        for carta in self.cartas:
            # quitar comodines, 8s y 9s
            if carta.numero in [0, 8, 9]:
                to_remove.append(carta)

        # otra forma de listar las cartas a remover
        # to_remove = [carta for carta in self.cartas if carta.numero in [0,8, 9]]

        for remove in to_remove:
            self.cartas.remove(remove)


class Mano:
    """ Una mano de cartas de cualquier juego """
    def __init__(self, cartas):
        self.cartas = cartas

class ManoTruco(Mano):
    """Elimino funcion suma, funcion agregar carta y comprobacion de 3 cartas ya que la funcion entregar_cartas siempre entrega 3"""
    def _carta_cuenta_envido(self, carta):
        """ de una carta data obtiene cuanto suma al envido
            De un 12 devuelve 2, de un 10 cero y de un 7, devuelve 7"""
        return carta.numero if carta.numero < 10 else 0

    def _sumar_envido(self, carta1, carta2):
        """ Aqui las dos cartas finales se suman luego de detectar palos iguales """
        return 20 + self._carta_cuenta_envido(carta1) + self._carta_cuenta_envido(carta2)

    def envido(self):
        """ Calcular el envido dadas 3 cartas """

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

tr = MazoTruco()
mn = ManoTruco(tr.entregar_cartas()) # llamo una sola vez a la funcion entregar carta

print(f'Mano: {mn}')
print(f'Envido: {mn.envido()}')
