class JugadorAutomatico():
    
    def __init__(self, juego):
        self.juego = juego
     
    def arrastrarCarta(self, mazo):
        self.juego.append(mazo.pop())
    
    def ponerCarta(self, carta, juego, destino):
        if carta in juego:
            destino.append(carta)
            juego.remove(carta)
            if len(juego) == 0:
                self.mostrarResultado()
    
    def mostrarResultado(self):
        print("Lo siento, haz perdido. Sigue intentandolo")
