import sqlite3
import os

carpeta = os.path.dirname(os.path.abspath(__file__))
base = '{}/base-de-datos.db'.format(carpeta)
conn = sqlite3.connect(base)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS peliculas2
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre text, 
                director text, 
                anio int)''')

# Insert a row of data
c.execute("INSERT INTO peliculas2 (nombre, director, anio) VALUES ('Martix','Juan Perez', 1971)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.


resultados = c.execute('SELECT * FROM peliculas2')
print('Resultados')
for peli in resultados:
    print('Peli: {}'.format(peli))

conn.close()
print('TERMINADO')