import pygame
from consts import WINDOW_WIDTH, WINDOW_HEIGHT

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
    :param matrix: a 2d matrix of 1 for black , 0 for pass or 2 for question mark
    """
    for row in matrix:
        for call in row:
            if call == 1:
                pass
            elif call == 0:
                pass
            elif call == 2:
                pass


def question_mark(coordinates):
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


def draw_win():
    """
    draw a win massage on display_surface
    """
    pass
