Listas en Python <list>
=======================

Las listas en Python se usan para representar conjuntos ordenados de elementos.  
Los objetos contenidos pueden ser de cualquier tipo (incluidas otras listas).  

Nota: *Ordenado* quiere decir que la lista preserva el orden en que los elementos se
definieron, no que sus elementos se van a ordenar automaticamente.  

Veamos un ejemplo simple de como definir una lista:

.. code-block:: python

    mi_lista = [1, 2, 4]
    otra_lista = ["Jose", "Luisa", "Rafaela"]

    # tambien puede contener tipos diferentes
    variado = [1, "Pedro", 0, "Nombre"]

    # Puede contener variables
    listas = [mi_lista, otra_lista, variado]

    print(listas)
    [[1, 2, 4], ['Jose', 'Luisa', 'Rafaela'], [1, 'Pedro', 0, 'Nombre']]

Python usa los corchetes ``[]`` para delimitar donde empieza y donde
termina una lista. Para separar los elementos se usa la coma.  

Veamos algunas funciones de las listas:

.. code-block:: python

    lista = [8, 9]
    # agregar un elemento al final
    lista.append(3)
    print(lista)
    # [8, 9, 3]

    # elimiar un elemento específico
    lista.remove(9)
    print(lista)
    # [8, 3]
    # Cuidado! si se intenta eliminar un elemento que no existe Python lanzar un error

    # Tambien es posible eliminar por numero de indice y devolver lo eliminado
    primer_elemento = lista.pop(0)
    print(f'El primero era: {primer_elemento}')

    # Para obtener el largo de una lista, se usa la funcion len()
    apellidos = ["gonzalez", "gomez", "rodriguez", "lopez", "garcia"]
    total_apellidos = len(apellidos)
    print(f'Total de apellidos: {total_apellidos}')
    # Total de apellidos: 5

    # Ordenar los elementos de una lista
    lista.sort()
    # Si hay tipos que no son comparables, Python lanzara un error.
    # Si todos son numeros se ordenaran de mayor a menor
    # Si todos son strings, se ordenaran alfabéticamente

    # Es posible modificar directamente algun elemento de la lista
    # usando su numero de índice.

    lista = [3, 4, 5, 7]
    lista[1] = 9
    print(lista)
    [3, 9, 5, 7]

Las listas tambien permiten obtener rápido cada uno de sus elementos u
obtener sub listas incluidas.  
Usar los corchetes junto a la variable permite acceder a cualquier elemento
de la lista por su número de orden (comenzando por cero).  
Por ejemplo

*  ``nombre_de_mi_lista[0]`` devuelve el **primer** elemento de una lista.
*  ``nombre_de_mi_lista[1]`` devuelve el **segundo** elemento de una lista.

**Nota: si se pide un numero de elemento (se les llama índices) mayor a los
disponibles, Python lanzara un error.**  

Comprensión de Diccionario en Python: Explicado con ejemplos

Es posible tambien acceder a los elementos en orden inverso:

*  ``nombre_de_mi_lista[-1]`` devuelve el **último** elemento de una lista.
*  ``nombre_de_mi_lista[-2]`` devuelve el **anteúltimo** elemento de una lista.

Es posible tambien obtener una sublista:
**Nota: esto es anti-intuitivo y confuso. Requiere práctica habituarse**

*  ``nombre_de_mi_lista[0:3]`` devuelve una nueva lista cuyo primer elemento es
   ``nombre_de_mi_lista[0]`` y el últimos es ``nombre_de_mi_lista[2]`` (si, hasta 
   el 2). El segundo *parámetro* no esta incluido, el primero si. ¯\\_(ツ)_/¯
*  ``nombre_de_mi_lista[2:-2]`` devuelve una nueva lista cuyo primer elemento es
   ``nombre_de_mi_lista[2]`` (el tercer elemento) y el últimos es 
   ``nombre_de_mi_lista[-3]`` ¯\\_(ツ)_/¯
*  ``nombre_de_mi_lista[-2:]`` devuelve los ultimos dos elementos, desde 
   ``nombre_de_mi_lista[-2]`` hasta el final (no especificar nada significa hasta
   el final).

Veamos algunos ejemplos:

