# Listas por/de comprension
# mas ejemplos https://www.analyticslane.com/2019/09/23/listas-por-comprension-en-python/

lista = [x for x in "algunos caracteres mezclados" if x != "e"]

""" También podría escribirse como 
lista = [
    x
    for x in "algunos caracteres mezclados"
    if x != "e"
]
"""

# Equivalente a:
lista2 = []
for x in "algunos caracteres mezclados":
    if x != "e":
        lista2.append(x)

print(f"Lista 1 {lista}")
print(f"Lista 2 {lista2}")

print(f"lista == lista2 {lista==lista2}")
