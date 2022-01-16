.. Curso de Programación documentation master file, created by
   sphinx-quickstart on Sun Aug 12 16:52:37 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Curso de Programación para no programadores
===========================================

¿Que es programar?
------------------

Programar es escribir las *instrucciones* necesarias para que una *computadora* realice alguna tarea.  
Las *instrucciones* son diferentes según el entorno donde se usan o la finalidad que se busca.  
Existen muchos lenguajes de programación que reflejan esa variedad.  
Excede a este manual definir estrictamente que es una *computadora*. Diremos que al nombrarla incluimos a:

 - La clásica computadora que podemos tener en nuestra casa u oficina.
 - Una portatil como las conocidas notebooks
 - Un teléfono celular
 
Podemos extender lo que entendemos por computadoras agregando:

 - Un lavarropas moderno en tanto que tienen programas variados en un mini-computadora interna.
 - La alarma de una casa o auto que según diferentes acciones pre-establecidas dispara acciones programadas (luces y bocinas).

En general muchos electrodomésticos ya incluyen computadoras y por lo tanto programas.  
Estas *instrucciones* organizadas con alguna finalidad específica conforman lo que denominamos *software*.  

Ejemplo
-------

La computadora interna de un lavarropas que gestiona los dispositivos y conexiones internas podría tener estas instrucciones:

#. Abrir el conducto de agua hasta que el sensor detecte que se llegó al nivel esperado
#.  -- Si no se cumple en 20 segundos mostrar en pantalla codigo de error ERR01
#. Abrir el conducto de jabón líquido 10 segundos
#. Girar a velocidad normal el tambor 20 vueltas hacia la derecha
#. Girar a velocidad normal el tambor 20 vueltas hacia la izquierda
#. Abrir el desagote del tambor mientras gira durante 1 minuto
#.  -- Si el sensor detecta que todavia hay agua mostrar en pantalla codigo de error ERR02
#. Abrir el conducto de agua durante 20 segundos (para enjuague)
#. Girar a velocidad normal el tambor 20 segundos
#. Abrir el desagote del tambor
#.  -- Si el sensor detecta que todavia hay agua mostrar en pantalla codigo de error ERR03
#. Girar a velocidad rápida el tambor 2 minutos hacia la derecha
#. Girar a velocidad rápida el tambor 2 minutos hacia la izquierda
#. Destrabar la puerta del tambor, trabajo terminado.

¿Que hace un programador?
-------------------------

El trabajo de un programador de software es **literalmente escribir instrucciones** en un lenguaje de programación específico.  
Un programador conoce uno o más *lenguajes de programación* y puede desempeñarse con ellos en múltiples entornos de trabajo.  
Estos entornos incluyen:

 - Una página web
 - Una aplicación para tu celular
 - Un sistema que funciona en una computadora estándar (Word, Google Chrome, Excel o cualquier programa que ves en el *escritorio* de tu computadora)
 - Micro-sistemas que sirvan de soporte a sistemas más grandes y que *no se ven*

Acotar estos entornos donde un software se ejecuta es difícil, son múltiples.  

.. image:: /_static/imgs/hola1.png

¿Donde escribimos nuestro código?
---------------------------------

Como dijimos programar es escribir instrucciones (las denominaremos código o *código fuente*). Para esto podríamos usar algún 
software de edición de texto pero existen herramientas específicas para esta tarea.  

`Atom <https://ide.atom.io/>`_

.. image:: /_static/imgs/hola3.png

`Visual Studio <https://code.visualstudio.com/>`_ (de Microsoft)

.. image:: /_static/imgs/hola2.png

A estos entornos de trabajo se los conoce *Entornos de desarrollo Integrado* o IDE por sus siglas en inglés (Integrated Development Environment).  
Estas herramientas proveen funcionalidades que simplifican el trabajo de un programador


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices y tablas
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
