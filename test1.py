import pygame
from pygame.locals import *


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((0, 200, 255))
        self.rectangle = self.surface.get_rect()


pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Squares on a board")

square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()

image = pygame.image.load("images/saber.jpeg")
icon = pygame.image.load("images/saber.jpeg")

pygame.display.set_icon(icon)

pygame.time.delay(5000)


game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                game_on = False
        elif event.type == QUIT:
            game_on = False

    screen.fill((0, 0, 0))

    screen.blit(image, (100, 100))

    screen.blit(square1.surface, ((40, 40)))
    screen.blit(square2.surface, ((40, 530)))
    screen.blit(square3.surface, ((730, 40)))
    screen.blit(square4.surface, ((730, 530)))

    pygame.display.flip()
