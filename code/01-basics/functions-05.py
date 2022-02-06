
def my_print(*args, end='\n', **kwargs):
    for arg in args:
        print(arg, end=end)

    for key, value in kwargs.items():
        print(f'{key}={value}', end=end)


my_print('hola', 'mundo', nombre='juan', edad=32, end=' + ')

# hola + mundo + nombre=juan + edad=32
