import pyscroll
import pytmx
import pygame
import os
import weakref

from app.settings import *
from app.sprites.playerPlatform import PlayerPlatform
from app.sprites.enemyFactory import EnemyFactory

class PlatformSceneData:
    def __init__(self,mapName="WorldMap", nameInZone="StartPointWorld", screenSize=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        self.nextScene = None

        self.notifySet = weakref.WeakSet()
        self.allSprites = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()

        # DEBUT MAP DATA

        self.nameMap = mapName

        self.tmxData = pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))
        self.tiledMapData = pyscroll.data.TiledMapData(self.tmxData)
        self.cameraPlayer = pyscroll.BufferedRenderer(self.tiledMapData, screenSize, clamp_camera=True)
        # self.soundController = soundPlayerController()

        self.allSprites = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.itemGroup = pygame.sprite.Group()
        self.friendlyBullet = pygame.sprite.Group()
        self.enemyBullet = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()

        eFactory = EnemyFactory()

        for obj in self.tmxData.objects:
            if obj.type == "enemy":
                enemy = eFactory.create(obj, self)
                self.allSprites.add(enemy)
                self.enemyGroup.add(enemy)

                # if obj.type == "item":
                #     item = iFactory.create(obj)
                #     self.allSprites.add(item)
                #     self.itemGroup.add(item)

        # Put camera in mapData
        self.camera = pyscroll.PyscrollGroup(map_layer=self.cameraPlayer, default_layer=SPRITE_LAYER)
        self.camera.add(self.allSprites)

        # Spawn point of the player
        valBool = False
        for obj in self.tmxData.objects:
            if obj.name == "InZone":
                if obj.StartPoint == nameInZone:
                    self.spawmPointPlayerx = obj.x
                    self.spawmPointPlayery = obj.y
                    valBool = True

        self.player = PlayerPlatform(self.spawmPointPlayerx, self.spawmPointPlayery, self)

        self.allSprites.add(self.player)
        self.camera.add(self.player)

    def close(self):
        self.sceneRunning = False

    def backToMain(self):
        self.nextScene = TITLE_SCENE
        self.gameData.typeScene = TITLE_SCENE

        self.close()

    def reqImageName(self, nameMap):
        return os.path.join('tiles_map', nameMap + ".tmx")