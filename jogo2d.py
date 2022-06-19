import pygame
from pygame.locals import *
from sys import exit

x = 1280
y = 600

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Top Gun')

bg = pygame.image.load('assets/Fundo.PNG.png').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

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

    #movimento
    x-=0.6

    pygame.display.update()
