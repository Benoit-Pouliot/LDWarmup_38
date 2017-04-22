from app.scene.platformScene.PlatformSceneData import PlatformSceneData
from app.sprites.bullet import *
from app.settings import *
from app.scene.platformScene.CollisionPlayerPlatform import CollisionPlayerPlatform
from app.tools.functionTools import *
import pygame

class PlatformSceneLogicHandler:
    def __init__(self, gameData):

        self.sceneRunning = True
        self.endState = None
        self.newMapData = None
        self.gameData = gameData
        self.mapData = gameData.mapData
        self.player = gameData.mapData.player
        self.collisionChecker = CollisionPlayerPlatform(self.player, self.mapData)

    def handle(self):
        self.applyGravity(self.mapData.allSprites)
        self.applyFriction(self.mapData.allSprites)
        self.collisionChecker.collisionAllSprites(self.player, self.mapData, self.gameData)
        self.handleZoneCollision(self.player)
        self.mapData.allSprites.update()
        self.handleBullets(self.mapData, self.player)
        self.gameOverCondition(self.player)

    def handleZoneCollision(self, player):
        for obj in self.mapData.tmxData.objects:
            if self.isPlayerIsInZone(player, obj) == True:
                if obj.name == "OutZone":
                    nameNewZone = obj.LevelZone
                    nameInZone = obj.InZone

                    # Initializing new map
                    self.newMapData = PlatformSceneData(nameNewZone, nameInZone)

    def isPlayerIsInZone(self, player, zone):

        if player.rect.centerx  >= zone.x and \
           player.rect.centerx <= zone.x + zone.width and \
           player.rect.centery >= zone.y and \
           player.rect.centery <= zone.y + zone.height:
           return True
        else:
           return False

    def applyGravity(self, allSprites):
        for sprite in allSprites:
            if sprite.isPhysicsApplied == True or sprite.isGravityApplied == True:
                sprite.speedy += GRAVITY

    def applyFriction(self, allSprites):
        for sprite in allSprites:
            if sprite.isPhysicsApplied == True or sprite.isFrictionApplied == True:
                pass
                if sprite.speedx > 0 and sprite.speedx - FRICTION > 0:
                    sprite.speedx -= FRICTION
                elif sprite.speedx > 0:
                    sprite.speedx = 0

                if sprite.speedx < 0 and sprite.speedx + FRICTION < 0:
                    sprite.speedx += FRICTION
                elif sprite.speedx < 0:
                    sprite.speedx = 0

    def handleBullets(self, mapData, player):
        for bullet in mapData.friendlyBullet:
            if type(bullet) == Bullet:
                collisionBulletWall(bullet, mapData)
                collisionBulletWall(bullet, mapData)
                collisionBulletEnemy(bullet, mapData)
        for bullet in mapData.enemyBullet:
            if type(bullet) == SpiritBullet:
                pass
            else:
                collisionBulletWall(bullet, mapData)

        collisionBulletPlayer(mapData, player)

    def gameOverCondition(self,player):
        if player.isAlive == False:
            pygame.display.flip()
            pygame.time.wait(2000)
            self.newMapData = MapData('WorldMap', 'StartPointWorld')
            self.sceneRunning = False