Aplicaciones web con Python
===========================

Las aplicaciones web son programas que funcionan en servidores de internet.  
No es necesario instalarlos en nuestra computadora y se acceden
desde un navegador web (como Google Chrome, Mozilla Firefox u otros).  
Algunos ejemplos son google.com, pypi.org, wikipedia.org, etc.  

Cuando se accede a una aplicación web a través de su URL, el
navegador envía una petición al servidor donde está alojada la aplicación.  
El servidor procesa esa solicitud y envía una respuesta al navegador.  

A muy grandes rasgos (y omitiendo muchos detalles sobre el desarrollo
de aplicaciones webs modernas) podemos decir que una aplicación
web tiene dos partes:

* El *frontend*: es la cara visible de la aplicación. Es el responsable
  de definir que vemos y como interactuamos con la aplicación.
  Para el frontend necesitamos conocer HTML, CSS y JavaScript.
* El *backend*: es la parte de la aplicación que no vemos. Procesa
  internamente las peticiones del usuario y genera las respuestas.
  Puede leer y escribir bases de datos, archivos, etc.
  Python, Java, Javascript, PHP, Ruby y otros pueden ser usados en el
  backend.

Ambas partes pueden estar en el mismo servidor o en servidores diferentes.

Nuestra primera aplicacion web con Flask
----------------------------------------

Flask es un (micro)framework para Python que permite crear aplicaciones
web muy rápidamente.  
Con flask podemos definir *frontend* y *backend* en la misma aplicación.  

Antes de empezar a programar, creamos y activamos un entorno virtual
para nuestra aplicación.  

.. code-block:: bash

   # crear el entorno
   python -m venv <carpeta_donde_se_creara_el_entorno>
   # activar el entorno (en Windows)
   <carpeta_donde_se_creara_el_entorno>\Scripts\activate.bat
   # activar el entorno (en Linux)
   source <carpeta_donde_se_creara_el_entorno>/bin/activate
   
Para instalar Flask y comenzar nuestra primera aplicación web,
ejecutamo el siguiente comando en la terminal:

.. code-block:: bash

    pip install Flask


Ahora creamos un archivo llamado ``app.py`` con el siguiente contenido:

.. code-block:: python
    
    # Importar la clase Flask
    from flask import Flask

    # Crear una aplicacion Flask
    app = Flask(__name__)

    # Definir la respuesta que va a devolver nuestro servidor
    # cuando alguien acceda a la URL raiz (/)
    @app.route('/')
    def hello():
        return 'Hola usuario!'

    @app.route('/otro-recurso')
    def otro():
        return 'Hola usuario en <i>otro recurso!</i>'

Finalmente ejecutamos el servidor de desarrollo de Flask:

.. code-block:: bash

    flask run

    # Y veremos ...
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Si vamos al navegador e ingresamos a http://127.0.0.1:5000/
vamos a ver la respuesta que definimos en nuestra aplicación:
``Hola usuario!``.  

En la linea de comandos queda regisro de esa visita

.. code-block:: bash

    127.0.0.1 - - [22/Jan/2022 11:54:52] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [22/Jan/2022 11:54:52] "GET /favicon.ico HTTP/1.1" 404 -

Si nos dirigimos a la URL http://127.0.0.1:5000/otro-recurso vamos a ver
la respuesta que definimos para ese recurso: ``Hola usuario en <i>otro recurso!</i>``.

¿Que son ``<i>`` e ``</i>``?  

Son etiquetas HTML que definen un texto en *cursiva*.  
Veremos un poco mas adelante que es HTML y que más podemos hacer con él.  

Notas de esta aplicación
~~~~~~~~~~~~~~~~~~~~~~~~

Esta aplicación es muy simple pero nos permite ver de forma básica
como funciona una aplicación web.  

Por un lado el usuario accede a nuestro servidor desde su navegador
en las URLs ``127.0.0.1:5000`` y ``127.0.0.1:5000/otro-recurso``.  

* *127.0.0.1* significa "nuestra computadora" (tambien llamado *localhost*)
* *5000* es el puerto que este servidor temporal de desarrollo
  utiliza para escuchar peticiones.
* Luego de la barra (/) viene el *recurso* que estamos solicitando.
  En este caso, el recurso es la raiz (``/``) u ``/otro-recurso``.
  Necesitamos tener una función definida para cada recurso, si
  el usuario intenta acceder a un recurso que no esta definido
  en nuestro servidor, recibirá un error 404 (*not found* / no encontrado).

Nuestras funciones ``hello()`` y ``otro()`` son las encargadas de procesar
las peticiones y generar las respuestas. En estos casos no hay ningun
procesamiento antes de enviar la respuesta. Nuestro backend realmente no
está haciendo nada.  

El contenido que estas funciones devuelven es el que el navegador
va a mostrar al usuario. Esto es lo que llamamos *frontend*.  
En este caso nuestro frontend es muy simple, solo enviamos texto.  
No hay mucho valor hasta aquí.  

Avancemos a una versión más avanzada de nuestra aplicación web
donde *frontend* y *backend* sean un poco más interesantes.  
