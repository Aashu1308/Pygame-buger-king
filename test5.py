import pygame
from pygame.locals import *
import sys


class Player:
    def __init__(self):
        self.rect = pygame.draw.rect(
            display, (255, 0, 0), (100, 100, 100, 100))


pygame.init()
display = pygame.display.set_mode((300, 300))
FPS_CLOCK = pygame.time.Clock()
player = Player()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on the Player")

    pygame.display.update()
    FPS_CLOCK.tick(30)
