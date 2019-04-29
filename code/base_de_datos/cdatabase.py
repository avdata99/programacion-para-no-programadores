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