from pycards.mazos import MazoEspaniola


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

