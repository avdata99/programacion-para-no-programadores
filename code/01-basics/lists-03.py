nombres = ["juan", "pedro", "luis"]
apellidos = ["gonzalez", "gomez", "rodriguez"]

# combinar todos los nombres completos posibles
combinaciones = []
for nombre in nombres:
    for apellido in apellidos:
        nombre_completo = f"{nombre} {apellido}"
        combinaciones.append(nombre_completo)

total_combinaciones = len(combinaciones)
print(f'Total de combinaciones: {total_combinaciones}')
# Total de combinaciones: 9

primer_combinacion = combinaciones[0]
print(f'La primera combinación es: {primer_combinacion}')
# La primera combinación es: juan gonzalez

primeras_2_combinaciones = combinaciones[0:2]
print(f'Las primeras dos combinación son: {primeras_2_combinaciones}')
# Las primeras dos combinación son: ['juan gonzalez', 'juan gomez']

ultimas_2_combinaciones = combinaciones[-2:]
print(f'La últimas dos combinaciones son: {ultimas_2_combinaciones}')
# La últimas dos combinaciones son: ['luis gomez', 'luis rodriguez']

# eliminar elementos especìficos
combinaciones.remove("juan gonzalez")
# eliminar el primer elemento
del combinaciones[0]

# eliminar y devolver lo eliminado
primer_elemento = combinaciones.pop(0)
print(f'La primera combinación era: {primer_elemento} y ahora es {combinaciones[0]}')

# ordenar
combinaciones.sort()
print(f'Lista ordenada: {combinaciones}')

# invertir orden
combinaciones.reverse()
print(f'Lista invertida: {combinaciones}')
