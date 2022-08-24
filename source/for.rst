Iterando ando: ``for``
======================

En Python algunos objetos se pueden iterar. Esto es: **recorrer su
elementos de uno a la vez**. Muchos objetos tiene definida una forma
de iterarse, por ejemplo las listas.  

Veamos un ejemplo:  

.. code-block:: python

    mi_lista = ["Juan", "Pedro", "María"]

    for persona in mi_lista:
        saludo = f'Hola {persona}!'
        print(saludo)
    print('Iteración terminada')

    """ Imprime
    Hola Juan
    Hola Pedro
    Hola María
    Iteración terminada
    """

Como podemos imaginar, la línea ``print(saludo)`` se ejecuta tres veces.  
Estos es, una por cada uno de los elementos de ``mi_lista``.  
La sentencia ``for`` inicia un loop que **va a terminar cuando se quede
sin elementos que recorrer**.  

Anatomía de un ``for``
----------------------

La línea ``for persona in mi_lista:`` podría traducirse como:
*por cada persona en mi_lista hacer lo siguiente:*  

Analicémosla:

*  La sentencia ``for`` indica que vamos a iniciar una iteración.
*  A continuación se requiere un nombre de variable (en nuestro
   ejemplo ``persona``) para contener cada uno de los elementos de la iteración
   dentro de la porción de código que se va a ejecutar en cada vuelta del bucle.
*  Luego sigue la palabra ``in`` para que esta linea sea fácil de leer y como
   indicador de que vamos a continuar con algún objeto iterable.
*  Finalmente se coloca el objeto sobre el que deseamos iterar.
*  Como todas las líneas que preceden a un bloque de código termina con ``:``.
*  Todo el código que necesitamos que se ejecute para cada uno de los elementos
   debe estar tabulado. **La forma de saber donde termina esta porción de
   codigo es que se termina la tabulación**.
*  Nota: la variable ``persona`` solo está definida dentro del bloque del
   código del ``for``. Fuera de el no está definida y dará un error si se
   intenta usar.

¿Se puede anidar iteraciones?  
Si, claro. Veamos un ejemplo:  

.. code-block:: python

    lista_con_listas = [ [1, 12], [20, 22], [5, 8] ]

    for lista in lista_con_listas:
        for numero in lista:
            print(numero) 

    # imprimirá:
    1
    12
    20
    22
    5
    8

``continue`` y ``break`` en ciclos ``for``
------------------------------------------

Dentro de una iteración, existen formas de salir de
ella (``break``) y de saltearse un elemento (``continue``).  

Veamos un ejemplo:

.. code-block:: python

    # for / continue / break
    paises = ["Argentina", "Brasil", "Chile", "Uruguay", "Venezuela", "Colombia", "Japón"]
    print('Paises')
    for pais in paises:
        if pais == "Chile":
            continue
        print(f" - {pais}")
        if pais == "Venezuela":
            break
    print('FIN')
    """ imprime
    Paises
    - Argentina
    - Brasil
    - Uruguay
    - Venezuela
    FIN
    """    

Algunos elementos no pueden iterarse, por ejemplo los ``int``.  
El error ``'XXX' object is not iterable`` es la forma de informar esto.  

.. code-block:: python

    a = 90
    for x in a:
        print(x)
    
    """ devolverá el error.
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: 'int' object is not iterable
    """

``if`` + ``in``
---------------

Tambien podemos combinar ``if`` con ``in`` para saber si un objeto
esta contenido en una lista. 

.. code-block:: python

    lista = [1, 2, 3]

    if 4 in lista:
        print("4 está en la lista")
    else:
        print("4 no está en la lista")
    # imprime
    # 4 no está en la lista

Iterando *strings*
------------------

Como ya vimos antes, los strings tambien pueden usarse como
listas y por lo tanto se puede iterar.  

.. code-block:: python

    nombre = "Victor"

    for letra in nombre:
        print(letra)
    
    """ imprimirá
    V
    i
    c
    t
    o
    r
    """

Agregado: ``range``
~~~~~~~~~~~~~~~~~~~

Python tiene una funcion (técnicamente no es una función pero
por ahora podemos pensarla como tal) includa (*built-in*) que
permite iterar sobre una serie de números. Se llama ``range``
y podemos ver su funcionamiento con algunos ejemplos.  
Cuando llamamos a ``range`` con un solo un parámetro (siempre numeros)
este devuelve un objeto que se puede iterar. Incluye los números
desde cero hasta el valor pasado como parámetro menos uno
(comportamiento similar a los indices de las listas).  

.. code-block:: python

    for n in range(3):
        print(n)
    # imprimira (en lineas diferentes): 0 1 2

Cuando llamamos a ``range`` con dos parámetros (siempre numeros)
este devuelve un objeto que se puede iterar. Incluye los números
desde el primer parámetro hasta el valor pasado como segundo
parámetro menos uno.  

.. code-block:: python

    for n in range(2, 8):
        print(n)
    # imprimira (en lineas diferentes): 2 3 4 5 6 7

Cuando llamamos a ``range`` con tres parámetros (siempre numeros)
este devuelve un objeto que se puede iterar. Incluye los números
desde el primer parámetro hasta el valor pasado como segundo
parámetro menos uno. El último parámetro indica el tamaño del
salto entre un elemento y otro (por ejemṕlo 2 hará que el
resultado vaya de dos en dos).  

.. code-block:: python

    for n in range(3, 10, 2):
        print(n)
    # imprimira (en lineas diferentes): 3 5 7 9

Tambien es posible convertir el resultado de ``range`` a una lista
(que ya conocemos).  

.. code-block:: python

    pares = range(0, 100, 2)
    lista_pares = list(pares)
    print(lista_pares)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32,
    34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64,
    66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

Tareas
~~~~~~

*  Escribir un programa que:

   *  Incluya al inicio una funcion llamada ``es_par`` y que devuelva
      *verdadero* o *falso* según corresponda
   *  Le solicite al usuario que ingrese una lista de números separados por coma.
   *  Transformarme este texto ingresado a lista con ``split(',')``
   *  Iterere todos ellos e imprima solo aquellos que son pares.

*  Escribir un programa que itere todos los múltiplos de 3 desde el cero
   al 500000 e imprima solo aquellos que además son divisibles (el resto
   de la division es cero) por 13.

*  Escribir un programa que responda estas preguntas:

   *  ¿Cuantos números multiplos de siete menores a 10.000 terminan en *999*?
   *  ¿Cuales son?
