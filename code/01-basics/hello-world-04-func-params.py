# Format strings

def hello_world(nombre, pais):
    print("Hello world {} de {}!".format(nombre, pais))
    # valores enumerados
    print("Valores enumerados. Hello world {0} de {1} ({0}-{1})!".format(nombre, pais))
    # valores con nombre
    print("Valores con nombre. Hello world {name} de {country}!".format(name=nombre, country=pais))
    # Estilo C
    print("Estilo C. Hello world %s de %s !" % (nombre, pais))
    # Nueva opcion con python 3.8
    print(f"Hello world {nombre} de {pais}!")

hello_world(nombre="Juan", pais="Argentina")
