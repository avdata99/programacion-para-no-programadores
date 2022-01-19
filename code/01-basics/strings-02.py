# Algunas funciones de los "strings"
nombre = "Juan Gonzalez"
nombre_minuscula = nombre.lower()
print(nombre_minuscula)

nombre_mayuscula = nombre.upper()
print(nombre_mayuscula)

# buscar
print(nombre.find("Gonzalez"))
# buscar tambien
print("Gonzalez" in nombre)

separador = "+"
lista = ["Juan", "Pedro", "Luis"]
print(separador.join(lista))
# muestra Juan+Pedro+Luis

# limpiar caracteres a los costados
print("   hola   ".strip())
# muestra hola

print("[algo]".strip("[]"))
# muestra algo
