from random import choice


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __repr__(self):
        return f'{self.numero} de {self.palo}'

class Mazo:
    def __init__(self, palos):
        self.cartas = []
        self.palos = palos
        self.cargar_cartas()

    def cargar_cartas(self):
        raise NotImplementedError

    def entregar_carta(self):
        """ Entregaer una carta al azar y quitarla del mazo """
        carta = choice(self.cartas)
        self.cartas.remove(carta)
        return carta


class MazoEspaniola(Mazo):
    def __init__(self):
        super().__init__(palos=['Oro', 'Copa', 'Espada', 'Basto'])

    def cargar_cartas(self):
        
        # Agregar dos comodines
        self.cartas.append(Carta(numero=0, palo='Comodin'))
        self.cartas.append(Carta(numero=0, palo='Comodin'))

        # Agregar las cartas de cada palo
        for n in range(1, 13):
            for p in self.palos:
                self.cartas.append(Carta(numero=n, palo=p))


class MazoTruco(MazoEspaniola):
    def cargar_cartas(self):
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
carta = tr.entregar_carta()
print(f' - Carta entregada {carta}')
carta = tr.entregar_carta()
print(f' - Carta entregada {carta}')

print('Cartas respantes:')
print(tr.cartas)
