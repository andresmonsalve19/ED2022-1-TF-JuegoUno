class Carta():
    
    def __init__(self, color, simbolo):
        self.color = color
        self.simbolo = simbolo
        self.propiedad = None
        
    def __str__(self):
        carta = self.color +"-" + str(self.simbolo)
        return carta
    
