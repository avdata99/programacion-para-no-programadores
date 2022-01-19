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
