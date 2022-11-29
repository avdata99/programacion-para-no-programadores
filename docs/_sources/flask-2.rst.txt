Aplicacion v2
-------------

Nuestra archivo ``app.py``

.. include:: /code/02-web/flask/prj-03/app.py
    :literal:

Nuestro archivo ``cripto/data.py`` (recuerda agregar un archivo vacío ``cripto/__init__.py``)

.. include:: /code/02-web/flask/prj-03/cripto/data.py
    :literal:

El estilo CSS de nuestro sitio en ``/static/base.css``

.. include:: /code/02-web/flask/prj-03/static/base.css
    :literal:

El código JavaScript de nuestro sitio en ``/static/base.js``

.. include:: /code/02-web/flask/prj-03/static/base.js
    :literal:

El template HTML de la home de nuestra aplicacion web en ``/templates/index.html``

.. literalinclude:: /code/02-web/flask/prj-03/templates/index.html
    :language: html

El template HTML de la pagina de detalle de una criptomoneda en ``/templates/datos.html``

.. literalinclude:: /code/02-web/flask/prj-03/templates/datos.html
   :language: html

Tarea
~~~~~

*   Crear una lista de criptomonedas en el backend y sacar la que esta en el frontend.
    Asegurarse que el sitio siga funcionando de la misma forma.
*   Agrega un nuevo template HTML para mostrar un mensaje de error cuando
    no se encuentre la criptomoneda buscada.
    **Nota:** Cuando una criptomenoda no existe, el API devuelven
    ``{'code': -1121, 'msg': 'Invalid symbol.'}``.
