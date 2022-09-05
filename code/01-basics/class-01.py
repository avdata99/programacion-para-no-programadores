class FacturaServicio:
    """ Cada factura para el pago de servicios hogareños """
    def __init__(self, monto, servicio):
        self.monto = monto
        self.servicio = servicio

    def __add__(self, otro):
        """ Sumar esta factura a otra factura 
            Notar que el resultado no es otro objeto de este tipo,
            es solo un numero."""
        if type(otro) != FacturaServicio:
            raise Exception('La suma solo está permitida para objetos del mismo tipo')

        return self.monto + otro.monto

    def __str__(self):
        return f'$ {self.monto} a pagar por el servicio de {self.servicio}'

    def __eq__(self, otro):
        """ Revisar si son iguales a otra factura """

        if type(otro) != FacturaServicio:
            raise Exception('La comparacion solo está permitida para objetos del mismo tipo')
        
        montos_iguales = self.monto == otro.monto
        servicios_iguales = self.servicio == otro.servicio

        return montos_iguales and servicios_iguales

f1 = FacturaServicio(3500.90, 'Internet')
print(f1)

f1 = FacturaServicio(3500.90, 'Internet')
f2 = FacturaServicio(1806.06, 'Telefono')

print(f1 + f2)
5306.96

f1 = FacturaServicio(1500.90, 'Internet')
f2 = FacturaServicio(1500.90, 'Internet')
f3 = FacturaServicio(3500.90, 'Internet')

if f1 == f2:
    print('f1 y f2 SI son iguales')
else:
    print('f1 y f2 NO son iguales')

if f2 == f3:
    print('f2 y f3 SI son iguales')
else:
    print('f2 y f3 NO son iguales')

"""
f1 y f2 SI son iguales
f2 y f3 NO son iguales
"""