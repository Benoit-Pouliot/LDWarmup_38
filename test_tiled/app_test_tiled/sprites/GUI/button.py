import pygame
import os
from test_tiled.app_test_tiled.settings import *
from test_tiled.app_test_tiled.sprites.GUI.MessageBox import MessageBox


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, text, callback):
        super().__init__()

        self.messageBox = MessageBox(pos, size, text)
        self.image = self.messageBox.image
        self.rect = self.messageBox.rect
        self.callback = callback

    def notify(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()