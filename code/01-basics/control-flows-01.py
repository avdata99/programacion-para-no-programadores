nombre = "juan"
a_en_nombre = "a" in nombre
# otra opcion a_en_nombre = nombre.find("a") >= 0

if a_en_nombre:
    print(f"La letra 'a' está en {nombre}")
else:
    print(f"La letra 'a' no está en {nombre}")
