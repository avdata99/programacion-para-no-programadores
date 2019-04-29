"""
Juego del ahorcado
version 0.2
"""

from lib_ahorcadov3.ahorcado_lib import elegir_palabra, intento

palabra = elegir_palabra()
estado = ['-'] * len(palabra)

for i in range(1, 11):
    estado = intento(nro=i, estado=estado, palabra=palabra)