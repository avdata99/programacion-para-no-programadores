import fractions


class fraccion:
    def _init_(self, numerador, denominador):
        self.numerador = int(numerador)
        if numerador == denominador:
            return 1
        self.denominador = int(denominador)
        """
        if denominador == 0:
            return None ("denominador no puede ser 0")
            """

        if denominador == 1:
            return self.numerador

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)
print 
        
            
numero = [1, 100]

numerador = numero 
denominador = numero 









quit
"""
assert fraccion(2,3) + fraccion(1,3) == fraccion (3,3)
assert fraccion(4,5) + fraccion(3,5) == fraccion (7,5)
assert fraccion(10,9) + fraccion(15,3) == fraccion (55,9)
assert fraccion(40,4) - fraccion(8,2) == fraccion (24,4)

print resultado  
"""

