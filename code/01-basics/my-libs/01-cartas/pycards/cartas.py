"""
Manejo de cartas individuales
"""


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return f'{self.numero} de {self.palo}'

    def __repr__(self):
        return f'<Carta {self.numero} de {self.palo}>'
