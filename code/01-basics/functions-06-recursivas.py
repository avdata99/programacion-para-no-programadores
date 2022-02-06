"""
Serie de Fibonachi
Resuelta con una funcion recursiva
"""

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


for nro in range(11):
    fib_num = fib(nro)
    print(f'fib({nro}) = {fib_num}')
