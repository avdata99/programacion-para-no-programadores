Funciones incluidas en Python
-----------------------------

Así como nosotros definimos nuestras propias funciones, Python ya incluye
algunas funciones. Ya hemos usado una de ella en nuestros códigos de
ejemplo: ``print``.  

Estas funciones incorporadas y disponibles en Python se las conoce como *built-ins*.  

La funcion ``print`` simplemente *imprime* en nuestra terminal cualquier
valor que se le pase como parámetro.  

Algunos ejemplos:

.. code-block:: python

    print('Hola')
    nombre = 'Juan'
    print(nombre)

Pero ``print`` no es la única función disponible, son muchas.  

Nota: La lista de todas las funciones built-ins de Python esta disponible 
`aquí <https://docs.python.org/3/library/functions.html>`_.  

Algunos ejemplos:

.. code-block:: python

    # abs -> obtener el valor abosoluto de un numero
    abs(-3)
    3
    # len -> obtener el largo de un objeto. No disponible para cualquier
    # objeto. En el caso de los strings, cuenta las letras
    len('hola')
    4
    nombre = 'Victor'
    len(victor)
    6
    # type -> devuelve el tipo de un objeto
    type('hola')
    # devuelve <class 'str'>
    type(nombre)
    # devuelve <class 'str'>
    # max y min -> devuelven el elemento maximo y minimo de una lista de elementos
    max(3, 5, 15, 1)
    15
    min(3, 5, 15, 1)
    1
    # en caso de strings, max y min resuelven ordenando alfabéticamente.
    max("hola", "chau")
    'hola'

Tareas
~~~~~~

*  Escribir una función que dadas tres palabras devuelva el
   largo total de todas ellas juntas. Por ejemplo (si la funcion se llamara
   ``largo_total``) la llamada ``largo_text('hola', 'chau', 'tercera')``
   debe devolver 15.
*  Escribir una función que dados dos números devuelva el valor
   absoluto del menor de ambos.

**En todos los casos usar la función para asegurarse
que funciona como es esperado.**  
