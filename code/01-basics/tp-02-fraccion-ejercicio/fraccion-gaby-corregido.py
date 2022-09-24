# Tarea de suma de fracciones
# Aqui defino la clase fraccion


class Fraccion:
    """
    Aqui construyo el objeto fraccion, y le asigno a los atributos los parametros o valores
    # los atributos son el self.num y self.den y los parametros numerador y denominador
    """
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)
        self.simplificar()
 
    # defino lo  que quiero que se muestre, osea la fraccion 

    def __str__(self):
        return f'{self.numerador} / {self.denominador}'

    # para operar y simplificar las operaciones necesitamos el m.c.d y el m.c.m
    # maximo_comun_divisor = m.c.d

    def maximo_comun_divisor(self, a, b):
        resto = 0
        while b != 0:
            resto = b
            b = a % b
            a = resto
        return a

    def simplificar(self):
        numerador = self.maximo_comun_divisor(self.numerador, self.denominador)
        self.numerador = int(self.numerador/numerador)
        self.denominador = int(self.denominador/numerador)

    def minimo_comun_multiplo(self, a, b):
        return a * b / self.maximo_comun_divisor(a, b)

    #    sumar y devolver un objecto NUEVO tipo fraccion
    #    def __add__ ....
    #    validar que "otro" es una fraccion
    # hasta aca bien, ver el cuaderno y comparar donde dice formula del max_comun divisor

    # operaciones matematicas
    def __add__(self, otra):
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm / self.denominador
        diferencia_otra = mcm / otra.denominador
        numerador_resultante = (diferencia_self * self.numerador) + (diferencia_otra* otra.numerador)
        # luego el m.c.m sera el denominador y el numerador será la suma
        return Fraccion(numerador_resultante, mcm)

    def __eq__(self, otro):
        return self.numerador == otro.numerador and self.denominador == otro.denominador


assert Fraccion(2,3) + Fraccion(1,3) == Fraccion(3,3)
assert Fraccion(4,5) + Fraccion(3,5) == Fraccion(7,5)
assert Fraccion(2, 4) == Fraccion(1, 2)

f1 = Fraccion(1,2)
f2 = Fraccion(2,4)

f3 = f1 + f2
print(f"{f1} + {f2} = {f3}")
