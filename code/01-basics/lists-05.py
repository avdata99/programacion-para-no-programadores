# Listas por/de comprension
# mas ejemplos https://www.analyticslane.com/2019/09/23/listas-por-comprension-en-python/

lista_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = [x for x in lista_base if x > 5]

""" También podría escribirse como 
lista = [
    x
    for x in lista_base
    if x > 5
]
"""

# Equivalente a:
lista2 = []
for x in lista_base:
    if x > 5:
        lista2.append(x)

print(f"Lista 1 {lista}")
print(f"Lista 2 {lista2}")

print(f"lista == lista2 {lista==lista2}")

""" muestra
Lista 1 [6, 7, 8, 9, 10]
Lista 2 [6, 7, 8, 9, 10]
lista == lista2 True
"""
