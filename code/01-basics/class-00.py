class Persona:
    def __init__(self, nombre, apellido, edad, pais, ciudad):
            
        self._nombre= nombre
        self._apellido=apellido
        self._edad= edad
        self._pais=pais
        self._ciudad=ciudad
        self.validate()
    
    @property
    def nombre(self):
        return self._nombre.capitalize()

    @nombre.setter
    def nombre(self, value):
        if type(value) != str:
            raise Exception (f'El nombre {value} no es valido, introduzca solo nombre con letras')
        self._nombre = value    

    @property
    def apellido(self):
        return self._apellido.capitalize()

    @apellido.setter
    def apellido(self, value):
         if type(value) != str:
            raise Exception (f'El apellido {value} no es valido, introduzca solo apellido con letras')
         self._apellido = value  

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
         if type(value) != int:
            raise Exception (f'La edad {value} es INCORRECTA, introduzca la edad en numeros solamente')
         self._edad = value  

    @property
    def pais(self):
        return self._pais.capitalize()

    @pais.setter
    def pais(self, value):
         if type(value) != str:
            raise Exception (f'El pais {value} es invalido, introduzca el pais solo con letras')
         self._pais = value      

    @property
    def ciudad(self):
        return self._ciudad.cappitalize() 

    @ciudad.setter
    def ciudad(self, value):
         if type(value) != str:
            raise Exception (f'La ciudad {value} no es correcta, introduzca solo ciudades escritas con letras')
         self._ciudad = value

    def validate (self):
        if type(self._nombre) != str:
            raise Exception('el nombre debe ir escrito con letras')        
        
        if type(self._apellido) != str:
            raise Exception('el apellido debe ir escrito con letras')        
        
        if type(self._edad) != int:
            raise Exception('la edad debe ir con numeros enteros')
        
        if type(self._pais) != str:
            raise Exception('el pais debe ir escrito con letras')        
        
        if type(self._ciudad) != str:
            raise Exception('la ciudad debe ir escrito con letras')
    
    def imprimir_datos (self):
        datos= f' -Nombre completo: {self._nombre} {self._apellido} /n -Su edad es: {self._edad}/n -Vive en: {self._pais} {self._ciudad} '
        print(datos)         

lista = [
    Persona('james', 'smith', 40, 'estados unidos', 'chicago'),
    Persona('ana julia', 'valdez', 25, 'mexico', 'guadalajara'),
    Persona('Helena', 'Dominguez', 19, 'Ecuador', 'Machala')
] 
               