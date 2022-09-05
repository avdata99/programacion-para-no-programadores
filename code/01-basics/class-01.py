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
