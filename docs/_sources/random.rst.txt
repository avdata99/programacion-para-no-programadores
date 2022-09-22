Librerías incluida: ``random``
==============================

Asi como hay funciones incluidas (*built-ins*) que se pueden usar sin
estar declaradas tambien hay más herramientas de Python disponibles pero
que requieren ser *importadas*.  

Importar (con el comando ``import`` o de la forma ``from X import Y``)
en Python es disponibilizar nueva herramientas (fuenciones y otras) en
nuestro código.  

Python al azar: ``random``
--------------------------

El módulo ``random`` incluye una serie de funciones que permiten
darle aleatoriedad a nuestro código.  

Veamos un ejemplo. La funcion ``randint`` genera numeros al alzar
entre dos valores pasados como parámetros.  

.. code-block:: python

    from random import randint

    al_azar = randint(1, 100)
    print(al_azar)
    
    # otra forma de usarlo podría ser
    import random
    al_azar = random.randint(1, 100)
    print(al_azar)

Asi como el ``.`` se usa en ``objeto.propiedad`` tambien se usa
en ``modulo.objeto_en_modulo``.  

``choice``: Elegir un opción al azar de una lista.
--------------------------------------------------

La función ``choice`` recibe como parámetro una lista de la cual
devolverá un elemento al azar.  

.. code-block:: python

    from random import choice

    opciones = ["piedra", "papel", "tijeras"]
    opcion_elegida = choice(opciones)
    print(opcion_elegida)
    # tijeras

``shuffle``: Mezclar una lista
------------------------------

Otra función del módulo ``random`` es ``shuffle`` que recibe una lista
como parámetro y la desordena aleatoriamente.  

Ejemplo:  

.. code-block:: python

    from random import shuffle

    mazo = [
        {"numero": 1, "palo": "espada"},
        {"numero": 2, "palo": "espada"},
        # ...
        {"numero": 11, "palo": "oro"},
        {"numero": 12, "palo": "oro"},
    ]
    suffle(mazo)
    print(mazo[0])
    # {"numero": 11, "palo": "oro"}

Tareas
~~~~~~

*  Escribir un programa que elija un numero al azar entre 1 y _N_ (el numero que quieras, puede ser 10 por ejemplo) y
   le pida al usuario que lo adivine. El programa debe decirle al usuario si el numero que ingresó es mayor o menor
   al numero que se eligió al azar. El programa debe terminar cuando el usuario adivine el numero elegido al azar.

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 045 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-045/ejercicio.py>`_
    (contenido en este repositorio)

.. include:: /ejercicios/ejercicio-045/ejercicio.py
   :literal:

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 046 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-046/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-046/ejercicio.py
   :literal:

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 047 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-047/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-047/ejercicio.py
   :literal:
