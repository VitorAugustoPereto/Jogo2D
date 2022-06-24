import random
import pygame
from pygame.locals import *
from sys import exit

#pygame.mixer.music.set_volume()
#musicafundo = pygame.mixer.music.load('assets/MusicaFundo.mp3')
#pygame.mixer.music.play(-1)

#barulhocolisao = pygame.mixer.Sound('assets/smw_map_castle_crumbles.wav')


#tamanho da tela
x = 1280
y = 660
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Top Gun') #nome na janela ou nome do jogo

#cria nave inimiga, tamanho e rotação da imagem
naveInimiga = pygame.image.load("assets/Nave2.PNG.png").convert_alpha()
naveInimiga = pygame.transform.scale(naveInimiga,(50,50)) #define o tamanho da nave
naveInimiga = pygame.transform.rotate(naveInimiga, 90   )

#posição inicial da nave inimiga
pos_naveInimiga_x = 500
pos_naveInimiga_y = 360

#cria a nave do jogador
navePlayer = pygame.image.load("assets/Nave1.PNG.png").convert_alpha()
navePlayer = pygame.transform.scale(navePlayer,(60,60)) #define o tamanho da nave
navePlayer = pygame.transform.rotate(navePlayer, -90)

#posição inicial da nave do jogador
pos_navePlayer_x = 100
pos_navePlayer_y = 275

#imagem, tamanho e alinhamento e posição do missil
missil = pygame.image.load("assets/Missil.png").convert_alpha()
missil = pygame.transform.scale(missil,(50,14))
missil = pygame.transform.rotate(missil, 180)
vel_x_missil = 0
pos_x_missil = 100
pos_y_missil = 300

#função para associar a colisão, podendo somar os pontos após cada acontecimento programado no jogo
pontos = 1

triggered = False #para manter o missil parado e ser ativado pelo jogador ao precionar a tecla definida


rodando = True

#Fução para escolher a fonte e o tamanho do placar na tela do jogo
#font = pygame.font.SysFont('assets/fontpixel.ttf' 5a)

#transforma as imagens por assim dizer dentro do jogo, assumirem papeis de objetos
player_rect = navePlayer.get_rect()
naveInimiga_rect = naveInimiga.get_rect()
missil_rect = missil.get_rect()


#define imagem de fundo e nas proporções de altura e largura
bg = pygame.image.load('assets/Fundo.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))



#funções de respawn
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = pos_navePlayer_x
    respawn_missil_y = pos_navePlayer_y+24
    vel_x_missil = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]


#função para ativar a colisão e regra do jogo
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
    #barulhocolisao.play()

#loop para fazer rodar o jogo
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0, 0))

#cria movimentação do fundo
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0)) #cria bg novamente em carrossel
    if rel_x < 1200:
        screen.blit(bg, (rel_x,0))
#velocidade do fundo
    x-=0

#teclas de movimento, define que telhas serão do movimento no programa
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w] and pos_navePlayer_y > 1:
        pos_navePlayer_y -= 1
        if not triggered:
            pos_y_missil -= 1
#if not triggered = desprende o missil da nave
    if tecla[pygame.K_s] and pos_navePlayer_y < 600:
        pos_navePlayer_y += 1
        if not triggered:
            pos_y_missil += 1

    #tecla para disparar o missil
    if tecla[pygame.K_SPACE]:
        triggered = True #ao acionar o missil dispara pois está parado pela variavel triggered = false
        vel_x_missil = 2 #velocidade do missil


    #respawn, define a cordenada de respawn
    #posição nave inimiga
    if pos_naveInimiga_x == 50:
        pos_naveInimiga_x = respawn()[0]
        pos_naveInimiga_y = respawn()[1]

    #posição do missil
    if pos_x_missil == 1300:
        pos_x_missil, pos_y_missil,triggered, vel_x_missil = respawn_missil() #lista das variaveis

    #se a nave for atingida pelo missil / cordenada do respawn
    if pos_naveInimiga_x == 50 or colisao():
        pos_naveInimiga_x = respawn()[0]
        pos_naveInimiga_y = respawn()[1]

    #posição rect ou seja, associa o raio traçado ao objeto
    player_rect.y = pos_navePlayer_y
    player_rect.x = pos_navePlayer_x

    missil_rect.x = pos_x_missil
    missil_rect.y = pos_y_missil

    naveInimiga_rect.x = pos_naveInimiga_x
    naveInimiga_rect.y = pos_naveInimiga_y


    #movimento e velocidade dos itens
    x-=1
    pos_naveInimiga_x -= 1.5
    pos_x_missil += vel_x_missil #comando para o missil ganhar movimento próprio
    
    #caso tire as # abaixo, demarca o raio do objeto, podendo definir cor do raio e grossura do traçado
    #pygame.draw.rect(screen, (255,0,0), player_rect, 4)
    #pygame.draw.rect(screen, (255,0,0), naveInimiga_rect, 4)
    #pygame.draw.rect(screen, (255,0,0), missil_rect, 4)

    #comando para aparecer o placar em meio ao jogo, marcando a pontuação
    #score = font.render(f' Pontos: {int(pontos)} ', True, (0,0,0))
    #screen.blit(score, (50,50))

    #criada imagens na tela do jogo
    screen.blit(naveInimiga, (pos_naveInimiga_x, pos_naveInimiga_y))
    screen.blit(missil, (pos_x_missil, pos_y_missil)) #posição definir acima da nave para não sobrepor
    screen.blit(navePlayer, (pos_navePlayer_x, pos_navePlayer_y))

    print(pontos)

    pygame.display.update()