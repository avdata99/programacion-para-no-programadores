apellidos = ["gonzalez", "gomez", "rodriguez", "lopez", "garcia"]

total_apellidos = len(apellidos)
print(f'Total de apellidos: {total_apellidos}')
# Total de apellidos: 5

primer_apellido = apellidos[0]
print(f'El primer apellido es: {primer_apellido}')
# El primer apellido es: gonzalez

ultimo_apellido = apellidos[-1]
print(f'El último apellido es: {ultimo_apellido}')
# El último apellido es: garcia

primeros_2 = apellidos[0:2]
print(f'Los primeros dos: {primeros_2}')
# Los primeros dos: ['gonzalez', 'gomez']

ultimos_2 = apellidos[-2:]
print(f'Los últimos dos son: {ultimos_2}')
# Los últimos dos son: ['lopez', 'garcia']

# eliminar elementos especìficos
apellidos.remove("lopez")
# eliminar el primer elemento
del apellidos[0]

# eliminar y devolver lo eliminado
primer_elemento = apellidos.pop(0)
print(f'El primero era: {primer_elemento} y ahora es {apellidos[0]}')
# El primero era: gomez y ahora es rodriguez

# ordenar
apellidos.sort()
print(f'Lista ordenada: {apellidos}')
# Lista ordenada: ['garcia', 'rodriguez']

# invertir orden
apellidos.reverse()
print(f'Lista invertida: {apellidos}')
# Lista invertida: ['rodriguez', 'garcia']