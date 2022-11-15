Paquetes externos
=================

La construcción de paquetes en Python representan una de las mejores prácticas para
distribuir código. Aislar correctamente la solución a un problema nos permite reutilizar
esa porción de código en otros proyectos, y nos permite además compartirlo con la comunidad.  
`Pypi <https://pypi.org/>`_ es la biblioteca más usada por la comunidad de Python para
redistribuir paquetes. Cientos de miles de paquetes estan disponibles allí para descarga.   

Los paquetes externos son paquetes que no vienen por defecto con Python, pero que se
pueden instalar para ampliar las funcionalidades de Python.  

Cada proyecto de software incluye en general un conjunto de paquetes a instalar del cual depende.  
Para instalar un paquete externo, se usa la herramienta ``pip``. Esta herramienta puede usarse
desde la terminal.   

Si estas usando Git Bash en Windows, es posible que ya tengas instalado ``pip``.  
Para probar si ya lo tenes instalado poder ejecutar alguna de estas opciones.  

.. code-block:: bash

   pip --version
   # o lo que es lo mismo
   pip -V

Si no recibis un mensaje de error y podes ver la versión de ``pip`` podes saltearte la
siguiente sección

Instalar ``pip``
----------------

Instalar ``pip`` en Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Descargar el script de instalación `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_ y
ejecutarlo con Python desde tu terminal.  

.. code-block:: bash
   
   python get-pip.py

Instalar ``pip`` en Linux (Ubuntu)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sudo apt install python3-pip

Instalar paquetes con ``pip``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Una vez instalado pip ya podes instalar paquetes localmente.  

.. code-block:: bash

   pip install <nombre_paquete>
   # opcionalmente se puede indicar la versión exacta a instalar
   pip install <nombre_paquete>==<version>
   # Instalar una lista de paquetes desde un archivo de texto con los requerimientos
   pip install -r requirements.txt


Entornos virtuales
==================

Un desarrollador de software en general trabaja sobre más de un proyecto, y por lo tanto
necesita instalar más de un conjunto de paquetes. Uno para cada proyecto.  
Para evitar conflictos entre las versiones usadas en cada proyecto, se recomienda usar
entornos virtuales.  
Cada entorno virtual se crea con una versión específica de Python, y permite instalar
un conjunto de paquetes específicos.  
Cada proyeto activa y se ejecuta dentro de estos entornos.  
Python permite crear y activar estos entornos virtuales con el módulo ``venv``.  

Crear un entorno virtual
------------------------

.. code-block:: bash

   python -m venv <carpeta_donde_se_creara_el_entorno>


Activar un entorno virtual
--------------------------

La forma de activación de los entornos virtuales depende del sistema operativo.  
Para Windows el comando para activate un entorno virtual es

.. code-block:: bash
   
      <carpeta_donde_se_creara_el_entorno>\Scripts\activate.bat

Para Linux el comando para activar un entorno es

.. code-block:: bash

   source <carpeta_donde_se_creara_el_entorno>/bin/activate

Te vas a dar cuenta que el entorno esta activado porque tu terminal va a agregar
el nombre de tu entorno entre parentesis en la linea de tu terminal.  
Una vez activado el entorno, el comando ``pip`` instalara los paquetes dentro de este.  
Para desactivar el entorno virtual, ejecutar el comando ``deactivate`` (el mismo para
ambos sistemas operativos).  


Tarea
~~~~~~

*  Clonar el repositorio `autos justicia 2022 <https://github.com/avdata99/autos-justicia-cordoba-2022>`_

   *  Crear un entorno local, activarlo e instalar ``requirements.txt``
   *  Si el entorno va a ser una carpeta dentro de la carpeta del proyecto, agregar la
      carpeta al archivo ``.gitignore``
   *  Ejecutar el script ``scrape.py`` y asegurarse de que funcione como se espera.
   *  Analizar el código y proponer algún cambio mediante algún PR
