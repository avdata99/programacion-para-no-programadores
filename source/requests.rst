Paquete ``requests``
--------------------

El paquete `requests <https://pypi.org/project/requests/>`_ es uno muy usado.  
Formalmente podemos decir que es un cliente HTTP. Con el podemos realizar
peticiones de recursos web de una forma muy sencilla.  

Veamos este ejemplo:

.. include:: /code/01-basics/external-libs/requests-00.py
   :literal:

Ese ejemplo muestra como descargar el contenido de una página web.  
El resultado obtenido es el código HTML de la página.  
Esto es similar a lo que hacen los navegadores de internet (Google
Chrome o Mozilla Fiefox por ejemplo) cuando accedemos a una página web.  

Esto es muy útil para obtener información de una página web y procesarla
con Python. Existen tecnicas para extraer información de un documento HTML
y transformarlo en datos que podemos usar en nuestro programa.  

A estas técnicas se les llama `Web scraping <https://es.wikipedia.org/wiki/Web_scraping>`_
y son muy usadas.  

Pero no toda la web es HTML. Existen muchos otros formatos de datos que
ya está pensados para ser leidos directamente por computadoras.  
El formato ``JSON`` es uno de los más usados.

Veamos un ejemplo de un recurso web en formato ``JSON``:

.. include:: /code/01-basics/external-libs/requests-02.py
   :literal:

En este caso podemos ver como el recurso JSON es transformado a diccionario
con la funcion ``json()`` de la librería requests.  

Veamos un ejemplo de un recurso web en formato ``txt``:

.. include:: /code/01-basics/external-libs/requests-06.py
   :literal:

En este ejemplo nos descargamos un libro completo y analizamos las letras
y las palabras más usadas.  

Tarea
~~~~~

*  Hacer un programa con Python que nos de el precio de alguna
   criptomenedas que el usuario desee (usaremos el USDT como si
   fuera el dólar como respuesta).

   *  Con ``input`` le pediremos al usuario que ingrese el código de la
      criptomoneda que quiere consultar (por ejemplo ``ETH`` para Ethereum
      o ``BTC`` para bitcoin).
   *  Despues el precio puede devolverse de dos formas (elegir una):
   
      *   Hacer un request a https://api2.binance.com/api/v3/ticker/24hr
          y obtener una lista de diccionarios obtenidos todos los precios.
          Iterar la lista hasta que se encuentre el ``symbol`` igual a 
          ``XXXUSDT`` (donde ``XXX`` es el código de la criptomoneda) y 
          devolver el valor de ``lastPrice``.
      *   Hacer un request a https://api2.binance.com/api/v3/ticker/24hr?symbol=XXXUSDT
          (donde ``XXX`` es el código de la criptomoneda) y obtener un
          diccionario con el precio. Devolver el valor de ``lastPrice``.
