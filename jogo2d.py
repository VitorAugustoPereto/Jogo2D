import random
import pygame
from pygame.locals import *
from sys import exit

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Top Gun')

naveInimiga = pygame.image.load("assets/Nave2.PNG.png").convert_alpha()
naveInimiga = pygame.transform.scale(naveInimiga,(60,60))
naveInimiga = pygame.transform.rotate(naveInimiga, 90)

#posição inicial
pos_naveInimiga_x = 500
pos_naveInimiga_y = 360


navePlayer = pygame.image.load("assets/Nave1.PNG.png").convert_alpha()
navePlayer = pygame.transform.scale(navePlayer,(75,75))
navePlayer = pygame.transform.rotate(navePlayer, -90)


#posição inicial
pos_navePlayer_x = 200
pos_navePlayer_y = 275


missil = pygame.image.load("assets/Missil.png").convert_alpha()
missil = pygame.transform.scale(missil,(25,15))
missil = pygame.transform.rotate(missil, 180)


vel_x_missil = 0
pos_x_missil = 200
pos_y_missil = 300

pontos = 10

triggered = False


rodando = True


player_rect = navePlayer.get_rect()
naveInimiga_rect = naveInimiga.get_rect()
missil_rect = missil.get_rect()



bg = pygame.image.load('assets/Fundo.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))



#funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]


def respawn_missil():
    triggered = False
    respawn_missil_x = pos_navePlayer_x
    respawn_missil_y = pos_navePlayer_y
    vel_x_missil = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]


def colisao():
    global pontos
    if player_rect.colliderect(naveInimiga_rect) or naveInimiga_rect.x == 60:
        pontos -=1
        return True
    elif missil_rect.colliderect(naveInimiga_rect):
        pontos +=1 
        return True
    else:
        return False



while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1200:
        screen.blit(bg, (rel_x,0))


    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w] and pos_navePlayer_y > 1:
        pos_navePlayer_y -= 1
        if not triggered:
            pos_y_missil -= 1

    if tecla[pygame.K_s] and pos_navePlayer_y < 665:
        pos_navePlayer_y += 1

        if not triggered:
            pos_y_missil += 1


    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missil = 2


    #respawn
    if pos_naveInimiga_x == 50:
        pos_naveInimiga_x = respawn()[0]
        pos_naveInimiga_y = respawn()[1]

    if pos_x_missil == 1300:
        pos_x_missil, pos_y_missil,triggered, vel_x_missil = respawn_missil()


    if pos_naveInimiga_x == 50 or colisao():
        pos_naveInimiga_x = respawn()[0]
        pos_naveInimiga_y = respawn()[1]

    #posição rect
    player_rect.y = pos_navePlayer_y
    player_rect.x = pos_navePlayer_x

    missil_rect.x = pos_x_missil
    missil_rect.y = pos_y_missil

    naveInimiga_rect.x = pos_naveInimiga_x
    naveInimiga_rect.y = pos_naveInimiga_y


    #movimento
    x-=1
    pos_naveInimiga_x -= 1.5

    pos_x_missil += vel_x_missil
    
    #pygame.draw.rect(screen, (255,0,0), player_rect, 4)
    #pygame.draw.rect(screen, (255,0,0), naveInimiga_rect, 4)
    #pygame.draw.rect(screen, (255,0,0), missil_rect, 4)


    #criada imagens
    screen.blit(naveInimiga, (pos_naveInimiga_x, pos_naveInimiga_y))
    screen.blit(missil, (pos_x_missil, pos_y_missil))
    screen.blit(navePlayer, (pos_navePlayer_x, pos_navePlayer_y))

    print(pontos)

    pygame.display.update()
