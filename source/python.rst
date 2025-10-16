Instalando Python
=================

Para comenzar a programar en Python, primero necesitamos instalar Python en nuestra computadora.  
Python es el lenguaje de programación que usaremos en este curso es fácil de aprender y con
una gran comunidad de usuarios.  

El primer paso es descargar el instalador de Python desde su sitio web oficial: https://www.python.org/  

.. image:: /_static/imgs/install-python-win.png

... y luego seguir los pasos del instalador.  

.. image:: /_static/imgs/install-python-win-2.png

.. image:: /_static/imgs/install-python-win-3.png

.. image:: /_static/imgs/install-python-win-4.png

.. image:: /_static/imgs/install-python-win-5.png

.. image:: /_static/imgs/install-python-win-6.png

Consola Python
--------------

Listo, ya tenemos Python instalado en nuestra computadora.  
Ya podemos abrir una terminal (o consola) de Python y probar que todo funciona correctamente.  

.. code-block:: python

    print("Probando")

.. image:: /_static/imgs/install-python-win-7.png

Podemos tambien probar que Python funciona correctamente desde PowerShell (que será nuestra
terminal en Windows).  

Podemos ver la versión de Python instalada con el comando:

.. code-block:: powershell

    python -V

.. image:: /_static/imgs/install-python-win-8-test-powershell.png

Tambien alli mismo podemos abrir la terminal interactiva de Python con el comando:

.. code-block:: powershell

    python

Usando PowerShell
-----------------

.. image:: /_static/imgs/python-win-9-powershell-ni-notepad.png

Aqui podemos ver el uso de algunos comandos básicos de PowerShell (la terminal que usaremos en Windows):

``mkdir nombre_carpeta``:
    Crea una nueva carpeta con el nombre indicado.

``cd nombre_carpeta``:
    Cambia el directorio actual a la carpeta indicada.

``ni nombre_archivo``:
    Crea un nuevo archivo con el nombre indicado.

``notepad nombre_archivo.py``:
    Abre el archivo indicado con el editor de texto Notepad (en este caso un archivo Python).

``python nombre_archivo.py``:
    Ejecuta el archivo Python indicado.
