# tarea del envido
# funcion

def envido_carta_unica(valor):
    if valor >= 10:
        valor = 0
    return valor

def suma_envido(valor1, valor2):
    suma_envido = 20 + envido_carta_unica(valor1) + envido_carta_unica(valor2)
    return suma_envido

def envido(valor1, palo1, valor2, palo2):
    if palo1 == palo2:
        print ("envido")
        suma = suma_envido(valor1, valor2)
        print(suma)
    else:
        print(
            max([envido_carta_unica(valor1), envido_carta_unica(valor2)])
        )

palo1 = "oro"
palo2 = "oro"
valor1 = 11
valor2 = 10

envido(valor1, palo1, valor2, palo2)
