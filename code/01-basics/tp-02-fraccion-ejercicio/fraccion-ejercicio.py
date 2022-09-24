class Fraccion:
    # init con numerador y denominador
    # def __add__ ....
    #    validar que "otro" es una fraccion
    #    sumar y devolver un objecto NUEVO tipo fraccion

assert Fraccion(2, 3) + Fraccion(1, 3) == Fraccion(1, 1)
assert Fraccion(4, 5) + Fraccion(3, 5) == Fraccion(7, 5)
assert Fraccion(3, 2) + Fraccion(8, 11) == Fraccion(49, 22)
