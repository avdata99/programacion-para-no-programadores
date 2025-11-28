# Ejemplo simple de request HTTP GET usando solo builtins (sin 'with')
import os
from urllib.request import urlopen


archivo = "code/requests/quijote.txt"
if os.path.exists(archivo):
    f = open(archivo, "r", encoding="utf-8")
    texto_utf8 = f.read()
    f.close()
else:
    url = "http://babel.upm.es/~angel/teaching/pps/quijote.txt"
    response = urlopen(url)
    texto = response.read()
    print(f'La respuesta es del typo {type(texto)}')
    texto_utf8 = texto.decode("utf-8")
    print(texto_utf8)
    response.close()

    f = open("code/requests/quijote.txt", "w", encoding="utf-8")
    f.write(texto_utf8)
    f.close()

palabras = texto_utf8.split()
print("Cantidad de palabras en el texto:", len(palabras))
