Diccionarios: ``dict``
======================

Los diccionarios en Python son una estructura de datos preparadas para almacenar
colecciones de elementos (separados por coma) compuestos de una clave y un valor
(suele llamarlos en ingles *key*, *value*).  
Los diccionarios se delimitan con llaves ``{}``.  

Veamos un ejemplo:  

.. code-block:: python

    persona = {
        "nombre": "Luis",
        "apellido": "Colon",
        "edad": 32
    }
    type(persona)
    # devuelve <class 'dict'>

Los valores pueden accederse directamente desde sus claves.  
Esto es así tanto para leer como para modificar cada elemento.  
Las claves son únicas, no puede haber dos elementos con la misma clave.  

.. code-block:: python

    persona = {
        "nombre": "Luis",
        "apellido": "Colon",
        "edad": 32
    }

    print(f'Nombre: {persona["nombre"]} {persona["apellido"]} tiene {persona["edad"]} años')
    'Luis Colon tiene 32 años'

    print(persona["nombre"])
    'Luis'

    edad = persona["edad"]
    print(edad)
    32

    persona["apellido"] = "Gonzalez"
    print(persona)
    {"nombre": "Luis", "apellido": "Gonzalez", "edad": 32}

En algunas ocasiones no vamos a tener certeza de que las claves a las
que queremos acceder existen.  

.. code-block:: python

    persona = {
        "nombre": "Luis",
        "apellido": "Colon",
        "edad": 32
    }

    # La siguiente línea lanzará un error (la clave no existe)
    persona["clave_que_no_exite"]

    # Para acceder a elementos de los que no sabemos si su clave existe,
    # usamos la función "get" de los diccionarios
    persona.get("clave_que_no_exite")
    # Si la clave (key) no existe la anterior línea no va a lanzar
    # un error. Simplemente devolverá None (es el "nada" de Python)

    # Si queremos un valor predeterminado para cuando la clave no 
    # esta definida podemos usar el segundo parámetro opcional de "get"
    persona.get("clave_que_no_exite", "valor_predeterminado")

    # Tambien es posible "preguntar" si una clave existe
    if "clave_buscada" in persona:
        print("clave_buscada SI existe como clave en 'persona'")

    # Esto es posible porque los diccionarios definen un iterador con la 
    # lista de sus claves

    for key in persona:
        print(f"Clave en persona: {key}")

Cada par de clave-valor es denominado como elemento (item).  
La función ``items`` de los diccionarios devuleve un objeto iterable
que podemos navegar con ``for`` y que devuelve en cada paso una
clave y un valor.  

.. code-block:: python

    persona = {
        "nombre": "Juan",
        "apellido": "Colon",
        "edad": 32
    }

    for k, v in persona.items():
        print(f'Item encontrado: Key:{k}, Value: {v}')

    # Item encontrado: Key:nombre, Value: Juan
    # Item encontrado: Key:apellido, Value: Colon
    # Item encontrado: Key:edad, Value: 32 

Los valores puede ser de cualquier tipo e incluso conformar estructuras muy complejas.  

Ejemplo:  

.. code-block:: python

    persona = {
        "nombre": "Luis",
        "apellido": "Colon",
        "edad": 32,
        "estudios": {
            "primario": True,
            "secundario": True,
            "terciario": False,
            "universitario": False
        },
        "experiencia_laboral": {
            "2005-2008": {
                "empresa": "Ferreteria el cosito del coso",
                "cargo": "Vendedor",
                "sueldo": 45000,
                "tareas": ["atender publico", "compras"]
                },
            "2009-2011": {
                "empresa": "Escuela Tecnica San Martin",
                "cargo": "profesor",
                "sueldo": 75000,
                "tareas": ["dictar clases", "elaborar cursos"]
                }
        }
    }

En el ejemplo anterior ``persona["estudios"]`` es a su vez un diccionario por lo que
tiene a su ves las propiedades de un nuevo objeto de este tipo.  
Las siguientes lineas son válidas para la estructura recién definida.   

.. code-block:: python

    print(persona["estudios"]["primario"])
    True

    if persona["estudios"]["secundario"]:
        print('La persona termino el secundario')

En el ejemplo anterior ``persona["experiencia_laboral"]["2005-2008"]["tareas"]`` es a
su vez una lista por lo que tiene a su ves las propiedades de estas.  
Las siguientes lineas son válidas para la estructura recién definida.   

.. code-block:: python

    for tareas in persona["experiencia_laboral"]["2005-2008"]["tareas"]:
        print(f"Tarea: {tarea}")

También es posible usar ``dict()`` para crear un diccionario.

.. code-block:: python

    d3 = dict(
        nombre='Laura',
        edad=47,
        documento=221029489
    )
    type(d3)
    # muestra <class 'dict'>
    print(d3)
    {'nombre': 'Laura', 'edad': 47, 'documento': 221029489}

Tareas
~~~~~~

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 020 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-020/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-020/ejercicio.py
   :literal:

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 030 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-030/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-030/ejercicio.py
   :literal:

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 031 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-031/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-031/ejercicio.py
   :literal:

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 032 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-032/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-032/ejercicio.py
   :literal:

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 041 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-041/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-041/ejercicio.py
   :literal:

*   Hacer un PR con una propuesta de solución para el
    `ejercicio 042 <https://github.com/avdata99/programacion-para-no-programadores/blob/master/ejercicios/ejercicio-042/ejercicio.py>`_

.. include:: /ejercicios/ejercicio-042/ejercicio.py
   :literal:

Algunos ejemplos de uso
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /code/01-basics/dicts-00.py
   :literal:

.. include:: /code/01-basics/dicts-01.py
   :literal:

.. include:: /code/01-basics/dicts-02.py
   :literal:
