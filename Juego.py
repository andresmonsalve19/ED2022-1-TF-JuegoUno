from collections import deque
from Carta import Carta
from Jugador import Jugador
from JugadorAutomatico import JugadorAutomatico
import random

class Juego():
    
    def __init__(self):
        # Se crea el juego de los jugadores automáticos
        self.juego1 = deque()
        self.juego2 = deque()
        self.juego3 = deque()
        
        # Mi juego
        self.miJuego = deque()
        
        # Se crean las instancias necesarias para el juego
        self.jugador = Jugador(self.miJuego)
        self.jugadorAutomatico1 = JugadorAutomatico(self.juego1)
        self.jugadorAutomatico2 = JugadorAutomatico(self.juego2)
        self.jugadorAutomatico3 = JugadorAutomatico(self.juego3)
        
        # Jugadores
        self.jugadores = (self.jugador, self.jugadorAutomatico1, self.jugadorAutomatico2, self.jugadorAutomatico3)
        self.bots = (self.jugadorAutomatico1, self.jugadorAutomatico2, self.jugadorAutomatico3)
        #Se crean las cartas
        # Las cartas 10, 11 y 12 son especiales
        # 10 -> Bloqueo
        # 11 -> Cambio de sentido
        # 12 -> +2 
        self.numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        
        # Colores -> R = Rojo, Y = Amarillo, G = Verde, B = Azul
        self.colores = ('R', 'Y', 'G', 'B')
        
        # Se crea el mazo
        self.cartas = deque()
        
        # Se crea la pila de de cartas botadas
        self.cartasBotadas = deque()
        self.onces = 0
        self.iniciar()
    
    def iniciar(self):
        #Se generan las cartas del mazo
        self.generarCartas()
        
        # Barajar o revolver las cartas
        self.revolverCartas(self.cartas)
        
        # Se le reparten las cartas a cada jugador
        for jugador in self.jugadores:
            self.repartirCartas(jugador, self.cartas)
        
        pantallaInicial = """
        ***************************************
        * ¡BIENVENIDOS AL UNO VIRTUAL! 
        ***************************************
        * Autores:
        * Jaime Andres Monsalve Ballesteros
        * Fredy Alberto Orozco Loaiza
        * Deumeck Hernandez Zuleta
        * Francisco Garcia
        ***************************************
        * Menú Principal
        * 1. Instrucciones del juego
        * 2. Jugar
        * 3. Salir
        ***************************************
        """
        
        print(pantallaInicial)
        
        instrucciones = """
        Para jugar este uno tenga en cuenta las siguientes recomendaciones:
        
        1. Para mover una carta a la pila "JUEGO" que es donde se bota la carta se debe hacer
        introduciendo por teclado la siguiente notacion --> mj, espacio, carta a botar
        Ejemplo --> mj R-8 --> Aquí se está moviendo la carta R-8.
        
        2. Para arrastrar una carta del MAZO se introduce por teclado la letra a
        
        NOTACION
        mj --> Significa mover a juego (pila JUEGO)
        a --> Significa arrastrar
        Colores de las cartas --> R: Red = Rojo, G: Green = Verde, B: Blue = Azul,  Y: Yellow = Amarillo
        Numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. El 10, 11 y 12 son especiales
        10 --> Carta de bloqueo o Skip
        11 --> Carta de cambio de sentido
        12 --> Carta +2
        """

        while (True):
            opcion = int(input("Elija una opcion: "))
            
            if (opcion == 1):
                # Se imprimen las instrucciones del juego
                print(instrucciones)
                
            elif (opcion == 2):
                self.cartasBotadas.append(random.choice(self.cartas))
                turno = 0
                reverse = False
                while True:
                    if (len(self.jugador.juego) == 0) or (len(self.jugadorAutomatico1.juego) == 0) or (len(self.jugadorAutomatico2.juego) == 0) or (len(self.jugadorAutomatico3.juego) == 0):
                        break
                    if turno == 0:
                        pantallaPrincipal = f"""
                        *********************************************************************
                        * MAZO [*-*] ({len(self.cartas)}) ***** JUEGO [{self.mostrarJuego(self.cartasBotadas)}] ({len(self.cartasBotadas)})
                        *********************************************************************
                        * Jugador 1: {self.mostrarJuego((self.jugadorAutomatico1.juego))} *** ({len(self.jugadorAutomatico1.juego)})
                        * Jugador 2: {self.mostrarJuego((self.jugadorAutomatico2.juego))} *** ({len(self.jugadorAutomatico2.juego)})
                        * Jugador 3: {self.mostrarJuego((self.jugadorAutomatico3.juego))} *** ({len(self.jugadorAutomatico3.juego)})
                        *********************************************************************
                        * Mi juego: {self.mostrarJuego((self.jugador.juego))} *** ({len(self.jugador.juego)})
                        *********************************************************************        
                        """
                        # Se imprime la pantalla principal del juego
                        print(pantallaPrincipal)
                        print(self.onces)
                        # Se le pide al usuario que haga su movimiento
                        movimiento = input("Ingrese su movimiento: ").split()
                        # Se programa una opcion para que pueda salirse del juego cuando el usuario lo desee                
                        try:
                            if (movimiento[0] == 'mj') and (int(movimiento[1].split("-")[1]) in self.numeros):
                                juego = self.jugador.juego
                                carta = self.buscarCarta(movimiento[1], juego)
                                destino = self.cartasBotadas
                                if self.validarMovimiento(carta):
                                    self.jugador.ponerCarta(carta, juego, destino)
                                    ultimaCarta = self.cartasBotadas[-1].__str__().split("-")
                                    numero = int(ultimaCarta[1])
                                    if numero == 10:
                                        turno = 2
                                        continue
                                    elif numero == 11:
                                        self.onces += 1
                                        if self.onces%2 != 0: 
                                            reverse = True
                                            turno = 3               
                                            continue
                                        else:
                                            reverse = False
                                            turno = 1
                                            continue
                                    elif numero == 12:
                                        if reverse:
                                            turno = 3
                                            continue
                                        turno = 1
                                        #self.tomarDosCartas(self.jugador)
                                        continue
                                    else:
                                        if reverse:
                                            turno = 3
                                            continue
                                        turno = 1
                                        continue
                                else:
                                    print("No se puede realizar ese movimiento, verifique su juego e inténtelo nuevamente o arrastre una carta")
                            elif (movimiento[0] == 'a'):
                                self.jugador.arrastrarCarta(self.cartas)
                                if reverse:
                                    turno = 3
                                    continue
                                turno = 1
                                continue
                            else:
                                if (int(movimiento[0]) == 0):
                                    break
                        except ValueError:
                            print("Movimiento no válido")
                        except IndexError:
                            pass  
                        
                    elif turno == 1:
                        self.jugarEnAutomatico(self.jugadorAutomatico1)
                        ultimaCarta = self.cartasBotadas[-1].__str__().split("-")
                        numero = int(ultimaCarta[1])
                        if numero == 10:
                            turno = 3
                            continue
                        elif numero == 11:
                            self.onces += 1
                            if self.onces%2 != 0: 
                                reverse = True
                                turno = 0               
                                continue
                            else:
                                reverse = False
                                turno = 2
                                continue
                        elif numero == 12:
                            if reverse:
                                turno = 0
                                continue
                            turno = 2
                            #self.tomarDosCartas(self.jugadorAutomatico1)
                            continue
                        else:
                            if reverse:
                                turno = 0
                                continue
                            turno = 2
                            continue        
                                               
                    elif  turno == 2:
                        self.jugarEnAutomatico(self.jugadorAutomatico2)
                        ultimaCarta = self.cartasBotadas[-1].__str__().split("-")
                        numero = int(ultimaCarta[1])
                        if numero == 10:
                            turno = 0
                            continue
                        elif numero == 11:
                            self.onces += 1
                            if self.onces%2 != 0: 
                                reverse = True
                                turno = 1               
                                continue
                            else:
                                reverse = False
                                turno = 3
                                continue
                        elif numero == 12:
                            if reverse:
                                turno = 1
                                continue
                            turno = 3
                            #self.tomarDosCartas(self.jugadorAutomatico2)
                            continue
                        else:
                            if reverse:
                                turno = 1
                                continue
                            turno = 3
                            continue
                        
                    elif turno == 3:
                        self.jugarEnAutomatico(self.jugadorAutomatico3)
                        ultimaCarta = self.cartasBotadas[-1].__str__().split("-")
                        numero = int(ultimaCarta[1])
                        if numero == 10:
                            turno = 1
                            continue
                        elif numero == 11:
                            self.onces += 1
                            if self.onces%2 != 0: 
                                reverse = True
                                turno = 2               
                                continue
                            else:
                                reverse = False
                                turno = 0
                                continue
                        elif numero == 12:
                            if reverse:
                                turno = 2
                                continue
                            turno = 0
                            #self.tomarDosCartas(self.jugadorAutomatico3)
                            continue
                        else:
                            if reverse:
                                turno = 2
                                continue
                            turno = 0
                            continue
            
                    self.recargarColaDeArrastre()
                break
                
            elif (opcion == 3):
                break
            
        
    def generarCartas(self):
        """Se genera el mazo de cartas"""
        for color in self.colores:
            for numero in self.numeros:
                carta1 = Carta(color, numero)
                carta2 = Carta(color, numero)
                self.cartas.append(carta1)
                self.cartas.append(carta2)
    
    def revolverCartas(self, mazo):
        random.shuffle(mazo)
    
    def repartirCartas(self, jugador, mazo):
        i = 0
        while (i < 8):
            cartaSeleccionada = random.choice(mazo)
            jugador.juego.append(cartaSeleccionada)
            mazo.remove(cartaSeleccionada)
            i += 1
    
    def mostrarJuego(self, juego):
        c = ""
        for carta in juego:
            c += f"[{carta.__str__()}]"
        return c
    
    def buscarCarta(self, descripcion, juego):
        for carta in juego:
            if (descripcion == carta.__str__()):
                return carta
    
    def validarMovimiento(self, carta):
        cartaAValidar = carta.__str__().split("-")
        pila = self.cartasBotadas[-1].__str__().split("-")

        # Validar por color o por numero
        try:
            if (cartaAValidar[0] == pila[0]) or (cartaAValidar[1] == pila[1]):
                return True
            else:
                return False
        except IndexError:
            pass
        
    def jugarEnAutomatico(self, jugador):
        juego = jugador.juego
        for carta in list(juego):
            if self.validarMovimiento(carta):
                jugador.ponerCarta(carta, juego, self.cartasBotadas)
                break
        else:
            jugador.arrastrarCarta(self.cartas)
         
    def recargarColaDeArrastre(self):
        if len(self.cartas) == 0:
            ultimaCarta = self.cartasBotadas[-1]
            
            for carta in self.cartasBotadas:
                self.cartas.append(carta)
                self.cartasBotadas.remove(carta)
                
            self.cartasBotadas.append(ultimaCarta)
        self.revolverCartas(self.cartas)
    
    def tomarDosCartas(self, jugador1, jugador2):
        jugador1.arrastrarCarta(self.cartas)

