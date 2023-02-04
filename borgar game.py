import pygame
import random
import time
from pygame.locals import *

pwidth = 250
pheight = 256


'''def Get_Center(surface):
    width, height = WIDTH, HEIGHT
    center = width//2 - surface.get_width()//2, height//2 - surface.get_height()//2
    return center'''


class Borgar(pygame.sprite.Sprite):
    def __init__(self, screen, centerx, centery):
        super(Borgar, self).__init__()
        self.surface = pygame.image.load("images/borgar.jpeg").convert()
        self.surface.set_colorkey((0, 0, 0))
        self.rect = self.surface.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.screen = screen

    def draw(self):
        self.screen.blit(self.surface, self.rect)


class player(pygame.sprite.Sprite):
    def __init__(self, screen, centerx, centery):
        super(player, self).__init__()
        self.surface = pygame.image.load("images/saber.png").convert_alpha()
        pygame.Surface.convert_alpha(self.surface)
        self.screen = screen
        self.speed = 10
        self.dir = ''
        self.rect = self.surface.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.width = self.rect.width
        self.height = self.rect.height

    def draw(self):
        self.screen.blit(self.surface, self.rect)

    def move(self):
        if self.dir != '':
            if self.dir == 'd' and self.rect.bottom < 600:
                self.rect.top += self.speed
            if self.dir == 'u' and self.rect.top > 0:
                self.rect.top -= self.speed
            if self.dir == 'l' and self.rect.left > 0:
                self.rect.left -= self.speed
            if self.dir == 'r' and self.rect.right < 800:
                self.rect.right += self.speed


class Background:
    def __init__(self):
        self.image = pygame.image.load("images/bkbackground.jpeg")
        self.rect = self.image.get_rect()
        self.location = [0, 0]
        self.rect.left, self.rect.top = self.location


class Label(pygame.sprite.Sprite):
    def __init__(self, screen, centerx, centery, msg, size):
        super(Label, self).__init__()
        self.screen = screen
        font1 = pygame.font.SysFont("futura", size)
        self.text = font1.render(msg, True, (0, 255, 0))
        self.rect = self.text.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def draw(self):
        self.screen.blit(self.text, self.rect)
        pygame.display.flip()


class Game:
    def __init__(self, screen):

        self.screen = screen
        self.screen.fill((255, 255, 255))

        self.background = Background()
        self.screen.blit(self.background.image, self.background.rect)

        self.icon = pygame.image.load("images/borgar_king.jpeg")
        pygame.display.set_icon(self.icon)

        self.foods = []
        self.eaten = 0

        for i in range(4):
            self.foods.append(Borgar(
                self.screen, WIDTH*random.randint(1, 9)//10, HEIGHT*random.randint(1, 9)//10))
        '''for f in self.foods:
            f.draw()'''

        self.player = player(screen, WIDTH//2, HEIGHT//2)
        self.mainclock = pygame.time.Clock()
        self.start_time = time.perf_counter()
        self.end_time = -1
        self.won = False

    def update(self):
        for f in self.foods:
            if self.player.rect.colliderect(f.rect):
                self.foods.remove(f)
                self.foods.append(Borgar(
                    self.screen, WIDTH*random.randint(1, 9)//10, HEIGHT*random.randint(1, 9)//10))
                self.eaten += 1
                print(self.eaten)
        for f in self.foods:
            f.draw()
        msg = "Eaten: {:d}".format(self.eaten)
        l = Label(self.screen, 650, 75, msg, 26)
        if self.eaten == 20:
            self.won = True
            self.end_time = time.perf_counter()
            print("You won")
            print("time taken: {:.2f}".format(self.end_time-self.start_time))
        self.player.move()
        self.player.draw()
        l.draw()
        pygame.display.flip()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE or event.key == K_ESCAPE or event.key == ord('q'):
                    raise SystemExit
                if event.key == K_LEFT or event.key == ord('a'):
                    self.player.dir = 'l'
                if event.key == K_RIGHT or event.key == ord('d'):
                    self.player.dir = 'r'
                if event.key == K_UP or event.key == ord('w'):
                    self.player.dir = 'u'
                if event.key == K_DOWN or event.key == ord('s'):
                    self.player.dir = 'd'
            if event.type == KEYUP:
                # End repetition.
                if event.key == K_LEFT or event.key == ord('a'):
                    self.player.dir = ''
                if event.key == K_RIGHT or event.key == ord('d'):
                    self.player.dir = ''
                if event.key == K_UP or event.key == ord('w'):
                    self.player.dir = ''
                if event.key == K_DOWN or event.key == ord('s'):
                    self.player.dir = ''

    def run(self):
        while True:
            self.mainclock.tick(20)
            self.screen.blit(self.background.image, self.background.rect)
            self._handle_events()
            self.update()
            if self.won:
                self.screen.fill((0, 0, 128))
                pygame.display.update()
                msg = "YOU WON!! Time Taken is: {:.2f}".format(
                    self.end_time-self.start_time)
                l = Label(display, WIDTH//2, HEIGHT//2, msg, 32)
                l.draw()
                time.sleep(5)
                raise SystemExit
            pygame.display.flip()


pygame.init()

display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Borgar King")
game = Game(display)

game.run()
