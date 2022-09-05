
class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if type(value) != str:
            raise Exception('Nombre inválido. Solo string permitido')
        self._nombre = value

    @property
    def apellido(self):
        return self._nombre

    @nombre.setter
    def apellido(self, value):
        if type(value) != str:
            raise Exception('Apellido inválido. Solo string permitido')
        self._nombre = value

    @property
    def nombre_completo(self):
        """ devuelve el nombre completo """
        return f'{self._nombre} {self._apellido}'

    @property
    def nombre_formal(self):
        """ devuelve el nombre completo en modo formal """
        return f'{self._apellido}, {self._nombre}'

    def limpiar(self):
        """ Mejorar el nombre y el apellido """
        self._nombre = self._nombre.strip().title()
        self._apellido = self._apellido.strip().title()

    def encabezado(self, titulo, limpiar=True):
        """ Genera y devuelve el nombre completo con
            "Sr." "Sra." o algun otro titulo.
            Opcionalmente se puede limpiar el nombre """
        # limpiar el nombre si se solicita
        if limpiar:
            self.limpiar()
        return f'{titulo} {self.nombre_completo}'

    # podemos tambien emular el comportamiento de los strings
    # e incluso copiar nombres de funciones de ellos
    def lower(self):
        """ devuelve el nombre completo en minusculas """
        return self.nombre_completo.lower()

    def upper(self):
        """ devuelve el nombre completo en minusculas """
        return self.nombre_completo.upper()
