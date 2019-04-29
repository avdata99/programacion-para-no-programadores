from cdatabase import MiBase

mb = MiBase()
mb.execute(query="INSERT INTO peliculas3 (nombre, director, anio) VALUES ('Martix','Juan Perez', 1971)")
resultados = mb.execute(query='SELECT * FROM peliculas3')
print('Resultados')
for peli in resultados:
    print('Peli: {}'.format(peli))

mb.close()
print('TERMINADO')