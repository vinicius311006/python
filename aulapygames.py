import time
import pygame

pygame.init()

tela = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Olá mundo")
tela.fill([255, 0, 255]) #cor da tela

pygame.display.flip() #excuta na tela

time.sleep(15) #segura a janela


