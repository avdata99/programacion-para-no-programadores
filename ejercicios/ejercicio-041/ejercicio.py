"""
La funcion "crear_mazo_cartas_espaniolas" funciona casi bien.
Por algun motivo faltan algunas cartas.
La tarea de este ejercicio es reparar esta función para que el mazo este completo
"""


def crear_mazo_cartas_espaniolas():
    palos = ['oro', 'copa', 'espada', 'basto']
    mazo = []
    for n in range(1, 12):
        for palo in palos:
            carta = {'numero': n, 'palo': palo}
            mazo.append(carta)
    return mazo

mazo_esp = crear_mazo_cartas_espaniolas()
print(mazo_esp)

# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


assert {'numero': 10, 'palo': 'oro'} in mazo_esp
assert {'numero': 11, 'palo': 'oro'} in mazo_esp
assert {'numero': 12, 'palo': 'oro'} in mazo_esp

print('Ejercicio terminado OK')
