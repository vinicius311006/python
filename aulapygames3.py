import time
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
cor = RED

pygame.init()

tela =pygame.display.set_mode((640, 480))

# bola
posicao_x = 300
posicao_y = 200
velocidade_x = 1
velocidade_y = 1

while True:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    posicao_x += velocidade_x
    posicao_y += velocidade_y

    if posicao_x > 600:
        velocidade_x = -0.1
        cor = RED
    elif posicao_x < 0:
        velocidade_x = 0.1
    if posicao_y > 440:
        velocidade_y = -0.1
        cor = GREEN
    elif posicao_y < 0:
        velocidade_y = 0.1

    tela.fill(BLACK)
    pygame.draw.ellipse(tela, cor, [posicao_x, posicao_y, 40 , 40])
    pygame.display.flip()
