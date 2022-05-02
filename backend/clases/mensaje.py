import escribir
import re

class Mensaje:
    texto = None
    def __init__(self, fecha, lugar, usuario, red_social, texto):
        self.fecha = fecha
        self.lugar = lugar
        self.usuario =  usuario
        self.red_social = red_social
        self.texto = texto
        self.sentimiento = None
        self.analizar()

    def __str__(self):
        return str(self.texto)

    def tilde(self, s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    
    def analizar(self):
        
        #analizar texto pra saber si es positivo, negativo o neutro
        numero_positivos = 0

        for positivo in escribir.Positivos:
            
            match_pattern = re.findall(self.tilde(positivo).lower(), self.tilde(self.texto).lower())
            numero_positivos += len(match_pattern)

        numero_negativos = 0

        for negativo in escribir.Negativos:
            
            match_pattern = re.findall(self.tilde(negativo).lower(), self.tilde(self.texto).lower())
            numero_negativos += len(match_pattern)

        if numero_positivos > numero_negativos:
            self.sentimiento = 'positivo'

        elif numero_positivos < numero_negativos:
            self.sentimiento = 'negativo'

        elif numero_positivos == numero_negativos:
            self.sentimiento = 'neutro'

        elif numero_negativos == 0 and numero_positivos== 0:
            self.sentimiento = 'neutro'



            
                   

    