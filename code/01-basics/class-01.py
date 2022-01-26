
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def revisar_nombre(self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

juan = Persona(nombre='juan', apellido='perez')
pedro = Persona(nombre='pedro', apellido='gomez')

print(f"Nombre: {juan.nombre}")
print(f"Apellido: {juan.apellido}")
print('---- CORRIGIENDO ----')
juan.revisar_nombre()
print(f"Nombre: {juan.nombre}")
print(f"Apellido: {juan.apellido}")

print(juan)
# Muestra: Juan Perez
# Sin __repr__ muestra <__main__.Persona object at 0x7f63d28b2be0>

print(pedro)  # sin revisar
# Muestra: pedro gomez
print(type(pedro))
# Muestra: <class '__main__.Persona'>

print(type(juan))
# Muestra lo mismo, son del mismo tipo: <class '__main__.Persona'>
