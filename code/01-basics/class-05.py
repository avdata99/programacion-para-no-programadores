"""
Ejemplo de una clase para manejar fracciones
(de numerador y denominador entero y positivo)
"""


class Fraccion:
    """ Clase para manejar fracciones de numeros enteros positivos """

    def __init__(self, numerador, denominador):
        if type(numerador) != int or type(denominador) != int:
            raise ValueError('Solo numeros enteros aceptados')
        if numerador < 0 or denominador < 1:
            raise ValueError('Solo numeros positivos aceptados')
    
        self._numerador = numerador
        self._denominador = denominador
        self._simplificar()

    @property
    def numerador(self):
        return self._numerador
    
    @numerador.setter
    def numerador(self, num):
        if type(num) != int:
            raise ValueError('Tipo de dato no admitido para numerador')
        if num < 1:
            raise ValueError('Valor de numerador no admitido')
        self._numerador = num
        self._simplificar()

    @property
    def denominador(self):
        return self._denominador
    
    @denominador.setter
    def denominador(self, den):
        if type(den) != int:
            raise ValueError('Tipo de dato no admitido para denominador')
        if den <= 0:
            raise ValueError('Valor de denominador no admitido')
        self._denominador = den
        self._simplificar()

    def _simplificar(self):
        """ Simplificar la fraccion a los numeros mas bajos posibles """
        men = min(self._numerador, self._denominador)
        for n in range(men, 1, -1):
            # Si este numero divide a los dos, entonces los divido
            if self._numerador % n == 0 and self._denominador % n == 0:
                self._numerador = int(self._numerador / n)
                self._denominador = int(self._denominador / n)
                break

    def __add__(self, otro):
        """ Sumar fracciones"""
        if type(otro) != Fraccion:
            raise ValueError('Solo suma aceptada entre fracciones')
    
        nuevo_denominador = self._denominador * otro.denominador
        nuevo_numerador = self._numerador * otro.denominador + otro.numerador * self._denominador

        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, otro):
        if type(otro) != Fraccion:
            raise ValueError('No son objetos iguales')

        return self._numerador == otro.numerador and self._denominador == otro.denominador

    def __str__(self):
        return f'({self._numerador} / {self._denominador})'

    def __repr__(self):
        return f'<Fraccion {self._numerador} / {self._denominador}>'


# Pruebas de funcionamiento

assert Fraccion(2, 3) + Fraccion(1, 3) == Fraccion(1, 1)
assert Fraccion(4, 5) + Fraccion(3, 5) == Fraccion(7, 5)
assert Fraccion(4, 5) + Fraccion(6, 5) == Fraccion(2, 1)
assert Fraccion(5, 12) + Fraccion(4, 19) == Fraccion(143, 228)
assert Fraccion(3, 2) + Fraccion(8, 11) == Fraccion(49, 22)

# Probar la simplificacion al inicio
assert Fraccion(8, 4) == Fraccion(2, 1)

f1 = Fraccion(2, 4)
assert f1 == Fraccion(1, 2)

f1.numerador = 2
assert f1 == Fraccion(1, 1), f'{f1} no es igual a {Fraccion(1, 1)}'

f1.denominador = 8
assert f1 == Fraccion(1, 8)

print('TODO OK')
