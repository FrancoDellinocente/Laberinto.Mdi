import pygame

pygame.init()

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

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, GREEN, rectangulo)

def dibujar_mapa (superficie, listaMuros):
    for muro in listaMuros:
        dibujar_muro(superficie, muro)

WIDTH = 748
HEIGHT = 578
#para ubicarlo en eje de las x hay que multiplicar por 17 yen el eje de las y por 22 por la cantidad de espacios que se lo desea mover
movimiento = pygame.Rect(90,550,10,10)
x=0
y=0
vel=0
alt=0

BLACK = (0, 0, 0)
GREEN = (0,255,0)

#Creo la ventana
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('muro')
reloj = pygame.time.Clock()

#listas para dibujar despues
listaPared = pygame.sprite.Group()
pared= Pared()
listaPared.add(pared)

listaPer = pygame.sprite.Group()
per = Per()
listaPer.add(per)

#Dibujo como va a ser el mapa
mapa = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXX                            X",
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

listaMuros = construir_mapa(mapa)

#comienza el bucle del juego
gameOver=False
while not gameOver:

    reloj.tick(60)

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

    #colision con los muros
    for muro in listaMuros:
        if movimiento.colliderect(muro):
            movimiento.x -= vel
            movimiento.y -= alt
    
    ventana.fill(BLACK)

    #dibujo
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro=="X":
                pared.rect.x=x
                pared.rect.y=y
                listaPared.add(pared)
                listaPared.draw(ventana)
            x+=22
        x=0
        y+=17

    #aqui es cuando pasara de nivel en nivel
    #if per.rect.y < 540:
    #    per.rect.y = 550



    listaPer.draw(ventana)
    #dibujar_mapa(ventana, listaMuros)
    pygame.display.flip()

    #no funciona todavia
    #pygame.mixer.music.load("music.mp3")
    #pygame.mixer.music.play(-1)

pygame.quit()
