import math

class Fraccion:

    # init con numerador y denominador
    def __init__(self, numerador, denominador):
        self.numerador=numerador
        self.denominador=denominador
        self._simplificar_fraccion()

    def __add__(self, otro):
        if type(otro) != Fraccion:
            raise ValueError('Solo se le pueden sumar fracciones')
        #lo primero que hacemos es calcular el multiplo comun menor o mcm
        # "math.lcm" es una funcion 
        mcm = math.lcm(self.denominador, otro.denominador)
        # ahora Dividimos el denominador común por el denominador de cada fracción para encontrar la fracción unitaria que
        fraccion_unitaria1= int(mcm/self.denominador)
        fraccion_unitaria2= int(mcm/otro.denominador)
        # multiplicamos la fraccion original por la fraccion unitaria(fraccion con valor 1)
        #al multiplicar por 1 el valor real de la fraccion no cambia pero logramos ponerlas con el mismo denominador. lo que nos facilita sumar solo los numeradores
        # para esto multiplicamos el numeradr y el denominador de cada fraccion por el valor que obtenemos en las variables fraccionUnitaria 1 y 2 segun corresponda
        nuevo_denominador1= self.denominador*fraccion_unitaria1
        nuevo_denominador2= otro.denominador*fraccion_unitaria2
        nuevo_numerador1= self.numerador*fraccion_unitaria1
        nuevo_numerador2= otro.numerador*fraccion_unitaria2
        numerador_final= nuevo_numerador1+nuevo_numerador2

        #sumamos los nuevos numeradores y los nuevos denominadores deverian ser iguales
        resultado=Fraccion(numerador_final,nuevo_denominador1)    

        return resultado
    def __eq__(self, otro):
        return self.numerador == otro.numerador and self.denominador == otro.denominador
    def __str__(self):
        return f'{self.numerador} / {self.denominador}'
    def _simplificar_fraccion(self):
        print(self.numerador,self.denominador)
        # "math.gcd(*integers)" Retorna el máximo común divisor de los argumentos enteros
        divisor= math.gcd(self.numerador,self.denominador)
        self.numerador=int(self.numerador/divisor)
        self.denominador=int(self.denominador/divisor)
        print(self.numerador,self.denominador)
 
assert Fraccion(2,3) + Fraccion(1,3) == Fraccion(3,3)
assert Fraccion(4,5) + Fraccion(3,5) == Fraccion(7,5)

assert Fraccion(4, 2) == Fraccion(2, 1)

assert Fraccion(4,7)+ Fraccion(3, 9) == Fraccion(19, 21)


"""import math
a = math.lcm(4,8)
print(a)

b = math.gcd(3,2)
print(b)"""