import inputs
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
SCREEN_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

GAMES, GAMES_DATA, STUDY_INFO, FILES = inputs.main_input()
# GAMES, GAMES_DATA, STUDY_INFO, FILES = ["1"], ["DSD", "D","F","g","H", 2], ['Maze1.csv']
POP_WINDOW_FONT_SIZE = int(0.1 * WINDOW_WIDTH)
POP_WINDOW_FONT_LOCATION = (int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2))
FONT_NAME = 'Calibri'
GAMES_AMOUNT = len(GAMES)
POP_UP_COLOR = (209, 237, 212)

SOLDIER_HEIGHT = 200
SOLDIER_WIDTH = 120

BACKGROUND = (17, 150, 34)

DISTANCE = WINDOW_WIDTH / (GAMES_AMOUNT + 1)

MAZE_IMG = pygame.image.load("maze.png")
MAZE_IMG = pygame.transform.scale(MAZE_IMG, (60, 60))

FLAG_IMAGE = pygame.image.load("flag_5188014.png")
FLAG_IMAGE = pygame.transform.scale(FLAG_IMAGE, (60, 60))

IMAGES_DICT = {"1": MAZE_IMG, "2": FLAG_IMAGE}

IMAGES = [IMAGES_DICT.get(game) for game in GAMES]

SOLDIER_IMG = pygame.image.load("soldier.png")
SOLDIER_IMG = pygame.transform.scale(SOLDIER_IMG, (SOLDIER_WIDTH, SOLDIER_HEIGHT))





LOGO_IMAGE = pygame.image.load("preview.webp")
LOGO_IMAGE = pygame.transform.scale(LOGO_IMAGE, SCREEN_SIZE)