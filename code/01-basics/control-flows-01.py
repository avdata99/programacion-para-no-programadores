nombre = "juan"
a_en_nombre = "a" in nombre
# otra opcion a_en_nombre = nombre.find("a") >= 0

if a_en_nombre:
    print(f"La letra 'a' está en {nombre}")
else:
    print(f"La letra 'a' no está en {nombre}")

# for
paises = ["Argentina", "Brasil", "Chile", "Uruguay"]
print('Paises')
for pais in paises:
    print(f" - {pais}")


# for / continue / break
paises = ["Argentina", "Brasil", "Chile", "Uruguay", "Venezuela", "Colombia"]
print('Paises')
for pais in paises:
    if pais == "Chile":
        continue
    print(f" - {pais}")
    if pais == "Venezuela":
        break
print('FIN')

# while

a = 10
while a > 0:
    print(f" - {a}")
    a -= 1