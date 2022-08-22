Booleanos <bool> + operadores de comparación + ``ìf``
=====================================================

El tipo de datos ``<bool>`` (nombrados así en memoria de matemático inglés
George Boole) solo usa dos valores: ``True`` y ``False`` (*verdadero* y *falso*).  
Es el tipo de datos más simple y uno de los más usados.  
Se puede asignar directamente o puede ser el resultado de una comparación.  
Los operadores de comparación en Python son:

*  ``==``: Compara si dos variables valen lo mismo. 
*  ``!=``: Compara si dos variables son distintas. En general en signo ``!``
   se usa para negar. Podemos pensar a este operador como *no igual*.  
*  ``>`` y ``<``: Compara si una variable es mayor o menor que otra.  

Para los números estas comparaciones son fáciles de intuir pero pueden significar
diferentes cosas para diferentes tipos de datos. Como vimos antes en las
funciones ``max`` y ``min`` usadas para *strings*, las comparaciones son alfabeticas.  
Es por esto que en Python podemos decir que 'alpha' < 'beta' es ``True``.  

Veamos algunos ejemplo con código.  

.. code-block:: python

    # "a" es igual a uno.
    a = 1
    b = 2

    # ¿Es "a" igual a 1?
    a == 1
    # Si, es verdadero
    True

    # ¿Es "a" mayor que "b"?
    a > b
    # No, es falso
    False

    # ¿Es "a" distinto de "b"?
    a != b
    # Si, es verdadero
    True

Control de flujo -> ``if / elif / else``
----------------------------------------

El flujo de un programa no tiene que ser siempre lineal.  
Diferentes porciones de código pueden ejecutarse si alguna condicion esperada se cumple.  
Para esto existe la sentencia ``if`` (traducido, es el *si* condicional del español).  

Veamos su funcionamiento con simples ejemplos:

``if``
~~~~~~

Uso de ``if`` solo:

.. code-block:: python
    
    a == 1
    if a > 0:  # nótese que la línea debe terminar en ":" como las funciones
        print('"a" es mayor que cero')

**Nota importante: la porción de código a ejecutaerse *si* se cumple la condición
debe estar tabulada (tal como lo hacemos en las funciones).**  

``else``
~~~~~~~~

Opcionalmente, podemos usar ``else`` para capturar los casos que no cumplen la condición.  

.. code-block:: python
    
    edad = 33
    if edad >= 18:
        print('Es mayor de edad')
        prohibir_entrada = False
    else:
        print('No es mayor de edad')
        prohibir_entrada = True

**Nota importante: Las tabulaciones definen el inicio y el fin de las porciones
de código a ejecutar según la condición. Puede ser más de una línea.**  

``elif``
~~~~~~~~

Entre ``if`` y ``else`` podemos usar uno o varios ``elif`` para identificar mas casos buscados.  
Nota: ``elif`` es una forma abreviada para ``else if``.  

Veamos un ejemplo un poco mas complejo de una función que usa ``if/elif/else``.  

.. code-block:: python
    
    def identificar_bicho(patas):
        if patas == 6:
            print('Es un insecto')
        elif patas == 8:
            print('Es un arácnico')
        else:
            print('Bicho no identificado')

    identificar_bicho(6)
    'Es un insecto'
    identificar_bicho(8)
    'Es un arácnico'
    identificar_bicho(5)
    'Bicho no identificado'

``and`` y ``or``
~~~~~~~~~~~~~~~~

Si queremos consultar mas de una condicón simultanemante podemos
usar ``and`` u ``or`` (*y* u *o*).  

Por ejemplo:

.. code-block:: python
    
    a = 1
    b = 2

    if a == 2 or b == 2:
        print('"a" o "b" valen dos (pueden ser ambos o cualquiera de los dos')

    if a == 2 and b == 2:
        print('"a" Y "b" valen dos')

Tareas
~~~~~~

*  Escribir una función que se llame ``es_par`` y que dado un número devuelva
   ``True`` o ``False`` según corresponda. Tip: Los numeros pares tienen resto
   cero al dividirlos por 2.  
*  Escribir una función que reciba 3 parametros: ``nombre``, ``edad`` y ``termino_secundario``.
   Si la edad es mayor que 18, ``termino_secundario`` es ``True`` y el nombre termina (tip:
   función ``endswith`` de los *strings*) con "s" devuelve ``True``. En cualquier otro caso,
   devuelve ``False``.
