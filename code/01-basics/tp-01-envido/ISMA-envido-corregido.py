
palos={
    'Oro':'1',
    'basto':'2',
    'Espada':'3',
    'Copa':'4',

}
figura=[10,11,12]

palo=[0,0,0,0]
cartas=[0,0,0,0]

for orden in ['primera', 'segunda', 'tercera']:

    print(f"ingrese el numero de la {orden} carta")
    numero=int(input())

    print(f"ingrese el palo segun corresponda:")
    for x in palos:
        print(x,":",palos[x])

    posicion=int(input())
    palo[posicion-1]+=1

    if numero in figura:
        cartas[posicion-1]+=0
    else:
        cartas[posicion-1]+=numero

# ver si el 2 esta en palo (o sea, hay 2 cartas de un mismo palo)
if 2 in palo:
    # ver en que indice esta un elemento especifico
    palo_con_dos_cartas = palo.index(2)
    tanto = cartas[palo_con_dos_cartas] + 20
else:
    tanto = max(cartas)
print(f"tiene {tanto} tantos para el envido")
