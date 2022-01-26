# grabar un archivo de texto

texto = "Hola"
f = open("archivo.txt", "w")
f.write(texto)
f.close()

# --------------------
# leer un archivo

f = open("archivo.txt")  # predeterminado lo abre para lectura
texto_leido = f.read()
f.close()

print(f"Texto leido: {texto_leido}")
