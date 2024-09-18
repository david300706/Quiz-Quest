import pygame
from consts import WINDOW_WIDTH, WINDOW_HEIGHT

# general setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_black_cube():
    pass


def draw_white_cube():
    pass


def draw_grid(matrix):
    """
    draw the maze on the display_surface
    :param matrix: a 2d matrix of 1 for no pass , 0 for pass or 2 for question mark
    """
    pass


def question_mark():
    """

    :return:
    """
    pass


def draw_massage():
    pass


def draw_player():
    pass


def draw_win():
    pass
