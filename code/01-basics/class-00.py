
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # def __str__(self):
    #     return f'{self.nombre} {self.apellido}'


juan = Persona(nombre='juan carlos', apellido='perez')
pedro = Persona(nombre='pedro ', apellido='gomez')
luis = Persona(nombre='Luis', apellido='Velez ')

print(juan.nombre)
print(pedro.apellido)
print(f'{luis.nombre} {luis.apellido}')

pedro.nombre = 'Pedro'
print(pedro.nombre)

juan.nombre = juan.nombre.title()
print(juan.nombre)

# print(juan)
# print(pedro)
# print(luis)
