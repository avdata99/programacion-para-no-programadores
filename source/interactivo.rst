Escribiendo nuestro primer código
=================================

Cuando programamos parte de nuestro trabajo es tomar datos de entrada,
procesarlos y finalmente transformarlos en datos de salida que necesitamos.  
Esta es una parte muy importante de nuestro trabajo como programadores. Es por
esto que todos los lenguajes de programación incluyen formas de procesar datos
de diferentes tipos.  

En Python (y en casi todos los lenguajes de programación) se utiliza el
operador `=` como forma de asignar un valor (el de la izquierda) a una *variable*
(a la derecha). De tal forma el código.  

.. code-block:: python

    a = 1

quiere decir: *asignar el valor 1 a la variable llamada* `a`.  
Si mas adelante en el código usamos `a` nos estaremos refiriendo a su contenido: *1*.  
Entonces ...

.. code-block:: python

    b = a + 1

quiere decir *asignar el valor a+1 a la variable llamada* `b`.  
En este caso `b` será igual a 2 (1+1).  

¿Qué es una variable?
---------------------

Las *variables* son los instrumentos que usan los lenguajes de programación para
almacenar datos de diferentes tipos.  
Deben tener un identificador o nombre (en los ejemplos anteriores `a` y `b`).  

Estos identificadores deben ser letras, números y el símbolo *_* (guión bajo) con estos límites:

 - no puede tener espacios.
 - no empezar con un número (si puede usarse despues del primer caracter).
 - no puede ser una palabra que Python ya tiene reservado para otras funciones como `if`, `for`, etc.  

De tal forma, los siguientes identificadores de variables son válidos:

 - `nombre`
 - `n3`
 - `nombre_y_apellido`
 - `_dato_privado`
 - `f910293`

y los sigiuentes no son válidos:

 - `3n` (no se puede empezar con números)
 - `while`  (es una palabra reservada de Python)
 - `nombre apellido` (no se pueden usar espacios)

Los siguientes son ejemplo de uso de los tipos básicos de datos de los que
disponemos en Python.  
