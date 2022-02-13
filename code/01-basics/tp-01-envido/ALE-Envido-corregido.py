import random


#jugador1=[{'numero': 1, 'palo': 'copa'}, {'numero': 3, 'palo': 'copa'}, {'numero': 7, 'palo': 'copa'}]
#flor=True
#jugador2=[{'numero': 1, 'palo': 'espada'}, {'numero': 6, 'palo': 'basto'}, {'numero': 5, 'palo': 'espada'}]
#flor=False

#Si activan esta prueba deben anular repartir() y si reparten flor coloquen la vandera que corresponda al jugador!!

flor=False

def mezclar():
    mazo=[]
    palos=["oro","basto","copa","espada"]
    numeros=[1,2,3,4,5,6,7,10,11,12]
    for palo in palos:
        for numero in numeros:
            dictioresult={"numero": numero ,"palo": palo}
            mazo.append(dictioresult)

    random.shuffle(mazo)    #Con esta función mezclamos el mazo
    return mazo

def repartir(mazo):
    jugador1 = []
    jugador2 = []
    cont=1
    for carta in mazo:
        if cont%2==1:
            jugador1.append(carta)
        else:
            jugador2.append(carta)
        cont+=1
        
        if cont==7:
            break
    
    return jugador1, jugador2

def cartas_recibidas(jugador):
    
    p1=jugador[0].get("palo")
    v1=jugador[0].get("numero")
    p2=jugador[1].get("palo")
    v2=jugador[1].get("numero")
    p3=jugador[2].get("palo")
    v3=jugador[2].get("numero")
    
    cartas=f"{v1} de {p1}, {v2} de {p2} y {v3} de {p3}"
    
    return cartas
    
def calcular_envido(jugador):

    envido=0
    
    p1=jugador[0].get("palo")
    v1=jugador[0].get("numero")
    p2=jugador[1].get("palo")
    v2=jugador[1].get("numero")
    p3=jugador[2].get("palo")
    v3=jugador[2].get("numero")

    if p1 == p2:
        if v1<8 and v2<8:
            envido=20+v1+v2
        elif v1>7 and v2>7:
            envido=20
        elif v1>7 and v2<8:
            envido=20+v2
        else:
            envido=20+v1
    elif p1==p3:
        if v1<8 and v3<8:
            envido=20+v1+v3
        elif v1>7 and v3>7:
            envido=20
        elif v1>7 and v3<8:
            envido=20+v3
        else:
            envido=20+v1
    elif p2==p3:
        if v2<8 and v3<8:
            envido=20+v2+v3
        elif v2>7 and v3>7:
            envido=20
        elif v2>7 and v3<8:
            envido=20+v3
        else:
            envido=20+v2
    else:
        envido=max(v1,v2,v3)

    if p1 == p2 == p3:
        if v1>7 and v2<8 and v3<8:
            envido=20+v2+v3
        elif v1>7 and v2>7 and v3<8:
            envido=20+v3
        elif v1<8 and v2>7 and v3<8:
            envido=20+v1+v3
        elif v1<8 and v2<8 and v3>7:
            envido=20+v1+v2
        elif v1<8 and v2>7 and v3>7:
            envido=20+v1
        elif v1>7 and v2<8 and v3>7:
            envido=20+v2
        elif v1<8 and v2<8 and v3<8:
            envido=20+v1+v2+v3
        else:
            envido=20
        flor=True
        print("Este jugador tiene flor!!!")

    return envido


print("Mezclamos el mazo")
mazo = mezclar()

print("Repartimos las cartas")
jugador1, jugador2 = repartir(mazo)

cartas1=cartas_recibidas(jugador1)
cartas2=cartas_recibidas(jugador2)

puntos_jugador1=calcular_envido(jugador1)
puntos_jugador2=calcular_envido(jugador2)

print("El jugador 1 grita envido! (Puede estar mintiendo...)")

print(f"Cartas del jugador 1: {cartas1} con un total de {puntos_jugador1} puntos")

if puntos_jugador2 > puntos_jugador1:
    print("El jugador 2 acepta!")
    print(f"Cartas del jugador 2: {cartas2} con un total de {puntos_jugador2} puntos")
else:
    print("El jugador 2 se va al mazo (y muestra las cartas aunque no es necesario)")
    print(f"Cartas del jugador 2: {cartas2} con un total de {puntos_jugador2} puntos")


if puntos_jugador1>= puntos_jugador2:
    print(f"Ganó el jugador 1 con {puntos_jugador1} puntos")
else:
    print(f"Ganó el jugador 2 con {puntos_jugador2} puntos")

