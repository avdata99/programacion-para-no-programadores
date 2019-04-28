import requests
import os

carpeta = os.path.dirname(os.path.abspath(__file__))
path_libro = '{}/florante.txt'.format(carpeta)
if os.path.exists(path_libro):
    f = open(path_libro, 'r')
    text = f.read()
    f.close()
    print('Leyendo archivo local')
else:
    print('DESCARGANDO LIBRO')
    url = 'http://www.gutenberg.org/cache/epub/15531/pg15531.txt'
    req = requests.get(url)
    text = req.text
    f = open(path_libro, 'w')
    f.write(text)
    f.close()

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
omitir = ['de', 'la', 'y', 'en', 'que', 'el', '', 'a', 'los', 'del', 'no',
            'las', 'por', 'se', 'su', 'con', 'mi', 'es', 'al', 'the', 'un',
            'una', 'of', 'para', 'como', 'o', 'lo', 'sus', 'más', 'si', 'me',
            'sin', 'and', 'to', 'ang', 'tu', 'ya', 'you']
for palabra in text.split(' '):
    palabra = palabra.lower()
    if palabra in omitir:
        continue
    if palabra not in palabras.keys():
        palabras[palabra] = 0
    
    palabras[palabra] += 1

letras = sorted(palabras.items(), key=lambda x: x[1], reverse=True)

print(letras[:20])