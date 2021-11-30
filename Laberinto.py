import pygame
from pygame import surface

pygame.init()

#clases para carga imagenes y tomar sus rectas que se utilizan en colisiones
class Per (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/perso2.png").convert_alpha()
        self.rect = self.image.get_rect()

class Pared (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/muro2.png").convert_alpha()
        self.rect = self.image.get_rect()

class Piso (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/piso.png").convert_alpha()
        self.rect = self.image.get_rect()

#Recibe un mapa y lo va recorriendo y almacenando cordenadas de los muro
def construir_mapa(mapa):
    listaMuros = []
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                listaMuros.append(pygame.Rect(x,y,22,17))
            x+=22
        x=0
        y+=17
    return listaMuros

"""
#Funciones que utilizaba cuando todavia no sabia cargar imagenes bien

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, GREEN, rectangulo)

def dibujar_mapa (superficie, listaMuros):
    for muro in listaMuros:
        dibujar_muro(superficie, muro)
"""

#Funcion para escribir Texto
def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def PantallaFinal(puntuacion):
    ventana.fill(BLACK)

    #Escribe los textos
    draw_text(ventana, "GAME OVER", 65, WIDTH // 2, HEIGHT // 4)
    draw_text(ventana, "Tu puntuacion fue: " + str(puntuacion), 30, WIDTH // 2, HEIGHT // 2)
    draw_text(ventana, "Presiona cualquier tecla para salir", 17, WIDTH // 2, HEIGHT * 3/4)
    pygame.display.flip()

    #Bucle para esperar a que el jugador presione una tecla
    waiting = True
    while waiting:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
 

#Defino alto y ancho de la ventana en pixeles
WIDTH = 748
HEIGHT = 578

#para ubicarlo en eje de las x hay que multiplicar por 17 yen el eje de las y por 22 por la cantidad de espacios que se lo desea mover
movimiento = pygame.Rect(90,550,10,10)
x=0
y=0
vel=0
alt=0

#Creo colores 
BLACK = (0, 0, 0)
GREEN = (0,255,0)

#Creo la ventana
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tza tun tzat')
reloj = pygame.time.Clock()

#Listas para dibujar despues
listaPared = pygame.sprite.Group()
pared= Pared()
listaPared.add(pared)

listaPiso = pygame.sprite.Group()
piso= Piso()
listaPiso.add(piso)

listaPer = pygame.sprite.Group()
per = Per()
listaPer.add(per)

#Mapas
mapa3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXX                              ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

mapa = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXX             X       XX  X    ",
"XXXX XXXXXXXXXX XX XXXXX XX XX XXX",
"XXXX XXXXXXXXXX    XXXXX    XX XXX",
"XXXX XXXXXXXXXXXXXXXXXXXXXXXXX XXX",
"XX             XX              XXX",
"XX XXXXXXXXXXX XX XXXXXXXXXXXXXXXX",
"XX  XX     XXX XX XXXXXXXXXXXXXXXX",
"XXX    XXX XXX    XX           XXX",
"XXXXXXXXXX XXXXXXXXX XXXXXXXXX XXX",
"XXXXX                XX    XXX XXX",
"XXXXXXXXXXXXXXXXXXXXXXX XX XXX XXX",
"XXXXX             XXXXX XX     XXX",
"XXXXX XXXXXXXXXXX XXXXX XXXXXXXXXX",
"XXXXX XXX         XXXXX XXXXXXX XX",
"XXXXX XX   XXXXXXXXXXXX XXXXXXX XX",
"XXXXX XX XXXXXXXXXXXXXX XXXXXXX XX",
"XXXXX XX                 XXXXXX XX",
"XXXXX XXXXXXXXXXXXXXXXXXXXXXXXX XX",
"XXX                             XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX",
"XXXXXXX      XXX       XXX      XX",
"XXXXXXX XXXX XXX XXXXX XXX XXXX XX",
"XXXXXXX XXXX     XXXXX     XXXX XX",
"XXXXXXX XXXXXXXXXXXXXXXXXXXXXXX XX",
"XXXXX                           XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX",
"XXXX                       XXXX XX",
"XXXX XXXXXXXXXXXXXXXXXXXXX XXXX XX",
"XXXX XX                XXX XXXX XX",
"XXXX     XXXXXXXXXXXXX XXX XXXX XX",
"XXXXXXXXXXXXXXXXXXXXXX XXX      XX",
"XXXX                     XXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

mapa1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX X",
"XX                               X",
"XX XXXXXXXXXXXXXXXXXXXXXXXXXX XXXX",
"XX XXXXXXXXXX            XXX     X",
"XX XXXXXXXXXX XXXXXXXXXX XXXXXXX X",
"XX XXX   XXXX X        X      XX X",
"XX     X XXX      XXXX XXXXXX XX X",
"XXXXXXXX XXXXXXXXXXX       XX XX X",
"XXXXX                 XXXX XX XX X",
"XXXXXXXXXXXXXXXXXXXXXXXXXX XX XX X",
"XXXX                       XX XX X",
"XXXX XXXXXXXXXXXXXXXXXXXXXXXX    X",
"XXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XX                            XXXX",
"XXXXXXXXXXXXXXXXXXXX XXXXXXXX XXXX",
"XXXXXXXXXX   XXXX    XXXXXXXX XXXX",
"XXX        X XXXX XXXXXXXXXXX XXXX",
"XXXXX XXXX X XX    XXX        XXXX",
"XXXXX XXX  X  XXXX XXX XXXXXXX XXX",
"XX    XXXX XX      XXX     XXX XXX",
"XX XXXXX   XXXXXXXXXXXXXXX XXx XXX",
"XX XXX                XXXX XXX XXX",
"XX XXXXXXXXXXXXXXXXXX XXX  XXX XXX",
"XXXX               XX XXX XXXX XXX",
"XXXX XX XXXXXXX XXXXX XXX      XXX",
"XXXX XX XXXXXXX       XXXXXXXX XXX",
"XXXX XX XXXXXXXXXXXXXXXXXXXXXX XXX",
"XXXX XX                        XXX",
"XXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XX                              XX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX XX",
"XXXX                XXXXXXXXXXX XX",
"XXXX XXXXXXXXXXXXXX              X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

mapa2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"                                 X",
"XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXX      X                     X",
"XXXXXXXXXX XXXXXXXXXXXXXXXX XXXX X",
"XXXXXXXXXX      XXX     XXX XXXX X",
"XXXXXXX    XXXX     XXX     XXX  X",
"XXXXXXX XXXXXXXXXXXXXXXXXXXXXXXX X",
"XXXXXXX                          X",
"XXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX     XXXXXXXX                XX",
"XXX XXXXXXXXXXXX XXXXXXXXXXXXXX XX",
"XXX X            XXXXXXXXXXXXXX XX",
"XXX XXXXXXXXXXXX XXXX        XX XX",
"XXX XXXX    XXXX XXXX XXXXXX XX XX",
"XXX XXXX XX XXXX XXXX XXXXXX XX XX",
"XXX XX   XX XXXX XXXX XXXXXX XX XX",
"XXX XXXXXXX XXXX XXXX   XXXX XX XX",
"XXX XXX          XXXXXX XXXX    XX",
"XXX XXXXX XXXXXX XXXXXX XXXXXXXXXX",
"XXX XXXXX XXXXXX XXX        XXXXXX",
"XXX X     XXXXXX XXXXXXXXXX XXXXXX",
"XXX XXXXX XXXXX          XX  XXXXX",
"XXX XXXXX XXXXXXXXXXXXXX XX      X",
"XXX XXXXX             XX XXXXXXX X",
"XXX XXXXXXXXXXXXXX XXXXX XX      X",
"XXX                XXXXX XX XXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX XX     XX",
"XXXX             XXXXXXX XXXXXX XX",
"XXXX XXX  XXXXXX XXXXXXX      X XX",
"XXXX XXXX XXXXXX         XXXXXX XX",
"XXXX XXXX XXXXXXXXXXXXXXXXXXX   XX",
"XXXX XXXX                      XXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Carga control de volumen de la musica
pygame.mixer.init()
pygame.mixer.music.load("Assets/music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

#variables que son necesarias iniciar antes que empiece el bucle del juego
score= 1000000
nivel= -1
posnormal=0
waiting = True
scoreFinal = 0
fondo= pygame.image.load("Assets/fondo.png").convert()
gameOver=False
fin=False

#comienza el bucle del juego
while not gameOver:

    reloj.tick(60)
    ventana.fill(BLACK)

    score= score-1

    #Pantalla de inicio
    if nivel == -1:
        ventana.blit(fondo, [0,0])
        draw_text(ventana, "Tza tun tzat", 65, WIDTH // 2, HEIGHT // 4)
        draw_text(ventana, "Juego hecho por Franco Dellinocente", 27, WIDTH // 2, HEIGHT / 2)
        draw_text(ventana, "Presiona cualquier tecla para comenzar", 17, WIDTH // 2, HEIGHT * 3/4)
        pygame.display.flip()
        while waiting:
            reloj.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    nivel=0
                    waiting = False


    #Fin de juego y carga la pantalla final
    if fin == True:
        PantallaFinal(scoreFinal)

    #Ubica al personaje al inicio de cada nivel
    if posnormal== 0:
        movimiento = pygame.Rect(90,550,10,10)
        posnormal=1

    #Eventos ya sea de precionar teclas o boton de quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver=True

        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                vel=-3
            elif event.key==pygame.K_RIGHT:
                vel=+3
            elif event.key==pygame.K_UP:
                alt=-3
            elif event.key==pygame.K_DOWN:
                alt=+3
        else:
            vel=0
            alt=0

    #movimiento y ubicacion del personaje
    movimiento.x += vel
    movimiento.y += alt
    per.rect.x = movimiento.x
    per.rect.y = movimiento.y

    #Primer nivel
    if nivel == 0:

        #Toma el array que se le indica y empieza a diferencia entre muro o piso
        listaMuros = construir_mapa(mapa)


        #Colision con los muros
        for muro in listaMuros:
            if movimiento.colliderect(muro):
                movimiento.x -= vel
                movimiento.y -= alt

        #Dibujo
        x=0
        y=0
        for fila in mapa:
            for muro in fila:
                if muro=="X":
                    pared.rect.x=x
                    pared.rect.y=y
                    listaPared.add(pared)
                    listaPared.draw(ventana)
                else:
                    pared.rect.x=x
                    pared.rect.y=y
                    listaPiso.add(piso)
                    listaPiso.draw(ventana)
                x+=22
            x=0
            y+=17

        listaPer.draw(ventana)

        #Si pasa tal punto cambia el nivel y en la vuelta del bucle posiciona al personaje
        if per.rect.x > 748 and nivel == 0:
            nivel=1
            posnormal=0

    #Segundo Nivel
    if nivel == 1:

        listaMuros = construir_mapa(mapa1)

        #colision con los muros
        for muro in listaMuros:
            if movimiento.colliderect(muro):
                movimiento.x -= vel
                movimiento.y -= alt

        #dibujo
        x=0
        y=0
        for fila in mapa1:
            for muro in fila:
                if muro=="X":
                    pared.rect.x=x
                    pared.rect.y=y
                    listaPared.add(pared)
                    listaPared.draw(ventana)
                    
                else:
                    pared.rect.x=x
                    pared.rect.y=y
                    listaPiso.add(piso)
                    listaPiso.draw(ventana)
                x+=22
            x=0
            y+=17

        

        listaPer.draw(ventana)

        if nivel == 1 and per.rect.y < 0:
            nivel=2
            posnormal=0
        

    #Tercer nivel
    if nivel == 2:
    
        listaMuros = construir_mapa(mapa2)

        #colision con los muros
        for muro in listaMuros:
            if movimiento.colliderect(muro):
                movimiento.x -= vel
                movimiento.y -= alt
                
        #dibujo
        x=0
        y=0
        for fila in mapa2:
            for muro in fila:
                if muro=="X":
                    pared.rect.x=x
                    pared.rect.y=y
                    listaPared.add(pared)
                    listaPared.draw(ventana)
                        
                else:
                    pared.rect.x=x
                    pared.rect.y=y
                    listaPiso.add(piso)
                    listaPiso.draw(ventana)
                x+=22
            x=0
            y+=17


        listaPer.draw(ventana)

        if nivel == 2 and per.rect.x < 0:
            scoreFinal=score
            fin= True
            #nivel=2
            #posnormal=0


    #Muestra el score en tiempo real
    draw_text(ventana, "score: " + str(score), 25, WIDTH * 3.5/4, 10)

    pygame.display.flip()

pygame.quit()
