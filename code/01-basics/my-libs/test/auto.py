class Auto:
    def __init__(self, marca, modelo):

        self._marca = marca
        self._modelo = modelo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        if type(value) != str:
            raise Exception(f'La marca "{value}" no es válida.')
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        if type(value) != int:
            raise Exception(f'El modelo "{value}" no es válido.')
        self._modelo = value

    def __str__(self):
        return f"<Auto {self._marca} {self._modelo}'>"
