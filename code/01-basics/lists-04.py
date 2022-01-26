nombre = "Pedro"

print(f"La primera letra de mi nombre es {nombre[0]}")
print(f"La última letra de mi nombre es {nombre[-1]}")

# los strings pueden ser tratados como listas de letras (caracteres)
for letra in nombre:
    print(letra, end='-')
