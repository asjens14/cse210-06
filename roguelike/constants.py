from pickle import NONE
from game.casting.color import Color
import random
# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "RougeLike"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = 512
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "roguelike/assets/fonts\\zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "roguelike/assets/sounds\\boing.wav"
WELCOME_SOUND = "roguelike/assets/sounds\\start.wav"
OVER_SOUND = "roguelike/assets/sounds\\over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "a"
LEFT2 = "left"
RIGHT = "d"
RIGHT2 = "right"
UP = "w"
UP2 = "up"
DOWN = "s"
DOWN2 = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
I="i"
J="j"
K="k"
L="l"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4
YOU_WIN = 5

# LEVELS
LEVEL_FILE = "roguelike/assets/data/rooms\\room{}.txt"
ENEMY_FILE = "roguelike/assets/data/enemy_map\\room{}.txt"
BASE_LEVELS = 5
ROOMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(ROOMS)
ROOMS = [[ROOMS[0],ROOMS[1],ROOMS[2]],
        [ROOMS[3],ROOMS[4],ROOMS[5]], 
        [ROOMS[6],ROOMS[7],ROOMS[8]]]
ROOM_RIGHT = 2
ROOM_BOTTOM = 2

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5
current_lives = DEFAULT_LIVES
DIFFICULTY = 5
DIFFICULTY2 = 10

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "ROOM: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "roguelike/assets/images\\ball.png"
BALL_WIDTH = 32
BALL_HEIGHT = 32
BALL_VELOCITY = 6

#ENEMY BALL
ENEMY_BALL_GROUP = "enemyballs"


# PLAYER
PLAYER_GROUP = "players"
PLAYER_IMAGES = [f"roguelike/assets/images\\{n:03}.png" for n in range(100, 103)]
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32
PLAYER_RATE = 6
PLAYER_VELOCITY = 4

# ENEMY
ENEMY_GROUP = "enemies"
ENEMY_IMAGES = {
    "a": [f"roguelike/assets/images\\{n:03}.png" for n in range(110, 113)],
    "b": ["roguelike/assets/images\\113.png"],
    "c": ["roguelike/assets/images\\120.png"]
    }
ENEMY_WIDTH = 32
ENEMY_HEIGHT = 32
ENEMY_RATE = 6
ENEMY_VELOCITY = 4
ENEMY_LIVES = 1

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "0": [f"roguelike/assets/images\\000.png"],
    "1": [f"roguelike/assets/images\\010.png"],
    "d": [f"roguelike/assets/images\\000.png"]
}
BRICK_WIDTH = 32
BRICK_HEIGHT = 32
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_START = "PREPARING TO START"
WAS_GOOD_GAME = "GAME OVER"
WINNER = "YOU WIN!!"


#BOSS
BOSS_LIVES = 10
