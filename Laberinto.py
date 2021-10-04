import pygame

pygame.init()

class Per (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/perso.png").convert_alpha()
        self.rect = self.image.get_rect()

class Pared (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets/muro.jpg").convert_alpha()
        self.rect = self.image.get_rect()

def construir_mapa(mapa):
    listaMuros=[]
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                listaMuros.appemd(pygame.Rect(x,y,80,80))
            x+=80
        x=0
        y+=80
    return listaMuros

WIDTH = 1280
HEIGHT = 720
movimiento = pygame.Rect(600,400,40,40)
x=0
y=0
vel=0
alt=0

BLACK = (0, 0, 0)

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
listaPer (per)

#Dibujo como va a ser el mapa
mapa = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXX  XXXXX    XXXXX     ",
"XXXXXX   XXXXXXX   XX   XXX",
"XXX       XXXXXXX      XXXX",
"XXXXXXXXX  XXXXXXXXX  XXXXX",
"XXXXXXXXXX  XXXXXXXX  XXXXX",
"X                       XXX",
"XXX  XXXXXXXXXXXXXXXXXXXXXX",
"XXXX  XXXXX         XXXXXXX",
"XXXXX        XXXXX  XX  XXX",
"XXXXXXXXXXXXXXXXXX  XXXXXXX",
"XXXX  XXXXX  XXXX  XXXXXXXX",
"                        XXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
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
                vel=-5
            elif event.key==pygame.K_RIGHT:
                vel=+5
            elif event.key==pygame.K_UP:
                alt=-5
            elif event.key==pygame.K_DOWN:
                alt=+5
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
            pared.rect.x=x
            pared.rect.y=y
            listaPared.add(pared)
            listaPared.drawn(ventana)
        x+=80
    x=0
    y+=80
    listaPer.drawn(ventana)
    pygame.display.flip()
pygame.quit()
