Cadenadas de caracteres o *strings* <str>
-----------------------------------------

Las cadenas de caracteres o *strings* son el tipo de dato para almacenar textos.  
Estos son llamados ``str`` en Python.  

.. code-block:: python

    nombre = "Juana Velez"
    # tambien es posible mostrar (imprimir) el contenido
    print(nombre)
    Juana Velez

Nota: Como los textos suelen naturalmente tener espacios es necesario
delimitar donde empiezan y terminan con las ``"`` o ``'`` (comillas simples
o dobles).  

Si intentamos definir una variable de tipo ``str`` sin comillas vamos a
recibir un error de sintaxis.  

.. code-block:: python

    nombre = Juana Velez
      File "<stdin>", line 1
        nombre = Juana Velez
                   ^
    SyntaxError: invalid syntax

Con los *strings* podemos hacer también algunas operaciones en Python.  
La suma en *strings* (se llama *concatenar*) es posible:  

.. code-block:: python

    nombre = "Juana"
    apellido = "Velez"
    
    nombre_completo = nombre + " " + apellido

**Nota: esta suma incluye tres strings, dos tienen nombre y otro es un
espacio definido directamente.**  

La multiplicación tambien esta definida para *strings*:  

.. code-block:: python

    letra = "a"
    letra * 4
    aaaa

Otras funciones disponibles para los *strings*:

.. code-block:: python

    nombre = "Juana Velez"
    # funcion lower -> pasar a minúsculas
    nombre.lower()
    'juana velez'
    # funcion upper -> pasar a mayúsculas
    nombre.upper()
    'JUANA VELEZ'
    # funcion format -> completar las llaves dentro de un string con
    # valores definidos fuera
    saludo = "Hola, {}".format(nombre)
    # otra forma de hacer los mismo (se le llama "f strings")
    saludo = f"Hola, {nombre}"

Los objetos de typo ``str`` tienen muchas propiedades o funciones

Tareas
~~~~~~

Investigar, usar y describir para que sirven las siguientes funciones para objetos
``str`` en Python.  

* ``replace``:
* ``capitalize``:
* ``title``:
* ``strip``:
