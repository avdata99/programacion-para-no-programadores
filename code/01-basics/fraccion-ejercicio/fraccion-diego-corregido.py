class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        self.denominador = int(denominador)
        
    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)
print 
        
f = Fraccion(3, 4)
print(f)







quit
"""
assert fraccion(2,3) + fraccion(1,3) == fraccion (3,3)
assert fraccion(4,5) + fraccion(3,5) == fraccion (7,5)
assert fraccion(10,9) + fraccion(15,3) == fraccion (55,9)
assert fraccion(40,4) - fraccion(8,2) == fraccion (24,4)

print resultado  
"""

