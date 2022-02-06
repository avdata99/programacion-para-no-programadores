
def mi_function(*args, **kwargs):
    print(f'Argumentos sin nombre: {args}')
    print(f'Argumentos con nombre: {kwargs}')


mi_function(3, "algo", nombre='Luis', edad=91)

# Argumentos sin nombre: (3, 'algo')
# Argumentos con nombre: {'nombre': 'Luis', 'edad': 91}
