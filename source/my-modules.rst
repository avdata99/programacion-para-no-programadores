Paquetes y módulos
-------------------

Hasta aquí hemos ejecutado nuestro código en un solo archivo.  

.. admonition:: no es exactamente así
    :class: hint

    En realidad cuando usamos algo como ``from random import ranint``
    estamos usando (importando) código que esta en otros archivos que no vemos (pero
    podríamos, `aquí esta el modulo interno de python random.py <https://github.com/python/cpython/blob/main/Lib/random.py>`_).  

En la medida que el código que hacemos crece, es necesario mantener un orden.  
Es por esto que conviene empaquetar el código que hacemos. Esto incluso nos permite
reutilizarlo en el futuro.

.. admonition:: reutilizar y compartir
    :class: tip

    Además de reutilizarlo nosotros lo podemos compartir
    abiertamente. La comunidad de Python es una de las más grandes en el desarrollo de
    software abierto. Al momento de escribir estas líneas, hay alrededor de 400.000 paquetes
    abiertos en `Pypi <https://pypi.org/>`_ (*The Python Package Index*). Todo este código
    esta disponible para nosotros.  

Podemos pensar a los paquetes Python como carpetas que pueden contener más paquetes
(sub-carpetas) y modulos (archivos de Python ``.py``) con funciones y clases para reutilizar.  

Para indicar que una carpeta es un paquete alcanza con agregarle un archivo llamado
``__init__.py``. Por el momento alcanza con que este archivo este vacío.  

.. graphviz::
    :name: pkg-structure
    :caption: Estructura de archivos y carpetas

    digraph {
        compound=true;
        rankdir="TB";
        labeljust=l;

        base [
                label="Mi código (carpeta)",
                shape="folder",
                fillcolor="#ACA5DD",
                style=filled
            ];
        main [
                fontsize="9",
                fontname="courier-new",
                label="#opciones para importar\limport paquete\lfrom paquete import modulo\lfrom paquete.modulo import mi_funcion",
                shape="component"
            ];
        paquete [
                label="paquete (carpeta)",
                shape="folder"
            ];
        init [
                label="__init__.py",
                shape="file"
            ];
        fn [
            fontsize="9"
            fontname="courier-new"
            label="def mi_funcion():",
            shape="component"
        ]

    subgraph cluster_a {
        color="#2344FF"
        label="modulo.py";
        fn
    }

    subgraph cluster_b {
        color="#2344FF"
        label="mi-programa.py"
        main
    }

    base -> main [label="contiene a" lhead="cluster_b"];
    base -> paquete;
    # main -> paquete [label=" import paquete ", style=dashed, arrowhead=true];
    paquete -> fn [label="contiene a" lhead="cluster_a"];
    paquete -> init;
    # main -> fn [label="from paquete\nimport module", style=dashed, lhead="cluster_a"];
    # main -> fn [label="from paquete.module\nimport my_function", style=dashed];
    }

De esta forma es posible mantener tu codigo ordenado y facil de mantener.   



.. code-block:: python
    :caption: funciones.py

    def suma(a, b):
        return a + b

.. code-block:: python
    :caption: otro_archivo_en_la_misma_carpeta.py

    import funciones
    a = funciones.suma(4, 5)

    from funciones import suma
    a = suma(4, 5)
