nombre = 'Pedro'
pais = 'Chile'

print("Hello world {} de {}!".format(nombre, pais))
# Hello world Pedro de Chile!

# valores enumerados
print("Valores enumerados. Hello world {0} de {1} ({0}-{1})!".format(nombre, pais))
# Valores enumerados. Hello world Pedro de Chile (Pedro-Chile)!

# valores con nombre
print("Valores con nombre. Hello world {name} de {country}!".format(name=nombre, country=pais))
# Valores con nombre. Hello world Pedro de Chile!

# Estilo C
print("Estilo C. Hello world %s de %s !" % (nombre, pais))
# Estilo C. Hello world Pedro de Chile !

# Nueva opcion con python 3.6
print(f"Hello world {nombre} de {pais}!")
# Hello world Pedro de Chile!
