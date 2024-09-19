import inputs
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
SCREEN_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# GAMES, GAMES_DATA, STUDY_INFO = inputs.main_input()
GAMES, GAMES_DATA, STUDY_INFO = ["1", "1", "1"], ["DSD", "D","F","g","H", 2], ["FFFFFFFFFFFFFFF"]
POP_WINDOW_FONT_SIZE = int(0.1 * WINDOW_WIDTH)
POP_WINDOW_FONT_LOCATION = (int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2))
FONT_NAME = 'Calibri'
GAMES_AMOUNT = len(GAMES)
POP_UP_COLOR = (209, 237, 212)

SOLDIER_HEIGHT = 200
SOLDIER_WIDTH = 80

BACKGROUND = (17, 150, 34)

DISTANCE = WINDOW_WIDTH / (GAMES_AMOUNT + 1)

MAZE_IMG = pygame.image.load("maze.png")
MAZE_IMG = pygame.transform.scale(MAZE_IMG, (60, 60))

IMAGES_DICT = {"1": MAZE_IMG}

IMAGES = [IMAGES_DICT.get(game) for game in GAMES]

SOLDIER_IMG = pygame.image.load("soldier.png")
SOLDIER_IMG = pygame.transform.scale(SOLDIER_IMG, (SOLDIER_WIDTH, SOLDIER_HEIGHT))

STOPS = [[390, 100], [420, 140], [410, 190], [371, 227],
         [348, 254], [313, 290], [268, 322], [236, 370], [208, 430],
         [200, 483], [213, 560], [239, 617], [295, 670],
         [349, 670], [460, 587], [586, 426], [646, 367], [720, 374],
         [750, 444], [750, 540], [720, 707], [634, 806], [471, 890]]


