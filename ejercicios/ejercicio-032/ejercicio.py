"""
El siguiente código permite crear facturas de ventas y agregar items.
El código no tiene fallas pero el cliente desea que la lista de items
no tenga productos duplicados. Si se intenta agregar un producto por
segunda vez, la función deberia darse cuenta y actualizar los valores
de ese item y no agregarlo como nuevo item.
"""


def agregar_item(factura, producto, precio_unitario, cantidad=1):
    """
    Agregar un item a una factura que se pasa como parámetro
    """
    precio_total = cantidad * precio_unitario
    item = {
        'producto': producto,
        'precio_unitario': precio_unitario,
        'cantidad': cantidad,
        'precio_total': precio_total,
    }

    factura['items'].append(item)
    factura['total'] += precio_total

def crear_factura():
    """ Crear una factura """
    factura = {
        'total': 0,
        'items': []  # lista de items
    }

    return factura

mi_factura = crear_factura()
agregar_item(mi_factura, 'Alfajor', 150, 3)
agregar_item(mi_factura, 'Turron', 53)
agregar_item(mi_factura, 'Turron', 53)


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.

assert mi_factura['total'] == 556

items_en_factura = mi_factura['items']
assert len(items_en_factura) == 2

print('Ejercicio terminado OK')
