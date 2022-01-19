
def potencia(a, b=2):
    print(f'Se llamo a la funcion potencia con {a} y {b}')
    return a ** b

resultado = potencia(3)
print(f'Resultado de la potencia 3 ** 2: {resultado}')

resultado = potencia(3, 3)
print(f'Resultado de la potencia 3 ** 3: {resultado}')
