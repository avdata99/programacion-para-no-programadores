Clases y objetos
================

En Python todo es un objeto. Por ejemplo, todas las variables para almacenar
textos son *objetos* del tipo ``str`` (les decimos *strings*).  
Hemos visto ya que estos objetos tienen propiedades y funciones (``upper``, 
``lower``, ``strip``, etc).  
¿Te preguntaste dónde estan definidas esas funciones?  
¿Quien decide que puede y que no puede hacerse con un objeto?  

La respuestas a todo son las **clases**. En Python (y en cualquier lenguaje que use
*Programación Orientada a Objetos*) podemos definir nuestros propios tipos de objetos.  
Cuando los definimos hacemos la elección de que como funcionará y que propiedades y
funciones incluirá.  

Mi primera clase
----------------

Veamos un ejemplo basico. Queremos definir un tipo de dato nuevo: ``Persona``.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1

    class Persona:
        def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido

    # ------------------- FIN DE LA CLASE ------------------------------------

    # Crear nuestros objetos de tipo Persona
    juan = Persona(nombre='juan carlos', apellido='perez')
    pedro = Persona(nombre='pedro ', apellido='gomez')
    luis = Persona('Luis', 'Velez ')

    # Ver el tipo
    type(juan)
    # imprime <class '__main__.Persona'>

    # imprimir propiedades de nuestro objeto
    print(f'{luis.nombre} {luis.apellido}')
    'Luis Velez'


Anatomia de una clase
~~~~~~~~~~~~~~~~~~~~~

*  ``class`` es una palabra reservada de Python (no la podemos usar como nombre de variable)
   que usamos para indicar que estamos definiendo una clase.
*  Despues de ``class`` agregamos el nombre de nuestra clase. Se deben cumplir las mismas
   reglas que para los nombres de variables (no pueden empezar con números, no pueden tener
   espacios, etc). Se suele usar aqui el formato *CamelCase* y siempre con mayúscula inicial.
   No es obligatorio.
*  Despues del nombre de la clase podemos colocar parentesis (no es obligatorio). Se usarán
   en caso de querer aprovechar algo llamado *Herencia* que veremos más adelante.
*  Finalmente agregamos *:* (dos puntos) para indicar que terminamos de definir el encabezado
   de la clase y vamos a comenzar con el bloque de código de ella.
*  El código de la clase debe estar tabulado hacia la derecha. **Esta es una de las grandes
   diferencias que Python tiene con los demás lenguajes de programación**. El código propio de
   la clase comienza tabulado y termina cuando el código vuelve a la izquierda. Muchos otros
   lenguajes de programación usan las llaves ``{}`` para delimitar donde empiezan y terminan
   los bloques de código.
*  Dentro del código de la clase debemos definir las propiedades y funciones que queremos que
   tengan nuestros objetos. Podemos agregar tantas propiedades y funciones como sean necesarias.
   Veremos más detalles a continuación.
*  ``__init__`` es hasta aquí nuestra única función (nos damos cuenta porque usa el ``def`` que
   ya conocemos junto a un grupo de parámetros). Cuando veamos estos guiones bajos dobles
   debemos interpretar que es una herramienta interna de Python. En este caso, todas las clases
   tienen una función de inicialización de una clase (y siempre se llama ``__init__``).
   Ser la función inicializadora quiere decir que se va a ejecutar cuando
   los usuarios de la clase la usen para construir un objeto de este tipo.
*  ``self`` es el primer parámetro de la función ``__init__``. Hablaremos en particular de este
   parámetro más adelante. Por ahora podemos decir que **es obligatorio que todas las funciones
   de las clases tengan un parametro que represente a cada objeto creado con esta clase**. Es
   por esto que veremos a ``self`` en (*casi*, hay situaciones especiales) todas las funciones
   de una clase.
*  Una vez definida la clase (y terminada anulando la tabulación y volviendo a la izquierda
   el código), esta se puede llamar simplemente con su nombre y entre paréntesis todos los
   parámetros que se hayan definido en ``__init__`` (despues de ``self``).

Clases y objetos
~~~~~~~~~~~~~~~~

Las clases se usan para definir el comportamiento de los objetos que podremos crear a partir
de ellas. Al proceso de crear un nuevo objeto se le dice *instanciar* y a cada objeto se le
puede llamar *instancia*.  
En el ejemplo anterior, las líneas

.. code-block:: python

    juan = Persona(nombre='juan carlos', apellido='perez')
    pedro = Persona(nombre='pedro', apellido='gomez')
    # como en las funciones, no es obligatorio nombrar los parámetros
    luis = Persona('Luis', 'Velez ')

crean tres *instancias* del tipo ``Persona``. Cada una de ellas es un objeto distinto y por
lo tanto las propiedades que contienen son independientes y se procesan de manera aislada.

.. code-block:: python

    print(juan.nombre)
    'juan carlos'
    print(pedro.nombre)
    'pedro'

Podemos pensar a los objetos o *instancias* como una versión concreta de una clase.  

¿``self``?
~~~~~~~~~~

Salvo algunas excepciones todas las funciones de las clases deben tener como primer
parámetro a ``self``. De esta forma, todo el objeto estará disponible dentro de cada
función de la clase. Esto es obligatorio y olvidar colocarla generará errores difíciles
de detectar en nuestras primeras experiencias con clases.  

Cuando llamamos a funciones de la clase que usan ``self``, no debemos pasar nada. Debemos
ignorarlo cuando estamos usando nuestro objeto. Esto es visible en todos los ejemplos
usados en este manual.  

Contenido de un clase
~~~~~~~~~~~~~~~~~~~~~

Dentro de la clase podemos definir las propiedades y funciones que nuestros objetos tendrán
cuando sean instanciados.  

Cuando escribimos ``self.PROPIEDAD = VALOR`` estamos indicando que los usuarios podrán usar
estas propiedades en los objetos definidos.  

Estas líneas ...  

.. code-block:: python
    :emphasize-lines: 3, 4

    class Persona:
        def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido

indican que todos los objetos de tipo ``Persona`` podrán referirse a las propiedades
``nombre`` y ``apellido``. Además el valor de ellas será inicializado con los parámetros
que usuario pase al construir estos objetos.  
Al no tener valores predeterminados (funciona igual que las funciones) ambas propiedades
son **obligatorias**. Si intentamos crear una ``Persona`` con algo como:
``juan = Persona(nombre='juan carlos')`` obtendremos un error, el ``apellido`` es
obligatorio.  

Asi como estas propiedades están definidas además de poder ser leidas como hemos visto,
tambien pueden modificarse libremente.  

.. code-block:: python

    diego = Persona('Diego', 'Algun apellido')
    diego.apellido = 'Solis'
    print(diego.apellido)
    'Solis'

Esta forma de definir y usar las propiedades en nuestros objetos es poco segura.  
En nuestra clase, el siguiente comportamiento si esta permitido:

.. code-block:: python
    :emphasize-lines: 2

    diego = Persona('Diego', 'Algun apellido')
    diego.apellido = 17  # sería bueno evitar esto
    print(diego.apellido)
    17

Tareas
~~~~~~

*  Crear una clase llamada ``Auto`` que se inicialice con algunas propiedades obligatorias y otras opcionales
