import pygame

# pygame.init()
GUARD_WIDTH = 2
GUARD_HEIGHT = 3
GUARD_START = [0, 11]
SOLDIER_HEIGHT = 3
SOLDIER_WIDTH = 2
GRID_HEIGHT = 25
GRID_WIDTH = 50
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1500
FRAME_HEIGHT = int(SCREEN_HEIGHT / GRID_HEIGHT)
FRAME_WIDTH = int(SCREEN_WIDTH / GRID_WIDTH)
SOLDIER_X_LENGTH = SOLDIER_WIDTH * FRAME_WIDTH
SOLDIER_Y_LENGTH = SOLDIER_HEIGHT * FRAME_HEIGHT

FLAG_HEIGHT = 4
FLAG_WIDTH = 4

MINE_WIDTH = 3
MINE_HEIGHT = 1

GRASS_HEIGHT = 2
GRASS_WIDTH = 2

AMOUNT_MINE = 20

TELEPORT_HEIGHT = 1
TELEPORT_WIDTH = 3
TELEPORT_AMOUNT = 5

BACKGROUND_COLOR = (25, 115, 22)

START_MESSAGE = "Welcome"
FONT_NAME = "Calibri"
START_FONT_SIZE = int(0.15 * SCREEN_WIDTH)
START_COLOR = (0, 0, 0)
START_LOCATION = \
    (0.2 * SCREEN_WIDTH, SCREEN_HEIGHT / 2 - (START_FONT_SIZE / 2))

LOST_LOCATION = (0.25 * SCREEN_WIDTH, 30)
ONE_LINE_LENGTH = 49

NIGHT_COLOR = (6, 36, 5)

LOST_MASSAGE = "you lost"
WON_MASSAGE = "you won"

FLAG_IMAGE = pygame.image.load("flag.png")
FLAG_IMAGE = pygame.transform.scale(FLAG_IMAGE, (FLAG_WIDTH * FRAME_WIDTH, FLAG_HEIGHT * FRAME_HEIGHT))

GRASS_IMAGE = pygame.image.load("grass.png")
GRASS_IMAGE = pygame.transform.scale(GRASS_IMAGE, (GRASS_WIDTH * FRAME_WIDTH, GRASS_HEIGHT * FRAME_HEIGHT))

MINE_IMAGE = pygame.image.load("mine.png")
MINE_IMAGE = pygame.transform.scale(MINE_IMAGE, (MINE_WIDTH * FRAME_WIDTH, MINE_HEIGHT * FRAME_HEIGHT))

SOLDIER_IMAGE = pygame.image.load("soldier.png")
SOLDIER_IMAGE = pygame.transform.scale(SOLDIER_IMAGE, (SOLDIER_WIDTH * FRAME_WIDTH, SOLDIER_HEIGHT * FRAME_HEIGHT))

SOLDIER_NIGHT_IMAGE = pygame.image.load("soldier_nigth.png")
SOLDIER_NIGHT_IMAGE = pygame.transform.scale(SOLDIER_NIGHT_IMAGE,
                                             (SOLDIER_WIDTH * FRAME_WIDTH, SOLDIER_HEIGHT * FRAME_HEIGHT))

EXPLOSION_IMAGE = pygame.image.load("explosion.png")
EXPLOSION_IMAGE = pygame.transform.scale(EXPLOSION_IMAGE, (5 * FRAME_WIDTH, 5 * FRAME_HEIGHT))

keys_to_save = {pygame.K_1: 1,
                pygame.K_2: 2,
                pygame.K_3: 3,
                pygame.K_4: 4,
                pygame.K_5: 5,
                pygame.K_6: 6,
                pygame.K_7: 7,
                pygame.K_8: 8,
                pygame.K_9: 9}


GUARD_IMAGE = pygame.image.load("soldier (2).png")
GUARD_IMAGE = pygame.transform.scale(GUARD_IMAGE, (GUARD_WIDTH * FRAME_WIDTH, GUARD_HEIGHT * FRAME_HEIGHT))

# TP_IMAGE = pygame.image.load("hole.png")
# TP_IMAGE = pygame.transform.scale(TP_IMAGE, (TELEPORT_WIDTH * FRAME_WIDTH, TELEPORT_HEIGHT * FRAME_HEIGHT))

INJURY_IMAGE = pygame.image.load("injury.png")
INJURY_IMAGE = pygame.transform.scale(INJURY_IMAGE, (2 * FRAME_WIDTH, 4 * FRAME_HEIGHT))

