import pygame
from consts import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK_CUBE_, WHITE_CUBE_, PLAYER_, QUESTION_MARK, FLAG, FONT_NAME, \
    SCROLL_, FONT_SIZE, COLOR_TEXT, LOCATION_TEXT
from consts import convert_index_to_cords

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# convert
BLACK_CUBE = BLACK_CUBE_.convert_alpha()
WHITE_CUBE = WHITE_CUBE_.convert_alpha()
PLAYER = PLAYER_.convert_alpha()
SCROLL = SCROLL_.convert_alpha()


def draw_black_cube(coordinates):
    display_surface.blit(BLACK_CUBE, coordinates)


def draw_white_cube(coordinates):
    display_surface.blit(WHITE_CUBE, coordinates)


def draw_grid(matrix):
    """
    draw the maze on the display_surface
    :param matrix: a 2d matrix of 1 for black , 0 for pass or 2 for question mark , 3 for flag
    """

    for index_x, row in enumerate(matrix):
        for index_y, call in enumerate(row):
            coordinates = convert_index_to_cords(index_x, index_y)

            if call == 1:
                draw_white_cube(coordinates)
            elif call == 0:
                draw_black_cube(coordinates)
            elif call == 2:
                draw_question_mark(coordinates)
            elif call == 3:
                draw_flag(coordinates)


def draw_question_mark(coordinates):
    """
    draw the question mark massage on display_surface
    """
    display_surface.blit(QUESTION_MARK, coordinates)


def draw_scroll():
    display_surface.blit(SCROLL, (WINDOW_WIDTH // 2 - 300, WINDOW_HEIGHT // 2 - 300))


def draw_massage(text):
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
    text_img = font.render(text, True, COLOR_TEXT)
    display_surface.blit(text_img, LOCATION_TEXT)


def draw_question_massage(message):
    """
    draw a question and the 3 answers passable on display_surface
    """
    draw_scroll()
    draw_massage(message["question"].key)
    draw_massage(message["question"][0])
    draw_massage(message["question"][1])
    draw_massage(message["question"][2])
    draw_massage(message["question"][3])


def draw_player(coordinates):
    """
    draw the player on the display_surface
    """
    display_surface.blit(PLAYER, coordinates)


def draw_flag(coordinates):
    display_surface.blit(FLAG, coordinates)


def draw_win():
    """
    draw a win massage on display_surface
    """
    pass
