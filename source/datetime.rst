Librerías incluida: ``datetime``
================================

Asi como hay funciones incluidas (*built-ins*) que se pueden usar sin
estar declaradas tambien hay más herramientas de Python disponibles pero
que requieren ser *importadas*.  

Importar (con el comando ``import`` o de la forma ``from X import Y``)
en Python es disponibilizar nueva herramientas (fuenciones y otras) en
nuestro código.  

Fecha y hora: ``datetime``
--------------------------

El manejo de fechas y horas básico en Python se hace con la librería ``datetime``.  

Fechas simples con ``date``
---------------------------

Si solo necesitamos una fecha general solo con día + mes + año podemos usar
objetos de tipo ``date``.  

.. code-block:: python

    from datetime import date

    hoy = date.today()
    print(hoy)
    # 2022-02-12
    print(type(hoy))
    # <class 'datetime.date'>

    # date (año, mes, dia)
    agosto_27_2022 = date(2022, 8, 27)

Variación de tiempo con ``timedelta``
-------------------------------------

Para sumar o restar persiodos de tiempo a una fecha existe ``timedelta``:  

.. code-block:: python

    from datetime import date, timedelta
    hoy = date.today()
    manana = hoy + timedelta(days=1)
    print(manana)
    # 2022-02-13

Fecha + hora = momento exacto con ``datetime``  
----------------------------------------------

Si necesitamos más precision que solo dia + mes + año debemos usar ``datetime.datetime``

**Nota: datetime como libreria incluye un objeto con el mismo nombre pero
son cosas distintas. Uno es la libreria y otro es la clase para construir
fecha/horas o datetimes.**  

.. code-block:: python

    from datetime import datetime, timedelta

    ahora = datetime.now()
    print(ahora)
    # 2022-02-12 14:35:16.687589

    print(type(ahora))
    # <class 'datetime.datetime'>

    en_15 = ahora + timedelta(minutes=15)
    print(en_15)
    # 2022-02-12 14:50:16.687589

    # la diferencia entre dos fechas, es un timedelta
    a = datetime(2022,3,4)
    b = datetime(1988,2,11,6,7,8)
    c = a - b
    print(c)
    # imprime 12439 days, 17:52:52
    type(c)
    # imprime <class 'datetime.timedelta'>


fecha <---> string
------------------

En muchos casos es requirido pasar de fecha a strings y viceversa.  
Para estos casos se usan las funciones ``strftime`` (fecha a
string) y ``strptime`` (string a fecha).  

.. code-block:: python

    from datetime import date, datetime

    hoy = date.today()
    print(hoy.strftime("%d/%m/%Y"))
    # 12/02/2022
    print(hoy.strftime("%Y-%m-%d"))
    # 2022-02-12
    print(hoy.strftime("%d de %B de %Y"))
    # 12 de February de 2022

    # pasar de string a fecha
    fecha_str = '2022-09-21'
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    print(fecha)
    # 2022-09-21 00:00:00


Tareas
~~~~~~

*   Hacer una función que le pida al usuario que inserte su fecha 
    de nacimiento y se le devuelva hace cuantos días nació.  