import random
import pygame
from pygame.locals import *
from sys import exit

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Top Gun')

naveInimiga = pygame.image.load("assets/Nave2.PNG.png").convert_alpha()
naveInimiga = pygame.transform.scale(naveInimiga,(50,50))
naveInimiga = pygame.transform.rotate(naveInimiga, 90   )

#posição inicial
pos_naveInimiga_x = 500
pos_naveInimiga_y = 360


navePlayer = pygame.image.load("assets/Nave1.PNG.png").convert_alpha()
navePlayer = pygame.transform.scale(navePlayer,(50,50))
navePlayer = pygame.transform.rotate(navePlayer, -90)

#posição inicial
pos_navePlayer_x = 200
pos_navePlayer_y = 300


bg = pygame.image.load('assets/Fundo.PNG.png').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

#funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]




rodando = True

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
    if tecla[pygame.K_s] and pos_navePlayer_y < 665:
        pos_navePlayer_y += 1

    #respawn
    if pos_naveInimiga_x == 50:
        pos_naveInimiga_x = respawn()[0]
        pos_naveInimiga_y = respawn()[1]



    #movimento
    x-=0.6
    pos_naveInimiga_x -= 1

    #criada imagens
    screen.blit(naveInimiga, (pos_naveInimiga_x, pos_naveInimiga_y))
    screen.blit(navePlayer, (pos_navePlayer_x, pos_navePlayer_y))

    pygame.display.update()
