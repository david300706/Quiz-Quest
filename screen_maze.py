import pygame
from consts import WINDOW_WIDTH, WINDOW_HEIGHT
from maze_main import convert_index_to_cords

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_black_cube(coordinates):
    pass


def draw_white_cube(coordinates):
    pass


def draw_grid(matrix):
    """
    draw the maze on the display_surface
    :param matrix: a 2d matrix of 1 for black , 0 for pass or 2 for question mark , 3 for flag
    """

    for index_x, row in enumerate(matrix):
        for index_y, call in row:
            coordinates = convert_index_to_cords(index_x, index_y)

            if call == 1:
                draw_black_cube(coordinates)
            elif call == 0:
                draw_white_cube(coordinates)
            elif call == 2:
                draw_question_mark(coordinates)
            elif call == 3:
                draw_flag()


def draw_question_mark(coordinates):
    """
    draw the question mark massage on display_surface
    """
    pass


def draw_massage():
    """
    draw a question and the 3 answers passable on display_surface
    """
    pass


def draw_player(coordinates):
    """
    draw the player on the display_surface
    """
    pass


def draw_flag():
    pass


def draw_win():
    """
    draw a win massage on display_surface
    """
    pass
