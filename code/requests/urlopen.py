# Ejemplo simple de request HTTP GET usando solo builtins (sin 'with')
from urllib.request import urlopen


url = "http://babel.upm.es/~angel/teaching/pps/quijote.txt"
response = urlopen(url)
texto = response.read()
print(f'La respuesta es del typo {type(texto)}')
texto_utf8 = texto.decode("utf-8")
# print(texto_utf8)
response.close()

palabras = texto_utf8.split()
print("Cantidad de palabras en el texto:", len(palabras))

palabras_info = {}
for palabra in palabras:
    palabra_lower = palabra.lower()
    # ignorar palabras cortas (artículos, preposiciones y conectores)
    if len(palabra_lower) < 5:
        continue
    if palabra_lower in palabras_info:
        palabras_info[palabra_lower]['count'] += 1
    else:
        palabras_info[palabra_lower] = {'count': 1, 'largo': len(palabra_lower)}

print("Cantidad de palabras distintas en el texto:", len(palabras_info))
palabras_mas_comunes = sorted(
    palabras_info.items(),
    key=lambda item: item[1]['count'],
    reverse=True
)[:10]

print("Palabras más comunes:")
for palabra, info in palabras_mas_comunes:
    print(f"  {palabra}: {info['count']} veces")

palabras_mas_largas = sorted(
    palabras_info.items(),
    key=lambda item: item[1]['largo'],
    reverse=True
)[:10]
print("Palabras más largas:")
for palabra, info in palabras_mas_largas:
    print(f"  {palabra}: {info['largo']} caracteres")
