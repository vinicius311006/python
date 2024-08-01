import pygame
import random
lagura = 800
altura = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

pygame.init()
tela = pygame.display.set_mode((lagura, altura))
carro = pygame.Vector2(375,500)
velocidade_carro = 5

obstaculo_1 = pygame.Rect(random.randint(0,lagura), 0, 100,100)
obstaculo_2 = pygame.Rect(random.randint(0,lagura), 0, 100,100)

velocidade_ob = 0.5
velocidade_ob2 = 0.7
pontos = 0

relogio = pygame.time.Clock()
color = WHITE

carroimg = pygame.image.load('./img/car.png')
carroimg = pygame.transform.scale(carroimg, (100, 100))

obstaculo_1img = pygame.image.load("./img/obstaculo.png")
obstaculo_1img = pygame.transform.scale(obstaculo_1img, (100,100))

obstaculo_2img = pygame.image.load("./img/obstaculo2.png")
obstaculo_2img = pygame.transform.scale(obstaculo_2img,(100,100))

fundo = pygame.image.load('./img/fundo.png')
fundo = pygame.transform.scale(fundo, (lagura,altura))

som = pygame.mixer.Sound('./img/som.wav')
mover = pygame.mixer.Sound('./img/mover.wav')

def gemeover():
    fonte = pygame.font.Font(None, 50)
    texto_pontuacao = fonte.render(f'Pontuação: {pontos}', True, RED)
    fim = fonte.render('G A M E O V E R', True, WHITE)
    tela.blit(texto_pontuacao, (300, 220))
    tela.blit(fim, (280,300))
    pygame.display.flip()
    pygame.time.delay(5000)


while True:
    fps = relogio.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_d]:
        carro.x += velocidade_carro
        mover.play()
    if Keys[pygame.K_a]:
        carro.x -= velocidade_carro
        mover.play()
    if Keys[pygame.K_w]:
        carro.y -=10
    if Keys[pygame.K_s]:
        carro.y +=10

        

    tela.fill(BLACK)
    tela.blit(fundo, (0,0))
    obstaculo_1.move_ip(0 * fps, velocidade_ob * fps)
    obstaculo_2.move_ip(0 * fps, velocidade_ob2 * fps)

    carro = pygame.draw.rect(tela, BLACK,[carro.x, carro.y, 100,100])
    obstaculo_1 = pygame.draw.rect(tela, BLACK, [obstaculo_1.x, obstaculo_1.y, 100,100])
    obstaculo_2 = pygame.draw.rect(tela, BLACK, [obstaculo_2.x, obstaculo_2.y, 100,100])

    tela.blit(carroimg, (carro.x, carro.y))
    tela.blit(obstaculo_1img, (obstaculo_1.x, obstaculo_1.y))
    tela.blit(obstaculo_2img, (obstaculo_2.x, obstaculo_2.y))

    if obstaculo_1.y > 600:
        obstaculo_1 = pygame.Rect(random.randint(0,lagura), 0, 100,55)
        pontos += 1
        som.play()
    if obstaculo_2.y > 600:
        obstaculo_2 = pygame.Rect(random.randint(0,lagura), 0, 100,55)
        pontos += 1

    if obstaculo_1.x > 700:
        obstaculo_1.x = 700
    if obstaculo_1.x < 0:
        obstaculo_1.x = 0

    if obstaculo_2.x > 700:
        obstaculo_2.x = 700
    if obstaculo_2.x < 0:
        obstaculo_2.x = 0            

    if carro.x < 0:
        carro.x = 0
    if carro.x > 700:
        carro.x = 700

    if obstaculo_1.colliderect(carro) or obstaculo_2.colliderect(carro):
        fonte = pygame.font.SysFont('arial', 30)
        texto = fonte.render('Game Over', True, GREEN)
        texto2 = fonte.render(f'Pontos: {pontos}', True, GREEN)
        tela.blit(texto, [250, 250])
        tela.blit(texto2, [450, 250])
        pygame.display.flip()
        pygame.time.delay(5000)
        pontos = -2

    pygame.display.flip() 