Funciones especiales de las clases
----------------------------------

Tambien conocidos como *métodos mágicos* (podemos pensar a la palabra método como
sinónimo de *función*) estas funciones se aplican a situaciones habituales de otros
objetos de Python. Estas situación son la suma, resta, division, comparación, etc.  
    
__add__
~~~~~~~

Que pasara si quisiéramos sumar dos ``Personas`` tal como las vimos en la clase anterior:

.. code-block:: python

    juan = Persona('Juan', 'Perez')
    victor = Persona('Victor', 'Gutierrez')

    a = juan + victor

Este código daría un error porque no esta definida la función especial (o mágica) ``__add__``.  
No esta definida porque esta suma no tendría sentido en estos objetos.  
Veamos un ejemplo donde si pudiera ser útil.  

.. code-block:: python

    class FacturaServicio:
        """ Cada factura para el pago de servicios hogareños """
        def __init__(self, monto, servicio):
            self.monto = monto
            self.servicio = servicio

        def __add__(self, otro):
            """ Sumar esta factura a otra factura 
                Notar que el resultado no es otro objeto de este tipo,
                es solo un numero."""
            if type(otro) != FacturaServicio:
                raise Exception('La suma solo está permitida para objetos del mismo tipo')

            return self.monto + otro.monto

La funcion especial ``__add__`` debe incluir un parámetro despues de ``self`` en el que
recibiremos cualquiera sea el objeto al que debemos sumarnos.  

Veamos este código en acción:  

.. code-block:: python

    f1 = FacturaServicio(3500.90, 'Internet')
    f2 = FacturaServicio(1806.06, 'Telefono')

    print(f1 + f2)
    5306.96

La función ``__add__`` devuelve un numero pero podría haber casos donde se devuelvan otros tipos de
datos. Muchas veces podemos esperar que dos objetos del mismo tipo al sumarse devuelvan un nuevo
objeto de ese tipo pero no es siempre el caso. Esto puede definirse a gusto.  
De la misma forma, podríamos sumar nuestro objetos con lo de otra clase. Nosotros lo hemos bloqueado
(lanzando un error) pero podríamos hacerlo si fuera necesario. Incluso podríamos devolver resultados
distintos por cada tipo de objeto al que sumamos nuestro objeto.  

__str__
~~~~~~~

Es probablemente la función especial más usada. Se usa para definir que texto se va a devolver
cuando el usuario necesite una representación *string* de este objeto.  

.. code-block:: python

    def __str__(self):
        return f'$ {self.monto} a pagar por el servicio de {self.servicio}'

Ejemplo de uso:  

.. code-block:: python

    f1 = FacturaServicio(3500.90, 'Internet')
    f1_str = str(f1)
    print(f1_str)

    # o directamente cuando se quiere imprimir nuestro objetio
    f1 = FacturaServicio(3500.90, 'Internet')
    print(f1)

__eq__
~~~~~~~

Si queremos permitir la comparación de objetos de nuestra clase se puede definir esta función.   
Esta función será llamada cuando nuestro objeto sea comparado con otro mediante el operador ``==``.  
Al igual que ``__add__``, podríamos comparar nuestro objetos con lo de otra clase si fuera necesario
(este no es el caso).  

.. code-block:: python

    def __eq__(self, otro):
        """ Revisar si son iguales a otra factura """

        if type(otro) != FacturaServicio:
            raise Exception('La comparacion solo está permitida para objetos del mismo tipo')
        
        montos_iguales = self.monto == otro.monto
        servicios_iguales = self.servicio == otro.servicio

        return montos_iguales and servicios_iguales

Veamoslo en acción:  

.. code-block:: python

    f1 = FacturaServicio(1500.90, 'Internet')
    f2 = FacturaServicio(1500.90, 'Internet')
    f3 = FacturaServicio(3500.90, 'Internet')

    if f1 == f2:
        print('f1 y f2 SI son iguales')
    else:
        print('f1 y f2 NO son iguales')

    if f2 == f3:
        print('f2 y f3 SI son iguales')
    else:
        print('f2 y f3 NO son iguales')

    """
    f1 y f2 SI son iguales
    f2 y f3 NO son iguales
    """

Código final de nuestra clase
-----------------------------

Disponible `aquí <https://github.com/avdata99/programacion-para-no-programadores/blob/master/code/01-basics/class-01.py>`_.  

.. include:: /code/01-basics/class-01.py
   :literal:


Otras funciones especiales
--------------------------

Estas algunas otras de las funciones especiales.  

*  ``__mul__``: Multiplipicación
*  ``__sub__``: Resta (*Substraction*) 
*  Para que nuestros objetos se comporten como diccionarios

  *  ``__getitem__``: Obtener un item con la clave que se pasa como parámetro
  *  ``__setitem__``: Definir un item con la clave y el valor que se pasan como parámetro
  *  ``__delitem__``: Eliminar el item que tiene la clave que se pasa como parámetro

*  ``__ne__``: No igual (*Not equal*) ``!=`` 
*  ``__lt__``: Menor que (*less than*) ``<`` 
*  ``__gt__``: Mayor que (*grater than*) ``>`` 
*  ``__neg__``: Negativo (para cuando usan ``-MY-OBJETO``) 

**Y hay muchas más.**   

Tareas
~~~~~~

*  Hacer un PR a la 
   `clase Carta <https://github.com/avdata99/programacion-para-no-programadores/blob/master/code/01-basics/class-04.py>`_
   para agregar la función ``__add__`` para que devuelva un ``int`` calculando el envido **solo** de esas dos cartas. **Incluir
   multiples asserts al final que pruebe al menos tres sumas (diferentes y variadas) y sus resultados (envidos) esperados**.
*  Hacer un PR a la 
   `clase Carta <https://github.com/avdata99/programacion-para-no-programadores/blob/master/code/01-basics/class-04.py>`_
   para agregar la función ``__eq__`` para que devuelva ``True`` solo cuando el numero y el palo sean iguales.

Algunos ejemplos de uso
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /code/01-basics/class-05.py
   :literal:
