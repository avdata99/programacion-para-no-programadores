from urllib.request import urlopen
# La libreria urllib de Python permite trabajar con URLs
# y descargar contenido desde la web.
# "urlopen" abre una URL y devuelve una respuesta (lo que devuelve el sitio de internet en esa URL).
# De esa respuesta se puede leer el contenido (por ejemplo, el HTML de una página web o un archivo de texto).
# Este programa toma un libro en formato texto disponible en internet.


# quijote_url = "http://babel.upm.es/~angel/teaching/pps/quijote.txt"
# martin_fierro_url = "https://www.gutenberg.org/cache/epub/14765/pg14765.txt"
martin_fierro_url = "https://raw.githubusercontent.com/avdata99/programacion-para-no-programadores/refs/heads/master/code/requests/martin_fierro.txt"

# Abrir la URL y obtener la respuesta del servidor
response = urlopen(martin_fierro_url)
# Asignar a una variable el contenido leído de la respuesta
texto = response.read()
# Es necesario cerrar la respuesta para liberar recursos
response.close()

# La funcion "urlopen" devuelve una respuesta que al leerse devuleve contenido en typo "bytes"
print(f'La respuesta es del tipo {type(texto)}')

# En Python, las variables tipo "bytes" son una secuencia de valores numéricos que representan
# datos binarios. Para convertir esos datos a texto legible, es necesario decodificarlos
# usando la codificación adecuada (en este caso, UTF-8).
texto_utf8 = texto.decode("utf-8")

# print("\n\n\n--- Texto decodificado (UTF-8) ---\n\n\n")
# print(texto_utf8)

print(f'\n\nLargo del texto: {len(texto_utf8)} caracteres')
palabras = texto_utf8.split()
# palabras (lista) almacena todas las palabras del texto usando la funcion "split" de los strings.
print("Cantidad de palabras en el texto:", len(palabras))

# Tarea: iterar todas las palabras y contar cuántas veces aparece cada una.
# Almacenar los resultados en un diccionario de la forma:
# {
#   "palabra1": 17,
#   "palabra2": 2,
#   ...
# }
