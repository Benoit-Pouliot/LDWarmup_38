# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (160, 160, 0)
GREY = (100, 100, 100)
PURPLE = (128, 0, 128)

COLORKEY = (1, 1, 1)

COLOR_POWER_BAR = (100,50,138)
COLOR_POWER_BAR_EMPTY = (0,0,0,1)

BACKGROUND_COLOR = (255,255,255)

#Main font
FONT_NAME = 'arial'

FPS = 60

#EPSILON
EPS = 0.000001

#DIMENSION
# http://gamedevelopment.tutsplus.com/articles/quick-tip-what-is-the-best-screen-resolution-for-your-game--gamedev-14723
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_WIDTH = 32
TILE_HEIGHT = 32

# Development mode, DEV or OPT
DEV_MODE = 1
OPT_MODE = 0
MODE = DEV_MODE

# To get which mouse button is pressed.
MOUSE_LEFT = 1
MOUSE_RIGHT = 3

#Scenes self.nextScene commands, used to tell SceneHandler what next scene to run after this one ends
TITLE_SCREEN = 0
SHOP_SCREEN = 1
INSTRUCTION_SCREEN = 911
CREDIT_SCREEN = 811
WIN_SCREEN = 3
GAME_OVER_SCREEN = 4
CREDIT_SCREEN = 5

PLATFORM_SCREEN = 42

# Sprite Layer
SPRITE_LAYER = 4
CAMERA_HUD_LAYER = 5

#Facing Sides
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

#Collisions
COLLISION_LAYER = 0
SOLID = 1 #Booléen de GID pour collision
ENTRANCEWALL = 2
SPRING = 3
LADDER = 4
NONE = 5 #Pour identifier qu'il n'y a eu aucune collision

OBSTACLE = 100 #This is not a tile

#Player jump states
GROUNDED = 0
JUMP = 1
CLIMBING = 2 #When on a ladder

#Physics
GRAVITY = 1
FRICTION = 1

#Projectiles
GRENADE_SPEEDX = 2
GRENADE_SPEEDY = 2
BARRICADE_DISTANCE = 50
TARGET_DISTANCE = BARRICADE_DISTANCE

#ENEMY MODE
WALKING = 1
PREPARE_ATTACK = 2
IN_ATTACK = 3

POWER_CAP = 9
RATIO = 5

# Dimension tile base for icon
TILEDIMX = 32
TILEDIMY = 32

# Dimension tile base for enemy
ENEMY_DIMX = 20
ENEMY_DIMY = 20

# Dimension tile base for player
PLAYER_DIMX = 21
PLAYER_DIMY = 21

# End level condition
PLAYER_DEAD = 0
LEVEL_WON = 1
LAST_LEVEL_WON =6

#GUI settings
DIALOG_TEXT_SIZE = 20
INPUT_BOX_FONT = "Arial"
INPUT_BOX_TEXT_SIZE = 20
MENU_FONT = "Arial"

COLOR_MENU_FONTS = WHITE
COLOR_MENU_1 = (41,41,39)
COLOR_MENU_2 = (142,120,12)
COLOR_MENU_SELECT_1 = (128,0,0)
COLOR_MENU_SELECT_2 = (204,255,255)
COLOR_MENU_FONTS_SELECT = WHITE

HUD_FONT_COLOR = WHITE
HUD_FONT_SIZE = 20
HUD_HEIGHT = 40
HUD_COLOR_1 = COLOR_MENU_1
HUD_COLOR_2 = (128,0,0)

FULL_LOAD_COLOR = (0,0,255)
LOADING_COLOR = COLOR_MENU_2

# If you add a Tag for debugging, you MUST set it here at 0 for everyone
# You can turn your tag on in your own settings_local.py for personal use

TAG_BP = 0
TAG_MARIE = 0
TAG_PHIL = 0

# Load settings_local.py if exist
try:
    from test_tiled.app_test_tiled.Settings_local import *
except ImportError:
    pass