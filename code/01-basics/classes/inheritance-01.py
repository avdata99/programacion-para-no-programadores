from ppt.jugadores import AzarPlayer, PiedraPlayer
from ppt.juego import competir

jugador1=AzarPlayer()
jugador2=PiedraPlayer()

for rondas in range(100):
    jugador1.competir(jugador2)
        
print(f"Gana Jugador {jugador1.name()}: {jugador1.ganados} - Gana Jugador {jugador2.name()}: {jugador2.ganados} - Empates: {jugador1.empatados}")
