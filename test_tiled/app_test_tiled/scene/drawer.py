import pygame
from test_tiled.app_test_tiled.settings import *

class Drawer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = FPS

    def draw(self, screen, camera, spritesHUD, player):

        if camera != None:
            camera.center(player.rect.center)
            camera.draw(screen)

        spritesHUD.draw(screen)
        pygame.display.flip()
        self.clock.tick(self.FPS)
