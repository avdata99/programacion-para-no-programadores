#establezco un diccionario con cada carta con su palo y valor
naipes = {
    'carta1': {
        'palo': 'copa',
        'numero': 7,
    },
    'carta2': {
        'palo': 'oro',
        'numero': 12,
    },
    'carta3': {
        'palo': 'espada',
        'numero': 6,
    }
}

def suma2(c1, c2):
    return c1 + c2 + 20

def suma1(c1, c2):
    return c1 + c2

#asigno una variable a cada item palo de cada carta en el diccionario
palo_carta1 = naipes['carta1']['palo']
palo_carta2 = naipes['carta2']['palo']
palo_carta3 = naipes['carta3']['palo']

#asigno una variable a cada item numero de cada carta en el diccionario
nro_carta1 = naipes['carta1']['numero']
nro_carta2 = naipes['carta2']['numero']
nro_carta3 = naipes['carta3']['numero']


numeros = [nro_carta1, nro_carta2, nro_carta3] #genero una lista con los mumeros de mis cartas
print(numeros)

if palo_carta1 == palo_carta2 == palo_carta3: #comparo si las 3 cartas son del mismo palo
    numeros.sort() #ordeno la lista numeros de menor a mayor
    print(numeros)
    if nro_carta1 < 10:
        if nro_carta2 < 10: 
            if nro_carta3 < 10:
                envido = suma2(numeros[1], numeros[2])
                print(envido)
            else:
                envido = suma2(numeros[0], numeros[1])
                print(envido)
        else:
            if nro_carta3 < 10:
                envido = suma2(numeros[0], numeros[1])
                print(envido)
            else:
                envido = suma1(numeros[0], 20)
                print(envido)
    else:
        if nro_carta2 < 10: 
            if nro_carta3 < 10:
                envido = suma2(numeros[0], numeros[1])
                print(envido)
            else:
                envido = suma1(numeros[0], 20)
                print(envido)
        else:
            if nro_carta3 < 10:
                envido = suma1(numeros[0], 20)
                print(envido)
            else:
                print(20)
else:
    #if palo_carta1 != palo_carta2 != palo_carta3: #comparo si las 3 cartas son de distinto palo -> solo me compara los primeros 2!!!!
    #    print("No tengo puntos")
    if palo_carta1 != palo_carta3:
        if palo_carta1 == palo_carta2:
            if nro_carta1 < 10:
                if nro_carta2 < 10:
                    envido = suma2(nro_carta1, nro_carta2)
                    print(envido)
                else:
                    envido = suma1(nro_carta1, 20)
                    print(envido)
            else:
                if nro_carta2 < 10:
                    envido = suma1(nro_carta2, 20)
                    print(envido)
                else:
                    print(20)
        else:
            if palo_carta2 == palo_carta3:
                if nro_carta2 < 10:
                    if nro_carta3 < 10:
                        envido = suma2(nro_carta2, nro_carta3)
                        print(envido)
                    else:
                        envido = suma1(nro_carta2, 20)
                        print(envido)
                else:
                    if nro_carta3 < 10:
                        envido = suma1(nro_carta3, 20)
                        print(envido)
                    else:
                        print(20)
            else:
                print("No tengo puntos")
    else:               
        if nro_carta1 < 10:
            if nro_carta3 < 10:
                envido = suma2(nro_carta1, nro_carta3)
                print(envido)
            else:
                envido = suma1(nro_carta1, 20)
                print(envido)
        else:
            if nro_carta3 < 10:
                envido = suma1(nro_carta3, 20)
                print(envido)
            else:
                print(20)