.. code-block:: python

    apellidos = ["gonzalez", "gomez", "rodriguez", "lopez", "garcia"]
    primer_apellido = apellidos[0]
    print(f'El primer apellido es: {primer_apellido}')
    # El primer apellido es: gonzalez

    ultimo_apellido = apellidos[-1]
    print(f'El último apellido es: {ultimo_apellido}')
    # El último apellido es: garcia

    primeros_2 = apellidos[0:2]
    print(f'Los primeros dos: {primeros_2}')
    # Los primeros dos: ['gonzalez', 'gomez']

    ultimos_2 = apellidos[-2:]
    print(f'Los últimos dos son: {ultimos_2}')
    # Los últimos dos son: ['lopez', 'garcia']

    # ordenar
    apellidos.sort()
    print(f'Lista ordenada: {apellidos}')
    # Lista ordenada: ['garcia', 'gomez', 'gonzalez', 'lopez', 'rodriguez']

    # invertir orden
    apellidos.reverse()
    print(f'Lista invertida: {apellidos}')
    # Lista invertida: ['rodriguez', 'lopez', 'gonzalez', 'gomez', 'garcia']

¿Puede ser más complicado?  
Si, un poco más. Podemos usar un tercer parámetro. Este indica los saltos que
damos para seleccionar elementos. Predeterminado es 1 (vamos de un elemento al otro).  

De esta forma ``nombre_de_mi_lista[1:6:2]`` significa *los elementos desde el primero
al quinto de dos en dos* y ``nombre_de_mi_lista[::-1]`` significa toda la lista completa
en sentido inverso (tambien podemos usar ``nombre_de_mi_lista.reverse()``).  


Los *strings* tambien son listas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python permite tratar a los *strings* como listas.  
Podemos pensar que una palabra es una lista de letras.  

Veamos algunos ejemplos:

.. code-block:: python

    nombre = "Pedro"
    print(f"La primera letra de mi nombre es {nombre[0]}")
    print(f"La última letra de mi nombre es {nombre[-1]}")

Función ``split`` de los *strings*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si quiero separar una frase en palabras Python ya incluye la funcion ``split`` en
los *strings*. Esta función devuelve un objeto de tipo lista.  

Veamos un ejemplo:

.. code-block:: python

    frase = "Era el mejor de los tiempos y era el peor de los tiempos"
    palabras = frase.split()
    print(palabras)
    ['Era', 'el', 'mejor', 'de', 'los', 'tiempos', 'y', 'era', 'el', 'peor', 'de', 'los', 'tiempos']

La función ``split`` tiene un parámetro llamado ``separator`` que tiene como valor prederminado
``" "`` (un espacio, su uso más común). Esté parámetro indica que *caracter* se va a usar para
separar los elementos de la lista resultande.  

Existen casos en que necesitamos separar por otros carcateres.  

Veamos un ejemplo:

.. code-block:: python

    raw_data = "juana,pedro,fabiana,victor,jose,laura"
    nombres = raw_data.split(',')
    print(nombres)
    ['juana', 'pedro', 'fabiana', 'victor', 'jose', 'laura']
    

Tareas
~~~~~~

*  Escribir una funcion que dada una palabra devuelva su tercera letra.

*  Escribir una funcion que reciba cuatro parametros obligatorios.

   *  Devuelva una lista

   *  Esta lista debe contener tres de los cuatro elementos (hay que quitar el que sea más pequeño)

   *  La lista devuelta debe estar ordenada de mayor a menor.

   *  Ejemplo: ``ordenar_y_quitar(4, 8, 9, 12)`` debe devolver ``[12, 9, 8]``.

*  Escribir una funcion que reciba un parametro llamado ``nombre_completo`` y devuelva una
   lista de tres elementos (siempre con tres elementos). 

    *  El primero de los elementos de la lista devuelta debe ser la primera
       palabra de ``nombre_completo`` (separada con la función ``split``)
    *  Si ``nombre_completo`` separado con ``split`` tiene solo un elemento,
       agregar dos *strings* vacios para cumplir el requisito de devolver una
       lista con tres elementos.
    *  Si el ``nombre_completo`` tiene solo dos palabras, devolver una lista de la
       forma ``['palabra1', '', 'palabra2']``
    *  Si el ``nombre_completo`` tiene tres palabras, devolver una lista de la
       forma ``['palabra1', 'palabra2', 'palabra3']``
    *  Si el ``nombre_completo`` tiene **más** de tres palabras, devolver una lista de la
       forma ``['palabra1', 'palabra2', 'palabra3']``
    *  Algunos ejemplos (suponiendo que la funcion se llame ``separar_nombre``, puede ser otro).
       Probarlos todos para asegurarse que funciona como es esperado. 

       *  ``separar_nombre('Juan')`` debe devolver ``['Juan', '', '']``
       *  ``separar_nombre('Juan Perez')`` debe devolver ``['Juan', '', 'Perez']``
       *  ``separar_nombre('Juan Carlos Perez')`` debe devolver ``['Juan', 'Carlos', 'Perez']``
       *  ``separar_nombre('Juan Carlos Perez Valdez')`` debe devolver ``['Juan', 'Carlos', 'Perez']``
