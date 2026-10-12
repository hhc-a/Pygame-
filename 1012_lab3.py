import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Step 3 - draw.rect 基礎語法")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((245, 240, 230))

    for j in range(10):
        for i in range(10):
            pygame.draw.rect(screen, (183, 212, 135), (50+i*50, 50+50*j, 40, 40))
            pygame.draw.rect(screen, (20, 43, 64), (50+i*50, 50+50*j, 40, 40), 2)

    pygame.display.flip()