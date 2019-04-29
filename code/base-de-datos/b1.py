import sqlite3
import os

class MiBase:

    def __init__(self, base_name='base-de-datos.db'):
        carpeta = os.path.dirname(os.path.abspath(__file__))
        self.base_name = base_name
        self.base_path = '{}/{}'.format(carpeta, self.base_name)
        self.connect()
    
    def connect(self):
        self.connection = sqlite3.connect(self.base_path)
        self.cursor = self.connection.cursor()
        # Create table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas3
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            nombre text, 
                            director text, 
                            anio int,
                            momento DATETIME DEFAULT CURRENT_TIMESTAMP)''')


    def execute(self, query):
        ret = self.cursor.execute(query)
        self.connection.commit()
        return ret
    
    def close(self):
        self.connection.close()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.

mb = MiBase()
mb.execute(query="INSERT INTO peliculas3 (nombre, director, anio) VALUES ('Martix','Juan Perez', 1971)")
resultados = mb.execute(query='SELECT * FROM peliculas3')
print('Resultados')
for peli in resultados:
    print('Peli: {}'.format(peli))

mb.close()
print('TERMINADO')