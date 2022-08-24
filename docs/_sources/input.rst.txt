Recibir datos del usuario ``input``
===================================

Es posible detener la ejecución de tu programa para solicitar
al usuario de nuetro programa que ingrese datos.  

.. code-block:: python

    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    print(f'Hola {nombre} {apellido}!')

La funcion ``input`` devuelve como *string* lo que el usuario ingresa.  
Si necesitaras un objeto de tipo ``int`` (por ejemplo para hacer cálculos)
podes hacer la transformación con ``int(variable_string)``.  

.. code-block:: python

    print('POTENCIAS')
    nro = input('Ingresa un numero: ')
    base = int(nro)
    print(f'{base}² = {base**2}')
    print(f'{base}³ = {base**3}')
    print(f'{base}⁴ = {base**4}')
    print(f'{base}⁵ = {base**5}')

    """ Ejemplo 
    POTENCIAS
    Ingresa un numero: 7
    7² = 49
    7³ = 343
    7⁴ = 2401
    7⁵ = 16807
    """

Tareas
~~~~~~

*  ¿Que pasa si en el último ejemplo el usuario inserta una letra en lugar
   de un número? ¿Por qué?.
*  Escribir un programa que le pida al usuario que ingrese los datos
   necesarios y calcule el `índice de masa corporal <https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal>`_.
