import pygame
from pygame.locals import *


def Get_Center(surface):
    width, height = pygame.display.get_window_size()
    if isinstance(surface, Square):
        center = width//2 - surface.rectangle.width//2, height//2 - \
            surface.rectangle.height//2
    else:
        center = width//2 - surface.get_width()//2, height//2 - surface.get_height()//2
    return center


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((0, 200, 255))
        self.rectangle = self.surface.get_rect()
        self.grow = True

    def inflate(self):
        if self.grow:
            self.rectangle.inflate_ip(4, 4)
            self.surface = pygame.Surface(
                (self.rectangle.width, self.rectangle.height))
            self.surface.fill((0, 200, 255))
            self.grow = self.rectangle.width < 50
        else:
            self.rectangle.inflate_ip(-4, -4)
            self.surface = pygame.Surface(
                (self.rectangle.width, self.rectangle.height))
            self.surface.fill((0, 200, 255))
            self.grow = self.rectangle.width < 25


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        pygame.display.set_caption("Squares on a board")
        self.screen.fill((0, 0, 0))

        self.square1 = Square()
        self.square2 = Square()
        self.square3 = Square()
        self.square4 = Square()

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

            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.square1.rectangle.collidepoint(mouse_pos):
                    self.square1.inflate()
                elif self.square2.rectangle.collidepoint(mouse_pos):
                    self.square2.inflate()
                elif self.square3.rectangle.collidepoint(mouse_pos):
                    self.square3.inflate()
                elif self.square4.rectangle.collidepoint(mouse_pos):
                    self.square4.inflate()

    def run(self):
        while True:
            self.clock.tick(60)

            self._handle_events()

            top_left = Get_Center(self.image)
            self.screen.blit(
                self.image, self.image.get_rect(topleft=top_left))
            self.screen.blit(self.square1.surface, ((40, 40)))
            self.screen.blit(self.square2.surface, ((40, 530)))
            self.screen.blit(self.square3.surface, ((730, 40)))
            self.screen.blit(self.square4.surface, ((730, 530)))

            pygame.display.flip()


pygame.init()
game = Game()
game.run()
