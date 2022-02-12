""" Herencia """


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def lower(self):
        """ Representacion en minúsculas del nombre completo
            No cambia los valores del objeto real """
        return f'{self.nombre.lower()} {self.apellido.lower()}'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Programador(Persona):

    def __init__(self, nombre, apellido, lenguajes):
        super().__init__(nombre=nombre, apellido=apellido)
        self.lenguajes = lenguajes

    def agregar_lenguaje(self, lenguaje):
        self.lenguajes.append(lenguaje)

juan = Persona(nombre='juan carlos', apellido='perez')
pedro = Programador(nombre='pedro ', apellido='gomez', lenguajes=['Python'])
pedro.agregar_lenguaje('JavaScript')

print(juan.nombre)
# juan carlos
print(pedro.nombre)
# pedro 
print(pedro.lenguajes)
# ['Python', 'JavaScript']
