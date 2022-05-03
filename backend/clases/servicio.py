class Servicio:

    def __init__(self, nombre, alias):
        self.nombre = nombre
        self.alias = alias
        self.positivo = 0
        self.negativo = 0
        self.neutro = 0

    def getSentimiento(self, sentimiento):
        if sentimiento == 'positivo':
            self.positivo +=1
        if sentimiento == 'negativo':
            self.negativo +=1
        if sentimiento == 'neutro':
            self.neutro +=1