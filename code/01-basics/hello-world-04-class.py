
class Saludador:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def saludar(self):
        print(f"Hello world {self.nombre} de {self.pais}!")

saludador = Saludador("Juan", "Argentina")
saludador.saludar()
# Hello world Juan de Argentina!

saludador.nombre = "Luis"
saludador.saludar()
# Hello world Luis de Argentina!

# otra instancia
saludador2 = Saludador("Pedro", "Chile")
saludador2.saludar()
# Hello world Pedro de Chile!
