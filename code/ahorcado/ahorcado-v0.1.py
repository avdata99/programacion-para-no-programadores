"""
Juego del ahorcado
version 0.1
"""

palabra = 'lavarropas'
# mantengo el estado del juego como texto
estado = []

print('AHORACADO: Intento 1/10')
print('- ' * len(palabra))
letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado.append(letra_ingresada)
        aciertos += 1
    else:
        estado.append('-')

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))


#  ----------- INTENTO 2 ---------------
print('**********************************')
print('AHORACADO: Intento 2/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))

#  ----------- INTENTO 3 ---------------
print('**********************************')
print('AHORACADO: Intento 3/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))

#  ----------- INTENTO 4 ---------------
print('**********************************')
print('AHORACADO: Intento 4/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))


#  ----------- INTENTO 5 ---------------
print('**********************************')
print('AHORACADO: Intento 5/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))

#  ----------- INTENTO 6 ---------------
print('**********************************')
print('AHORACADO: Intento 6/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))

#  ----------- INTENTO 7 ---------------
print('**********************************')
print('AHORACADO: Intento 7/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))

#  ----------- INTENTO 8 ---------------
print('**********************************')
print('AHORACADO: Intento 8/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))

#  ----------- INTENTO 9 ---------------
print('**********************************')
print('AHORACADO: Intento 9/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()

c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))

#  ----------- INTENTO 10 ---------------
print('**********************************')
print('AHORACADO: Intento 10/10')
estado_texto = ' '.join(estado)
print(estado_texto)

letra_ingresada = input('Ingresa una letra: ')

if letra_ingresada == palabra:
    print('Ganaste!')
    quit()
    
c = 0
aciertos = 0
for letra in palabra:
    if letra_ingresada == letra:
        estado[c] = letra_ingresada
        aciertos += 1
    c = c + 1

if aciertos == 0:
    print('FALLASTE!')
else:
    print('Bien! {} aciertos'.format(aciertos))