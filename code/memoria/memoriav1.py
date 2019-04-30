"""
Juego de memoria
Tablero con Fichas que el jugador debe recordar
"""

filas = 3
columnas = 4
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

celdas = filas * columnas

print('Letras: ' + letras)

f = 0
c = 0
for fila in range(filas):
    f = f + 1
    for columna in range(columnas):
        c = c + 1
        print('|X', end='')
    print('|')

