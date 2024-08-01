import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
cor = RED

pygame.init()

tela =pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game Loop")

relogio = pygame.time.Clock()

jogador_pos = pygame.Vector2(tela.get_width() / 2, tela.get_height() / 2)

jogador2_pos = pygame.Vector2(100,60)
velocidade = 1

while True:
    fps = relogio.tick(30)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        jogador_pos.y -= velocidade * fps
    if keys[pygame.K_s]:
        jogador_pos.y += velocidade * fps
    if keys[pygame.K_a]:
        jogador_pos.x -= velocidade * fps
    if keys[pygame.K_d]:
        jogador_pos.x += velocidade * fps            

    #jogador 2
    if keys[pygame.K_UP]:
        jogador2_pos.y -= 2 * fps
    if keys[pygame.K_DOWN]:
        jogador2_pos.y += 2 * fps
    if keys[pygame.K_LEFT]:
        jogador2_pos.x -= 2 * fps
    if keys[pygame.K_RIGHT]:
        jogador2_pos.x += 2 * fps            

    tela.fill(BLACK)
    pygame.draw.rect(tela, cor, (jogador_pos.x, jogador_pos.y, 50, 50))
    pygame.draw.rect(tela, cor, (jogador2_pos.x, jogador2_pos.y, 50, 50))
    pygame.display.flip()
                         
