class Auto:
    def __init__(self, marca, modelo, estado, referencia):
        self.marca = marca
        self.modelo = modelo
        self.estado = estado
        self.referencia = referencia
        if type(modelo) != int:
            raise Exception ('El modelo debe ser escrito con números')
        if referencia == str:
            referencia = []
            if len(referencia) > 100:
                raise Exception ('La referencia es demasiado larga, escriba una más corta')
        elif referencia == int:
            raise Exception ('La referencia debe ser escrita')

auto1 = Auto("Fiat", 97, "usado", "es un fiat uno")
print(auto1)
        
        

        

    
