import pygame
from pygame.locals import *


def Get_Center(surface):
    width, height = pygame.display.get_window_size()
    center = width//2 - surface.get_width()//2, height//2 - surface.get_height()//2
    return center


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Square, self).__init__()
        self.rect = pygame.draw.rect(
            screen, (0, 200, 255), (x, y, 25, 25))

    def update(self):
        print("Mouse clicked inside rectangle")


class Game:
    def __init__(self):
        pygame.display.set_caption("Squares on a board")

        self.square1 = Square(40, 40)
        self.square2 = Square(40, 530)
        self.square3 = Square(730, 40)
        self.square4 = Square(730, 530)

        self.icon = pygame.image.load("images/borgar_king.jpeg")
        self.image = pygame.image.load("images/saber.jpeg")

        pygame.display.set_icon(self.icon)

        self.clock = pygame.time.Clock()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE or event.key == K_ESCAPE:
                    pygame.quit()
                    raise SystemExit

            if event.type == MOUSEBUTTONDOWN:
                if self.square1.rect.collidepoint(pygame.mouse.get_pos()):
                    self.square1.update()
                elif self.square2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.square2.update()
                elif self.square3.rect.collidepoint(pygame.mouse.get_pos()):
                    self.square3.update()
                elif self.square4.rect.collidepoint(pygame.mouse.get_pos()):
                    self.square4.update()
                else:
                    print("Mouse clicked outside rectangle",
                          pygame.mouse.get_pos())

    def run(self):
        while True:
            self.clock.tick(60)

            self._handle_events()
            '''group = pygame.sprite.Group(
                [self.square1, self.square2, self.square3, self.square4])
            group.update()'''

            top_left = Get_Center(self.image)
            screen.blit(
                self.image, self.image.get_rect(topleft=top_left))

            '''screen.blit(self.square1.surface, ((40, 40)))
            screen.blit(self.square2.surface, ((40, 530)))
            screen.blit(self.square3.surface, ((730, 40)))
            screen.blit(self.square4.surface, ((730, 530)))'''

            pygame.display.flip()


pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill((0, 0, 0))

game = Game()

game.run()
