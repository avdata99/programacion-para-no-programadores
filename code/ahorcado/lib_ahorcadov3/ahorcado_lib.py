import random


def elegir_palabra():
    palabras = ['lavarropas', 'televisor', 'polonia', 'estufa']
    azar = random.randint(0, len(palabras)-1)
    return palabras[azar]


def intento(nro, estado, palabra):
    print('AHORACADO: Intento {}/10'.format(nro))
    estado_texto = ' '.join(estado)
    print(estado_texto)
    letra_ingresada = input('Ingresa una letra: ')

    if letra_ingresada == palabra:
        print('Ganaste!')
        quit()

    aciertos = 0
    c = 0
    for letra in palabra:
        if letra_ingresada == letra:
            estado[c] = letra_ingresada
            aciertos += 1
        c = c + 1

    if aciertos == 0:
        print('FALLASTE!')
    else:
        print('Bien! {} aciertos'.format(aciertos))
    
    return estado