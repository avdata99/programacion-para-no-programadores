Números enteros <int>
=====================

Desde la consola interactiva de Python podemos usar numeros enteros.  
Estos son llamados ``int`` en Python (vienen de *Integer* en inglés).  
Con los enteros podemos hacer operaciones de cálculo básicas en Python.  

.. code-block:: python

    edad = 31
    calculo = 291 + 56 - 12
    # tambien es posible mostrar (imprimir) el resultado simplemente escribiendo
    # el nombre de la variable que deseamos conocer
    calculo
    355
    # fuera de la consola interactiva, es necesario usar la funcion "print" para
    # mostrar el valor contenido en una variable
    print(calculo)
    355
    
    una_multiplicacion = 3 * 4
    potencia = 2 ** 3  # ** hace calculos de potencias, en este caso: 2 al cubo
    division = 8 / 4

    resto = 5 % 2  # (calcula el resto de la division, en este caso 5/2 es 2 con resto 1)

Nota: Las palabras a la izquierda del signo igual son los nombres que elegimos
para nuestras variables. Son arbitrarios y no representan nada más que un nombre
interno, no tienen un significado especial para Python.  

Es tambien posible usar las variables para hacer cálculos

.. code-block:: python

    unidades = 3
    precio = 11
    precio_final = unidades * precio

    # Mostrar resultado
    precio_final
    33

En Python, todo es un *objeto*. El concepto de *objeto* lo vamos a ver en profundidad más adelante.  
Por lo pronto diremos que un *objeto* en Python es un elemento que tiene propiedades (también
llamados *atributos*) y funciones.  

Por ejemplo, en el código anterior la variable *unidades* (definida en la linea que dice
``unidades = 3``) es en realidad un *objeto* de tipo ``int``.  

Los objetos de typo ``int`` no tienen muchas propiedades y funciones
A mono de ejemplo, la funcion ``bit_length`` permite saber el numero
de dígitos que este número tiene en su versión binaria.  

.. code-block:: python

    unidades = 3
    unidades.bit_length()
    2 # sería = 11 en binario (2 digitos binarios)
    # Es tambien posible asignar el resultado de esa funcion a una variable
    bits_en_unidades = unidades.bit_length()
    # ver el resultado
    bits_en_unidades
    2

**Nota importante: La forma de llamar a las propiedades y funciones de un
objeto es usando el . (punto)**.  
Se hace de la forma ``objeto.propiedad`` o ``objeto.funcion()``.  
**Nótese que para llamar a las funciones son necesarios los paréntesis.**  

Si tenes curiosidad por conocer todas las propiedades y funciones de un *objeto*
(del tipo que sea) podes usar la funcion ``__dir__()``

.. code-block:: python

    unidades = 3
    unidades.__dir__()
    ['__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__',
     '__ne__', '__gt__', '__ge__', '__add__', '__radd__', '__sub__', '__rsub__',
     '__mul__', '__rmul__', '__mod__', '__rmod__', '__divmod__', '__rdivmod__',
     '__pow__', '__rpow__', '__neg__', '__pos__', '__abs__', '__bool__', '__invert__',
     '__lshift__', '__rlshift__', '__rshift__', '__rrshift__', '__and__', '__rand__',
     '__xor__', '__rxor__', '__or__', '__ror__', '__int__', '__float__', '__floordiv__',
     '__rfloordiv__', '__truediv__', '__rtruediv__', '__index__', '__new__',
     'conjugate', 'bit_length', 'to_bytes', 'from_bytes', 'as_integer_ratio',
     '__trunc__', '__floor__', '__ceil__', '__round__', '__getnewargs__', '__format__',
     '__sizeof__', 'real', 'imag', 'numerator', 'denominator', '__doc__', '__str__',
     '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__reduce__',
     '__subclasshook__', '__init_subclass__', '__dir__', '__class__']

No te preocupes por esa larga lista y por todos esos guiones bajos,
gradualmete iremos comprendiendo de que se tratan.  

Tareas
~~~~~~

Calcular cuantos segundos tiene un día definiendo las variables:

*  ``segundos_en_minuto``
*  ``minutos_en_hora``
*  ``horas_en_dia``

Finalmente asignar el resultado a una variable llamada ``segundos_en_dia``
