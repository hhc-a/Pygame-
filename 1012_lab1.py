import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("闕河正講師 — Pygame 基礎教學")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((245, 240, 230))
    pygame.display.flip()