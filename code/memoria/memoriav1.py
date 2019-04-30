"""
Juego de memoria
Tablero con Fichas que el jugador debe recordar
"""

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
filas = 3
columnas = 4

f = 0
c = 0
for fila in range(filas):
    f = f + 1
    for columna in range(columnas):
        c = c + 1
        print('|X', end='')
    print('|')


resultados = [[]]
f = 0
c = 0
for fila in range(filas):
    
    for columna in range(columnas):
        resultados[f]

        c = c + 1
    
    f = f + 1