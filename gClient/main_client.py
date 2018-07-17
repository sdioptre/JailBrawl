import os, sys, pygame
from texture import Platform
from player import Player
#flags = FULLSCREEN | DOUBLEBUF

class Client:

    def __init__(self):
        self.name = " "

    #def startup(self):




def main():
    pygame.init()
    running = True
    screen = pygame.display.set_mode((640, 480))
    #pygame.display.flip()
    player = Player()
    plat1 = Platform(100,100,player)
    allsprites = pygame.sprite.RenderPlain((player))
    clock = pygame.time.Clock()
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit(); sys.exit();
        keys=pygame.key.get_pressed()
        move_ticker = 0
        if keys[pygame.K_a]:
            if move_ticker == 0:
                move_ticker = 5
                player.move_l()
        elif keys[pygame.K_d]:
            if move_ticker == 0:
                move_ticker = 5
                player.move_r()
        else:
            player.stop()
        if move_ticker > 0:
            move_ticker -= 1
        #plat1.draw_rect(screen)
        screen.fill((0,0,0))
        plat1.update(screen)
        clock.tick(60)
        allsprites.update()
        allsprites.draw(screen)
        pygame.display.update()
        #print(clock.get_fps())
main()
