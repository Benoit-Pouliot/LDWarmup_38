# Imports
import os
import sys

import pygame

from app.sprites.GUI.Button import Button
from app.settings import *

import weakref


class WhiteTitleSceneData:
    def __init__(self):
        self.nextScene = None

        self.notifySet = weakref.WeakSet()
        self.allSprites = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()

        # Création du background
        self.background = pygame.sprite.Sprite()
        self.background.rect = pygame.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.background.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.image.fill((250,250,250))
        self.allSprites.add(self.background)


        self.camera = None

        self.createStartMenu()

    def createStartMenu(self):
        self.instructionButton = Button((540, 10 * SCREEN_HEIGHT / 20), (150, 50), 'Back to black', self.goToTitleScene)
        self.spritesHUD.add(self.instructionButton)
        self.notifySet.add(self.instructionButton)

        self.exitButton = Button((540, 15 * SCREEN_HEIGHT / 20), (150, 50), 'Exit', sys.exit)
        self.spritesHUD.add(self.exitButton)
        self.notifySet.add(self.exitButton)

    def goToTitleScene(self):
        self.nextScene = TITLE_SCENE