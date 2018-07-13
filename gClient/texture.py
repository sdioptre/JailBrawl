import pygame
from player import Player

class Platform(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, player):
        pygame.sprite.Sprite.__init__(self)
        self.x = xpos
        self.y = ypos
        self.playname = player
        self.pxspeed, self.pyspeed = player.get_speed()
    def getRectPos(self):
        return (self.x, self.y)

    def draw_rect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.y, self.x, self.y+15, self.x+40], 0)
    def update(self,screen):
        self.pxspeed, self.pyspeed = self.playname.get_speed()
        self.x += self.pxspeed
        self.y += self.pyspeed
    #    print (self.x)
        self.draw_rect(screen)
