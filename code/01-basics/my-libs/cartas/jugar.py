from pycards.truco.mazos import MazoTruco
from pycards.truco.manos import ManoTruco


tr = MazoTruco()
mn = ManoTruco()

carta1 = tr.entregar_carta()
mn += carta1
carta2 = tr.entregar_carta()
mn += carta2
carta3 = tr.entregar_carta()
mn += carta3

print(f'Mano: {mn}')
print(f'Envido: {mn.envido()}')