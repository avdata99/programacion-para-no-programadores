
def raiz(numero, raiz=2):
    print(f'Se llamo a la funcion raiz con {numero} y {raiz}')
    return numero ** (1/raiz)

resultado = raiz(numero=64)
print(f'Resultado de la raiz cuadrada de 64: {resultado}')

resultado = raiz(raiz=3, numero=27)
print(f'Resultado de la raiz cúbica de 27: {resultado}')
