import inputs
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 1500

GAMES, GAMES_DATA, STUDY_INFO = inputs.main_input()
GAMES_AMOUNT = len(GAMES)

SOLDIER_HEIGHT = 80
SOLDIER_WIDTH = 20

DISTANCE = WINDOW_WIDTH / GAMES_AMOUNT

MAZE_IMG = pygame.image.load("maze.png")
MAZE_IMG = pygame.transform.scale(MAZE_IMG, (30, 30))

IMAGES_DICT = {"1": MAZE_IMG}

IMAGES = [IMAGES_DICT.get(game) for game in GAMES]
