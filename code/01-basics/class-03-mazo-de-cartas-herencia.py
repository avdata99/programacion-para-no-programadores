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
        for remove in to_remove:
            self.cartas.remove(remove)


tr = MazoTruco()
carta = tr.entregar_carta()
print(f' - Carta entregada {carta}')
#  - Carta entregada 4 de Espada
carta = tr.entregar_carta()
print(f' - Carta entregada {carta}')
# - Carta entregada 6 de Espada
carta = tr.entregar_carta()
print(f' - Carta entregada {carta}')
#  - Carta entregada 4 de Copa

print('Cartas respantes:')
print(tr.cartas)
"""
Cartas respantes:
[
     <Carta 1 de Oro>, <Carta 1 de Copa>, <Carta 1 de Espada>, <Carta 1 de Basto>,
     <Carta 2 de Oro>, <Carta 2 de Copa>, <Carta 2 de Espada>, <Carta 2 de Basto>,
     <Carta 3 de Oro>, <Carta 3 de Copa>, <Carta 3 de Espada>, <Carta 3 de Basto>,
     <Carta 4 de Oro>,                                         <Carta 4 de Basto>,
     <Carta 5 de Oro>, <Carta 5 de Copa>, <Carta 5 de Espada>, <Carta 5 de Basto>,
     <Carta 6 de Oro>, <Carta 6 de Copa>,                      <Carta 6 de Basto>,
     <Carta 7 de Oro>, <Carta 7 de Copa>, <Carta 7 de Espada>, <Carta 7 de Basto>,
     <Carta 10 de Oro>, <Carta 10 de Copa>, <Carta 10 de Espada>, <Carta 10 de Basto>,
     <Carta 11 de Oro>, <Carta 11 de Copa>, <Carta 11 de Espada>, <Carta 11 de Basto>,
     <Carta 12 de Oro>, <Carta 12 de Copa>, <Carta 12 de Espada>, <Carta 12 de Basto>
]
"""
