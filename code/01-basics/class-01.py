
class Persona:
    def __init__(self, nombre, apellido, auto_corregir=True):
        self.nombre = nombre
        self.apellido = apellido
        if auto_corregir:
            self.corregir_nombre()

    def corregir_nombre(self):
        """ Asegurarse que el nombre y el apellido empiecen 
            con mayúscula y no tengan espacios al principio
            o al final
        """
        self.nombre = self.nombre.strip()
        self.apellido = self.apellido.strip()
        self.nombre = self.nombre.title()
        self.apellido = self.apellido.title()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

juan = Persona(nombre='juan carlos', apellido='perez')
pedro = Persona(nombre='pedro', apellido='gomez', auto_corregir=False)

print(f"Nombre: {juan.nombre}")
print(f"Apellido: {juan.apellido}")

print(f"Nombre: {juan.nombre}")
print(f"Apellido: {juan.apellido}")
print('---- CORRIGIENDO ----')
pedro.corregir_nombre()

print(juan)
print(pedro)
