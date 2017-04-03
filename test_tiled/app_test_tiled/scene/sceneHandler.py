from test_tiled.app_test_tiled.settings import *
from test_tiled.app_test_tiled.scene.worldMap.worldMap import WorldMap
from test_tiled.app_test_tiled.scene.titleScreen.titleScreen import TitleScreen

from test_tiled.app_test_tiled.scene.platformScreen.platformScreen import PlatformScreen
from test_tiled.app_test_tiled.gameData import GameData


class SceneHandler:
    def __init__(self, screen, firstScene=None):

        self.handlerRunning = True
        self.runningScene = firstScene
        self.screen = screen
        self.gameData = GameData(firstScene)


    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.runningScene.mainLoop()

            #When we exit the scene, this code executes
            if self.runningScene.nextScene == TITLE_SCREEN:
                self.runningScene = TitleScreen(self.screen, self.gameData)
            elif self.runningScene.nextScene == WORLD_MAP:
                self.runningScene = WorldMap(self.screen, self.gameData)
            elif self.runningScene.nextScene == PLATFORM_SCREEN:
                self.runningScene = PlatformScreen(self.screen, self.gameData)

