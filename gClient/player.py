import os, pygame
from pygame.locals import *
from pygame.compat import geterror
#initialize pygame and screen dimensions
pygame.init()
screen = pygame.display.set_mode((640, 480))

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'pics')
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

#define a character class for each character rendered on screen
class Character(pygame.sprite.Sprite):
    #class variables
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "bigboi"
        self.x = 0
        self.y = 0
        self.dead = False
        self.weapon = "none"
        self.image, self.rect = load_image('prisoner.png', -1)

#define class for local character
class Player(Character):
    #define acceleration on the local platform
    def __init__(self):
        Character.__init__(self)
        self.move = 10
        self.area = screen.get_rect()
        self.x = 320
        self.y = 240
        self.xaccel = 0
        self.yaccel = 0
        self.xspeed = 0
        self.yspeed = 0
        self.rect.topleft = self.x,self.y

    #use acceleration to make movement smooth
    def _move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.xspeed += self.xaccel
        self.yspeed += self.yaccel
        print(self.x)
        #self.yaccel -= 1

    def move_l(self):
        self.xaccel = -5

    def move_r(self):
        self.xaccel = 5

    def jump(self):
        self.yaccel = 5

    def get_speed(self):
        return self.xspeed,self.yspeed

    #def _walk(self):
    #    "move the monkey across the screen, and turn at the ends"
    #    newpos = self.rect.move((self.move, 0))
    #    if self.rect.left < self.area.left or \
    #        self.rect.right > self.area.right:
    #        self.move = -self.move
    #        newpos = self.rect.move((self.move, 0))
    #        self.image = pygame.transform.flip(self.image, 1, 0)
    #    self.rect = newpos

    #def update(self):
    #    self._walk()
    #use pygame input senses to change acceleration
    def _control(self):
        events = pygame.event.get()
        for event in     events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.xaccel = -5
                if event.key == pygame.K_a:
                    self.xaccel = 5
                if event.key == pygame.K_w:
                    self.yaccel = 10

    def update(self):
        self._move()
        self._control()
