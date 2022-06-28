class Jugador():
    
    def __init__(self, juego):
        self.juego = juego
        self.movimientos = ('mj', 'a')
    
    def arrastrarCarta(self, mazo):
        self.juego.append(mazo.pop())
    
    def ponerCarta(self, carta, juego, destino):
        if carta in juego:
            destino.append(carta)
            juego.remove(carta)
            if len(juego) == 0:
                self.mostrarResultado()
    
    def mostrarResultado(self):
        print(""" 
              ⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀ ⢸⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠰⠆⠀⠀⠀⠀⠰⠆⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠶⠶⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢰⣶⠄
            ⠀⠀⠀⠀⠀⠀⢸⣿⣧⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣼⣿⡇⠀⠀⢀⣿⡿⠀
            ⠀⠀⢀⣠⣴⣶⣾⣿⡿⠿⠿⠿⠿⠿⠿⣿⣿⡿⠿⣿⣿⣷⣶⣾⡿⠟⠀⠀
            ⠀⣠⣿⡿⠋⠉⢹⣿⣿⣶⠶⣶⣶⣶⣶⣿⣿⣿⣾⣿⣿⡏⠉⠁⠀⠀⠀⠀
            ⢠⣿⡟⠀⠀⠀⢸⣿⡟⠉⠀⠉⣻⣿⣿⣏⣀⣻⣿⣉⣿⡇⠀⠀⠀⠀⠀⠀
            ⠀⠉⠁⠀⠀⠀⢸⣿⣿⣿⣤⣿⣿⣿⣿⣿⡟⠋⠙⢿⣿⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢸⣿⣏⣉⣉⣿⣏⣉⣹⣿⣧⣀⣀⣾⣿⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⣿⡿⠿⠿⠿⠿⢿⣿⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      Siiii, haz ganado  
              """)
