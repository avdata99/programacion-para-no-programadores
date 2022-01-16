nombre = "juan"
apellido = "gonzalez"

# sumar. Le decimos concatenar
print(nombre + " " + apellido)

# los strings pueden ser tratados como listas de letras (caracteres)
for letra in nombre:
    print(letra, end='-')

respuesta = f"Mi nombre es {nombre} y mi apellido es {apellido}"
print(respuesta)

print(f"La primera letra de mi nombre es {nombre[0]}")
print(f"La última letra de mi nombre es {nombre[-1]}")
