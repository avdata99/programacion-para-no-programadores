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

Analizar la siguiente función y su ejemplo uso

.. code-block:: python

    def contar_palabras(frase):
        """ 
        Esta funcion toma una frase y devuelve un diccionario
        con una llave por cada palabra y un valor igual a la
        cantidad de veces que aparece en la frase
        """

        # Separar la frase en palabras
        palabras = frase.split()

        # preparar el diccionario vacio en el que voy a cargar los resultados
        resultados = {}

        # Iterar por la lista de palabras para contarlos
        for palabra in palabras:
            if palabra not in resultados:
                # si no existía, inicializarla en cero
                resultados[palabra] = 0
            else:
                # si existe, sumarle 1
                resultados[palabra] += 1
                
        return resultados

    # Probar la funcion
    contar_palabras("Oid mortales el grito sagrado. Libertad, libertad, libertad. Oid el ruido de rotas cadenas")
    {'Oid': 1, 'mortales': 0, 'el': 1, 'grito': 0, 'sagrado.': 0, 'Libertad,': 0, 'libertad,': 0, 'libertad.': 0, 'ruido': 0, 'de': 0, 'rotas': 0, 'cadenas': 0}

Hubieramos esperado que la palabra *Oid* tenga el valor 2 ya que esta dos veces pero ha fallado.
Proponer una solución.  

Hubieramos esperado que la palabra *libertad* tenga el valor 3 ya que esta tres veces pero ha fallado.  
Al parecer los signos de puntuación son un problema y deberían ser limpiados.  
Proponer una solucion.  