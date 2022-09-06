Propiedades controladas
-----------------------

Es posible tomar los valores que el usuario nos pasa al inicializar los objetos
(en ``__init__``) y guardarlos en variables privadas. Usamos el guión bajo inicial
en la propiedades para indicar que estas son internas de la clase y que no deberián
ser usadas. Esto es una convención pero no es obligatorio. Python no lanzará un error
si los usuarios de nuestra clase usan estas propiedades privadas.  

.. code-block:: python
    :linenos:
    :emphasize-lines: 3, 4, 8, 12

    class Persona:
        def __init__(self, nombre, apellido):
            self._nombre = nombre
            self._apellido = apellido

        @property
        def nombre(self):
            return self._nombre
        
        @property
        def apellido(self):
            return self._apellido

¿Que es ``@property``?
~~~~~~~~~~~~~~~~~~~~~~

Antes de la definición de una función (esto puede hacerse dentro y fuera de las clases)
es posible agregar lo que llamamos un decorador (o función decoradora). La sintaxis para
hacerlo es simplemente agregar esta línea sobre la definición de una función y comenzarla
con un ``@``. Estos decoradores se usan para modificar a la función de
formas que por el momento exceden lo que necesitamos conocer.  
En particular, ``@property`` es usado por las clases en Python para marcar que una
propiedad **existe** y que la funcion *decorada*
sera la encargada de atender las llamadas de **lectura** de esta propiedad.  
La escritura/modificación de cada propiedad se hace de otra forma.  

Hasta aquí estas propiedades son *solo lectura*

.. code-block:: python
    :linenos:
    :emphasize-lines: 7

    victor = Persona('Victor', 'Fernandez')
    print(victor.apellido)
    # funciona y devule 
    'Fernandez'
    # La siguiente línea fallará porque no esta todavía definido como funcionará
    # la asignación de esta propiedad
    victor.apellido = 'Gonzalez'

A las funciones de una clase para **leer** una propiedad se les llama ``getter``
y las las funciones para escribir un nuevo valor a una propiedad se las llama
``setter`` (por *get* y *set* del ingles: *obtener* y *definir*).  

Formalmente ahora podemos decir que nuestras propiedades ``nombre`` y ``apellido``
tienen ``getter`` pero no ``setter``.  

Veamos un ejemplo de ``setter`` para la propiedad ``nombre`` de la clase ``Persona``:  

.. code-block:: python
    :linenos:
    :emphasize-lines: 3, 4, 8

    @nombre.setter
    def nombre(self, value):
        # Antes de escribir mi variable privada _nombre, revisar que
        # cuampla con los requisitos definidos
        if type(value) != str:
            # Si no es del tipo *string* lanzaremos (raise) un error
            # (excepción) del Tipo Exception (hay otros tipos).
            raise Exception('Nombre inválido. Solo string permitido')
        
        # solo si pasa las validaciones (podrían ser varias)
        # sobreescribimos nuestra variable privada con el nuevo valor.
        self._nombre = value

La función definida para ser ``setter`` debe cumplir las siguientes condiciones:

*  Tener un decorador de la forma ``@NOMBRE_DE_LA_PROPIEDAD.setter``.
*  Tener el mismo nombre que la función ``getter``.
*  Incluir un parámetro para recibir el valor que el usuario quiere definir
   (usualmente lo llamaremos ``value``).

Es posible tambien definir propiedades personalizadas a gusto.  

.. code-block:: python
    :linenos:
    :emphasize-lines: 2, 7

    @property
    def nombre_completo(self):
        """ devuelve el nombre completo """
        return f'{self._nombre} {self._apellido}'

    @property
    def nombre_formal(self):
        """ devuelve el nombre completo """
        return f'{self._apellido}, {self._nombre}'

Estas propiedades solo tienen sentido para ser leidas. Es por esto que no tienen una funcion ``setter``.

Ejemplos de uso:

.. code-block:: python

    juan = Persona('juan carlos', 'perez')
    print(juan.nombre_completo)
    'juan carlos perez'
    print(juan.nombre_formal)
    'perez, juan carlos'
    # Si intento asignar una propiedad que es solo lectura (no tienen una funcion setter)
    # dará un error "can't set attribute" (no se puede asignar esta propiedad)
    juan.nombre_completo = 'Nuevo nombre completo'

Las propiedades ``nombre`` y ``apellido`` se pueden leer y escribir.  
Las propiedades ``nombre_completo`` y ``nombre_formal`` son simplemente combinaciones útiles
de otras propiedades básica. Solo se puede leer.  

Funciones de mi clase
---------------------

Es también posible definir funciones

.. code-block:: python

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

Algunos ejemplos de uso con estas nuevas funciones:  

.. code-block:: python

    juan = Persona('juan carlos', 'perez')
    print(juan.nombre_completo)
    # 'juan carlos perez'
    print(juan.nombre_formal)
    # 'perez, juan carlos'

    enc = juan.encabezado('Sr.', limpiar=False)
    print(enc)
    # 'Sr. juan carlos perez'

    enc = juan.encabezado('Sr.')
    print(enc)
    # 'Sr. Juan Carlos Perez'

    print(juan.nombre)
    # El nombre fue limpiado
    # 'Juan Carlos'

    print(juan.upper())
    # 'JUAN CARLOS PEREZ'

**Nota importante: Las funciones se llaman con los parentesis (y parámetros si se requieren) y las 
propiedades se llaman sin ellos (y no puede requerir parámetros).**  

Código de la clase final
`aquí <https://github.com/avdata99/programacion-para-no-programadores/blob/master/code/01-basics/class-00.py>`_.  

.. include:: /code/01-basics/class-00.py
   :literal:


Tareas
~~~~~~

*  Hacer un PR a la 
   `clase Persona <https://github.com/avdata99/programacion-para-no-programadores/blob/master/code/01-basics/class-00.py>`_
   para agregar la propiedad edad.
*  Hacer un PR a la 
   `clase Carta <https://github.com/avdata99/programacion-para-no-programadores/blob/master/code/01-basics/class-04.py>`_
   para validar que el ``palo`` es string en su función ``setter``.
*  Hacer un PR a la 
   `clase Carta <https://github.com/avdata99/programacion-para-no-programadores/blob/master/code/01-basics/class-04.py>`_
   para validar que el ``numero`` es mayor que cero y menor o igual que 12 en su función ``setter``.

Algunos ejemplos de uso
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /code/01-basics/class-04.py
   :literal:
