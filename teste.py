import pygame
import random
 
 
black= (0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,0)
 
pygame.get_init()
tela=pygame.display.set_mode((640,480))
pygame.display.set_caption('pygame impacto')
 
quadrado= pygame.Rect(300,random.randint(0,460),20,20)
jogador=pygame.Vector2(20,210)
jogador2=pygame.Vector2(600,210)
joadorPontos=0
jogador2Pontos=0
velocidade=0.2
velocidadeY=0.2
relogio=pygame.time.Clock()
color=white

 
while True:
    fps=relogio.tick(60)
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jogador.y-=10
    if keys[pygame.K_s]:
        jogador.y+=10
    if keys[pygame.K_UP]:
        jogador2.y-=10
    if keys[pygame.K_DOWN]:
        jogador2.y+=10
 
 
 
    tela.fill(black)
    pa1=pygame.draw.rect(tela,white,[jogador.x,jogador.y,20,60])
    pa2=pygame.draw.rect(tela,white,[jogador2.x,jogador2.y,20,60])
    pygame.draw.rect(tela,white,quadrado)
 
    quadrado.move_ip( velocidade * fps,velocidadeY*fps) #comando para iniciar a bolinha movimentando
 
    if quadrado.colliderect(pa1):
        color=red
        velocidade= -velocidade
    if quadrado.colliderect(pa2):
        color=bluevelocidade= -velocidade
   
 
    fonte = pygame.font.SysFont('arial', 30)
    texto = f'Jogador 1 = {joadorPontos} \|/ Jogador 2 = {jogador2Pontos}'
    texto = fonte.render(texto, True, yellow)
    tela.blit(texto, [150,10])
 
    if quadrado.x<0:
        color=white
        quadrado = pygame.Rect(300,random.randint(0,460),20,20)
        jogador2Pontos+=1
    if quadrado.x>620:
        color=white
        quadrado = pygame.Rect(300,random.randint(0,460),20,20)
        joadorPontos+=1
    if quadrado.y>460:
        velocidadeY= -velocidadeY
       
    if quadrado.x<0:
        velocidadeY= -velocidadeY
   
    if jogador.y<0:
        jogador.y=0
    if jogador.y>420:
        jogador.y=420
    if jogador2.y<0:
        jogador.y=0
    if jogador2.y>420:
        jogador.y=420
 
    pygame.display.flip()