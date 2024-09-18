import pygame.image

STOP_INPUT = "stop"

MAZE = "1"
GAMES = [MAZE]

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
# Grid size for maze:
GRID_HEIGHT = 15
GRID_WIDTH = 15
# Frame size for maze:
FRAME_HEIGHT = int(WINDOW_HEIGHT / GRID_HEIGHT)
FRAME_WIDTH = int(WINDOW_WIDTH / GRID_WIDTH)
MAZE_QUESTION_MAX_AMOUNT = 5

# maze asstes
BLACK_CUBE_ = pygame.image.load("cube_b.png")
WHITE_CUBE_ = pygame.image.load("cube_w.png")
PLAYER_ = pygame.image.load("player.png")
QUESTION_MARK_ = pygame.image.load("question-mark-sign-icon.png")
QUESTION_MARK = pygame.transform.scale(QUESTION_MARK_, (100, 100))
FLAG_ = pygame.image.load("flag_5188014.png")
FLAG = pygame.transform.scale(FLAG_, (100, 100))


def convert_index_to_cords(index_x, index_y):
    cords_y = FRAME_HEIGHT * index_y
    cords_x = FRAME_WIDTH * index_x
    return cords_x, cords_y
