import pygame
import pyscroll
import pytmx
import pprint as pp
import re
import pygame
from test_tiled.app_test_tiled.settings import *
from test_tiled.app_test_tiled.tools.functionTools import *
import os

from test_tiled.app_test_tiled.tools.TmxData import TmxData
from test_tiled.app_test_tiled.sprites.enemyFactory import EnemyFactory
from test_tiled.app_test_tiled.sprites.itemFactory import ItemFactory
import weakref
# from test_tiled.app_test_tiled.sound.soundPlayerController import *
# from test_tiled.app_test_tiled.sprites.player import *

class MapData:
    def __init__(self, mapName="WorldMap", nameInZone="StartPointWorld", screenSize=(SCREEN_WIDTH, SCREEN_HEIGHT)):

        self.nameMap = mapName

        self.tmxData = pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))
        self.tiledMapData = pyscroll.data.TiledMapData(self.tmxData)
        self.cameraPlayer = pyscroll.BufferedRenderer(self.tiledMapData, screenSize, clamp_camera=True)
        # self.soundController = soundPlayerController()


        # TESTS BP_TAG
        pp.pprint(self.tmxData)
        layer = self.tmxData.get_layer_by_name("Background_TL")
        pp.pprint(layer)
        print(layer)
        pp.pprint(self.tmxData.__dict__)
        print("-------------------------")
        pp.pprint(self.tmxData.__dict__['layers'][0])
        firstLayer = pp.pformat(self.tmxData.__dict__['layers'][0])
        pp.pprint(firstLayer)
        firstLayer = re.findall(r'"([^"]*)"', firstLayer)[0]
        pp.pprint(firstLayer)
        print("-------------------------")
        pp.pprint(self.tmxData.__dict__['tiledgidmap'])
        pp.pprint(self.tmxData.tiledgidmap)
        print("-------------------------")
        pp.pprint(self.tmxData.__dict__['tiledgidmap'][2])
        print("-------------------------")
        layer = self.tmxData.get_layer_by_name(firstLayer)
        pp.pprint(layer.__dict__)

        pp.pprint(self.tmxData.get_tile_gid(0,0,0))
        pp.pprint(self.tmxData.get_tile_gid(0,0,1))
        pp.pprint(self.tmxData.get_tile_gid(1,0,1))

        print("-------------------------")
        print("-------------------------")
        myTmxData = TmxData(self.tmxData)
        print("-------------------------")


        self.allSprites = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.itemGroup = pygame.sprite.Group()
        self.friendlyBullet = pygame.sprite.Group()
        self.enemyBullet = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()
        self.notifySet = weakref.WeakSet() #Set of all object that needs to be notified of events. Weak references are used to prevent this set from keeping objects alive

        eFactory = EnemyFactory()
        iFactory = ItemFactory()

        for obj in self.tmxData.objects:
            if obj.type == "enemy":
                enemy = eFactory.create(obj, self)
                if enemy is not None:
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

        # The game is not complete?
        if valBool == False:
            quitGame()

    def reqImageName(self, nameMap):
        return os.path.join('tiles_map', nameMap + ".tmx")