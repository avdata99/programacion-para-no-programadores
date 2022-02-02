# Algunas funciones de los "strings"
nombre = "Juan Gonzalez"
nombre_minuscula = nombre.lower()
print(nombre_minuscula)
# juan gonzalez

nombre_mayuscula = nombre.upper()
print(nombre_mayuscula)
# JUAN GONZALEZ

# buscar (devuielve la posicion donde se encontró)
print(nombre.find("Gonzalez"))
# 5

# buscar tambien
print("Gonzalez" in nombre)
# True

# limpiar caracteres a los costados
print("   ho la   ".strip())
# muestra ho la (sin espacios al principio o al final)

print("[algo]".strip("[]"))
# muestra algo
