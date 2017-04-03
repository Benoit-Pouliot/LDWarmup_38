from scene.LogicHandler import *
from app.settings import *


class WhiteTitleSceneLogicHandler(LogicHandler):
    def __init__(self,data):
        super().__init__(data)

    def handle(self):
        super().handle()
        self.checkHighlight()

    def checkHighlight(self):
        mousePos = pygame.mouse.get_pos()
        for obj in self.data.notifySet:
            if obj.rect.collidepoint(mousePos):
                obj.isSelected = True
            else:
                obj.isSelected = False