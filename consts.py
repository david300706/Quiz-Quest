import pygame.image

STOP_INPUT = "stop"

MAZE = "1"
FLAG_GAME = "2"
GAMES = [MAZE,FLAG_GAME]

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
# Grid size for maze:
GRID_HEIGHT = 15
GRID_WIDTH = 15
# Frame size for maze:
FRAME_HEIGHT = int(WINDOW_HEIGHT / GRID_HEIGHT)
FRAME_WIDTH = int(WINDOW_WIDTH / GRID_WIDTH)
MAZE_QUESTION_MAX_AMOUNT = 5

# maze assets
BLACK_CUBE__ = pygame.image.load("cube_b.png")
BLACK_CUBE_ = pygame.transform.scale(BLACK_CUBE__, (FRAME_HEIGHT, FRAME_WIDTH))

WHITE_CUBE__ = pygame.image.load("cube_w.png")
WHITE_CUBE_ = pygame.transform.scale(WHITE_CUBE__, (FRAME_HEIGHT, FRAME_WIDTH))

PLAYER__ = pygame.image.load("player.png")
PLAYER_ = pygame.transform.scale(PLAYER__, (FRAME_HEIGHT, FRAME_WIDTH))

SCROLL_ = pygame.image.load("scroll_good.png")
SCROLL_ = pygame.transform.scale(SCROLL_, (900,800 ))
#len(leangt_longest_row)
QUESTION_MARK_ = pygame.image.load("qustion_mark_rady_to_use.png")
QUESTION_MARK = pygame.transform.scale(QUESTION_MARK_, (FRAME_HEIGHT, FRAME_WIDTH))

FLAG_ = pygame.image.load("flag_3.png")
FLAG = pygame.transform.scale(FLAG_, (FRAME_HEIGHT, FRAME_WIDTH))

FONT_NAME = "Calibri"
FONT_SIZE = 40
COLOR_TEXT = (0, 0, 0)
LOCATION_TEXT = 200
GOLD_COLOR = (255, 215, 0)


def convert_index_to_cords(index_x, index_y):
    cords_y = FRAME_HEIGHT * index_y
    cords_x = FRAME_WIDTH * index_x
    return cords_x, cords_y
