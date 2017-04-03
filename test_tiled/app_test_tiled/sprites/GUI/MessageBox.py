import pygame
import os
from test_tiled.app_test_tiled.settings import *
from test_tiled.app_test_tiled.sprites.GUI.Box import Box


class MessageBox(pygame.sprite.Sprite):
    def __init__(self,pos, size, text):
        super().__init__()

        x = size[0]
        y = size[1]

        box = Box(pos,size)

        self.image = box.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.arial = pygame.font.SysFont("Arial", 20)
        self.text = self.arial.render(text, False, BLACK)

        boxRect = box.box.get_rect()
        textRect = self.text.get_rect()
        textRect.center = boxRect.center

        box.box.blit(self.text, textRect)