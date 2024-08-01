import time
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.init()

tela =pygame.display.set_mode((640, 480))

font = pygame.font.SysFont('impact', 100)

pygame.display.set_caption('Olá mundo')

tela.fill(BLACK)

pygame.draw.line(tela, WHITE, [10, 100], [630, 100], 5) # ultimo valor e a font white

pygame.draw.rect(tela,BLUE, [200,210,40,20])

pygame.draw.ellipse(tela, RED, [300, 200, 40, 40])

pygame.draw.polygon(tela, GREEN, [[420, 200], [440, 240], [400, 240], [400, 240]])

pygame.display.flip() #excuta na tela, atualizar tela

time.sleep(5) #segura a janela

#tela.fill(BLACK)

text = font.render('Olá mundo', True, WHITE)

tela.blit(text, [100, 200])

pygame.display.flip() #excuta na tela, atualizar tela

time.sleep(5) #segura a janela