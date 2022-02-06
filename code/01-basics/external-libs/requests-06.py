"""
Descargar un libro en formato texto y analizar 
algunos detalles generales de su contenido
"""

import requests
import os

path_libro = 'florante.txt'
if not os.path.exists(path_libro):    
    print('DESCARGANDO LIBRO')
    url = 'http://www.gutenberg.org/cache/epub/15531/pg15531.txt'
    req = requests.get(url)
    f = open(path_libro, 'w')
    f.write(req.text)
    f.close()

f = open(path_libro, 'r')
text = f.read()
f.close()
print('Leyendo archivo local')

print('Largo del texto {}'.format(len(text)))
print('Primeras 30 letras: {}'.format(text[:30]))
print('Ultimas 30 letras: {}'.format(text[-30:]))

# analizar letras
print('-------------------------------')
print('Letras mas usadas')
print('-------------------------------')
letras = {}
for letra in text:
    letra = letra.lower()
    if letra not in letras.keys():
        letras[letra] = 0
    
    letras[letra] += 1

letras = sorted(letras.items(), key=lambda x: x[1], reverse=True)

print(letras[:10])


# analizar palabras
print('-------------------------------')
print('Palabras mas usadas')
print('-------------------------------')
palabras = {}
for palabra in text.split(' '):
    palabra = palabra.lower()
    if len(palabra) < 5:  # omitir las palabras cortas
        continue
    if palabra not in palabras.keys():
        palabras[palabra] = 0
    
    palabras[palabra] += 1

letras = sorted(palabras.items(), key=lambda x: x[1], reverse=True)

print(letras[:20])