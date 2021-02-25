import sys, os
import pygame
pygame.init()

size = width, height = 320, 240

# surface - il tipo dello schermo
screen = pygame.display.set_mode(size)

# classe che in realtà raccoglie i colori
class Colors:
    black   = 0,0,0
    white   = 255,255,255
    red     = 255,0,0
    green   = 0,255,0
    blue    = 0,0,255

fileToLoad = os.path.join(os.path.dirname(sys.argv[0]), "ring.png")
ball = pygame.image.load_extended(fileToLoad)
ball = pygame.transform.scale(ball, (50,50))
ballrect = ball.get_rect()

mouseDown = False

while True:
    # gestione degli eventi
    for event in pygame.event.get():
        # evento di chiusura
        if event.type == pygame.QUIT:
            # non servirebbe ma per pulizia lo chiamo
            pygame.quit()
            sys.exit()
        # evento click del mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and ballrect.collidepoint(event.pos):
            mouseDown = True    # ricorda lo stato
            ballrect.center = event.pos
        # si alza il mouse
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False   # ricorda lo stato
        # il mouse è stato mosso
        elif event.type == pygame.MOUSEMOTION and mouseDown:
            ballrect.center = event.pos

    screen.fill(Colors.black)
    screen.blit(ball, ballrect)
    # rende visibili le modifiche allo schermo
    pygame.display.flip()
    pass
