class Fraccion:
    def __init__(self, numerador, denominador):
        if type(numerador) != int or type(denominador) != int:
            raise ValueError('Solo numeros enteros aceptados')
        if numerador < 0 or denominador < 1:
            raise ValueError('Solo numeros positivos aceptados')
    
        self.numerador = numerador
        self.denominador = denominador
        self._simplificar()

    def _simplificar(self):
        """ Simplificar la fraccion a los numeros mas simples posibles """
        men = min(self.numerador, self.denominador)
        for n in range(men, 1, -1):
            if self.numerador % n == 0 and self.denominador % n == 0:
                self.numerador = self.numerador / n
                self.denominador = self.denominador / n
                break

    def __add__(self, otro):
        """ Sumar fracciones"""
        if type(otro) != Fraccion:
            raise ValueError('Solo suma aceptada entre fracciones')
    
        nuevo_denominador = self.denominador * otro.denominador
        nuevo_numerador = self.numerador * otro.denominador + otro.numerador * self.denominador

        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, otro):
        if type(otro) != Fraccion:
            raise ValueError('No son objetos iguales')

        return self.numerador == otro.numerador and self.denominador == otro.denominador

    def __str__(self):
        return f'({self.numerador} / {self.denominador})'

    def __repr__(self):
        return f'<Fraccion {self.numerador} / {self.denominador}>'

assert Fraccion(2, 3) + Fraccion(1, 3) == Fraccion(1, 1)
assert Fraccion(4, 5) + Fraccion(3, 5) == Fraccion(7, 5)
assert Fraccion(4, 5) + Fraccion(6, 5) == Fraccion(2, 1)
assert Fraccion(5, 12) + Fraccion(4, 19) == Fraccion(143, 228)
assert Fraccion(3, 2) + Fraccion(8, 11) == Fraccion(49, 22)

# Probar la simplificacion al inicio
assert Fraccion(8, 4) == Fraccion(2, 1)

print('TODO OK')
