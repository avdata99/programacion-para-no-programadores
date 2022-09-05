Funciones en Python
-------------------

En este curso hemos nombrado y usado sin definir todavia a las *funciones*.  
Una funcion en Python es una porción de código que cumple una tarea determinada
y opcionalmente devuelve un resultado.  

Veamos un ejemplo:

.. code-block:: python

    def segundos_en_un_dia():
        segundos_en_una_hora = 60
        minutos_en_una_hora = 60
        horas_en_un_dia = 24
        segundos_en_un_dia = segundos_en_una_hora * minutos_en_una_hora * horas_en_un_dia
        return segundos_en_un_dia
    
    segundos = segundos_en_un_dia()
    print(segundos)
    86400

Anatomía de una función simple
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*  ``def`` es una palabra reservada de Python (no la podemos usar como nombre de variable)
   que usamos para indicar que estamos definiendo una función.
*  Despues de ``def`` agregamos el nombre de nuestra función. Se deben cumplir las mismas
   reglas que para los nombres de variables (no pueden empezar con números, no pueden tener
   espacios, etc).
*  Despues del nombre de la funcion colocamos parentesis (es obligatorio). En el futuro
   vamos a usarlas para agregar los que se llaman *parámetros*. Por ahora solo es importante
   no olvidar agregarlos.
*  Finalmente agregamos *:* (dos puntos) para indicar que terminamos de definir el encabezado
   de la función y vamos a comenzar con el código.
*  El código de la función debe estar tabulado hacia la derecha. **Esta es una de las grandes
   diferencias que Python tiene con los demás lenguajes de programación**. El código propio de
   la función comienza tabulado y termina cuando el código vuelve a la izquierda. Muchos otros
   lenguajes de programación usan las llaves ``{}`` para delimitar donde empiezan y terminan
   los bloques de código.
*  ``return`` se usa para indicar cual es el valor que devolverá nuestra función cuando sea
   llamada. En este caso es el resultado de un cálculo. No es obligario usarla, a veces simplemente
   necesitamos procesar datos sin entregar resultados.
*  Una vez definida (y terminada anulando la tabulación y volviendo a la izquierda el código),
   una función se puede llamar simplemente con su nombre y los paréntesis.

Funciones con parámetros
~~~~~~~~~~~~~~~~~~~~~~~~

Muchas funciones procesan datos que ya conocemos pero en muchos casos necesitamos que nuestra
función procese datos que pueden variar. Para estos casos necesitamos darle a nuestra funcion
la posibilidad de agregar valores variables llamados *parámetros*.
Estos parámetros se incluyen dentro de los paréntesis del encabezado de nuestra funcion
**separados por comas**.  

Ejemplo de una función con parámetros.

.. code-block:: python

    def sumar(a, b):
        print(f'Se llamo a la funcion sumar con {a} y {b}')
        return a + b

    resultado = sumar(10, 20)
    print(f'Resultado de la suma: {resultado}')
    Resultado de la suma: 30

    resultado = sumar(7, 27)
    print(f'Resultado de la suma: {resultado}')
    Resultado de la suma: 34

    resultado = sumar("10", "20")
    print(f'Resultado de la suma: {resultado}')
    Resultado de la suma: 1020
    # Para pensar: ¿Que sucedió?)

    # ¿Qué pasa si no completamos todos los parámetros esperados?
    sumar(10)

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: sumar() missing 1 required positional argument: 'b'

    # Obtenemos un error. Los parámetros asi como estan definidos son obligatorios.

Nótese que dentros del código de la función los parametros son variables disponibles
para usar libremente. Fuera de ella (por ejemplo tratar de usar ``a`` fuera de la
funcion ``suma``) no estan definidas y darán error. El alcance y validez de ``a``
es solo dentro de la función que la declaró como parámetro.  

Funciones con parámetros opcionales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En algunos casos no necesitamos que todos los parámetros sean obligatorios.
Muchas veces hay valores que son de uso más frecuente y el usuario no querrá
definirlos cada vez que llama a la función.  
Para esto existen parámetros *opcionales*. Simplemente colocamos cual es el
valor predeterminado para los parámetros en el encabezado de la función y
es suficiente.  
Tomemos el ejemplo de la funcion *potencia* y asumamos que en general los
usuarios querrán elevar números al cuadrado.   

.. code-block:: python

    def potencia(a, b=2):
        print(f'Se llamo a la funcion potencia con {a} y {b}')
        return a ** b

    resultado = potencia(3)
    print(f'Resultado de la potencia 3 ** 2: {resultado}')

    resultado = potencia(3, 3)
    print(f'Resultado de la potencia 3 ** 3: {resultado}')

    # Es tambien posible cambiar el orden de los parametros al
    # llamar a la función usando su nombre.
    # Las siguientes opciones devolverán el mismo resultado.
    resultado = potencia(3, 4)
    resultado = potencia(a=3, b=4)
    resultado = potencia(b=4, a=3)

Tareas
~~~~~~

*  Crear una funcion que calcule y devuelva la superficie de un rectangulo
   dados (como parámetros) los valores de sus lados. Usar esta funcion con
   valores ingresados por el usuario con ``input``.
*  Crear una funcion que dados un nombre y un apellido imprima en pantalla
   *"Hola NOMBRE APELLIDO!"*. La función no debe devolver ningun valor.
*  Crear una función que dado un texto pasado como parámetro, devuelva
   el mismo texto pero con todas las vocales cambiadas por un asterisco. 
*  Crear una funcion que dada una temperatura en grados Celsius devuelva
   el equivalente en grados Fahrenheit. Usar esta funcion con
   valores ingresados por el usuario con ``input``. 

**En todos los casos usar la función para asegurarse
que funciona como es esperado.**  

Algunos ejemplos de uso
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /code/01-basics/functions-01.py
   :literal:

.. include:: /code/01-basics/functions-02.py
   :literal:

.. include:: /code/01-basics/functions-03.py
   :literal:

.. include:: /code/01-basics/functions-04.py
   :literal:
