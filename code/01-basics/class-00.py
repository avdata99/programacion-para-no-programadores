
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # definir __str__
    # definir lower
    # definitr clean
    # allow init auto_clean


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
