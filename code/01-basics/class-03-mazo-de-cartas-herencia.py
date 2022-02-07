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

    def entregar_carta(self):
        """ Entregaer una carta al azar (y quitarla del mazo) """
        carta = choice(self.cartas)
        self.cartas.remove(carta)
        return carta


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
    def __init__(self):
        self.cartas = []


class ManoTruco(Mano):
    def __add__(self, otro):
        """ La funcion suma es agregar una carta 
            Solo esta definida para objetos tipo carta
            (solo puedo sumarle cartas)
            """
        if type(otro) != Carta:
            raise ValueError('Solo se le pueden sumar Cartas')
        self._agregar_carta(otro)
        return self

    def _agregar_carta(self, carta):
        """ Solo para llamar internalemte """
        if len(self.cartas) > 3:
            raise ValueError('Una mano de truco no puede tener mas de tres cartas')
        self.cartas.append(carta)

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
        """ Aqui las dos cartas finales se suman luego de detectar palos similares """
        return 20 + self._carta_cuenta_envido(carta1) + self._carta_cuenta_envido(carta2)

    def envido(self):
        self._validate_mano_completa()
        # ver todos los envidos posibles y elegir el mejor
        envidos = [max([self._carta_cuenta_envido(carta) for carta in self.cartas])]
        palos = [carta.palo for carta in self.cartas]
        if palos[0] == palos[1]:
            envidos.append(self._sumar_envido(self.cartas[0], self.cartas[1]))
        if palos[0] == palos[2]:
            envidos.append(self._sumar_envido(self.cartas[0], self.cartas[2]))
        if palos[1] == palos[2]:
            envidos.append(self._sumar_envido(self.cartas[1], self.cartas[2]))

        return max(envidos)

    def __str__(self):
        return ', '.join(map(str, self.cartas))

tr = MazoTruco()
mn = ManoTruco()

carta1 = tr.entregar_carta()
mn += carta1
carta2 = tr.entregar_carta()
mn += carta2
carta3 = tr.entregar_carta()
mn += carta3

print(f'Mano: {mn}')
print(f'Envido: {mn.envido()}')
