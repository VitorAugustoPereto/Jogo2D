import pygame
from pygame.locals import *
from sys import exit

x = 600
y = 800

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

    pygame.display.update()
