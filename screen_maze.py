import pygame
from consts import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK_CUBE_, WHITE_CUBE_, PLAYER_, QUESTION_MARK, FLAG, FONT_NAME, \
    SCROLL_, FONT_SIZE, COLOR_TEXT, LOCATION_TEXT, GOLD_COLOR
from consts import convert_index_to_cords
from scroll import draw_scroll

# general setup


# convert

# BLACK_CUBE = BLACK_CUBE_.convert_alpha()
# WHITE_CUBE = WHITE_CUBE_.convert_alpha()
# PLAYER = PLAYER_.convert_alpha()
# SCROLL = SCROLL_.convert_alpha()

BLACK_CUBE = BLACK_CUBE_
WHITE_CUBE = WHITE_CUBE_
PLAYER = PLAYER_
SCROLL = SCROLL_


def draw_black_cube(coordinates, display_surface):
    display_surface.blit(BLACK_CUBE, coordinates)


def draw_white_cube(coordinates, display_surface):
    display_surface.blit(WHITE_CUBE, coordinates)


def draw_grid(matrix, display_surface):
    """
    draw the maze on the display_surface
    :param matrix: a 2d matrix of 1 for black , 0 for pass or 2 for question mark , 3 for flag
    """

    for index_x, row in enumerate(matrix):
        for index_y, call in enumerate(row):
            coordinates = convert_index_to_cords(index_x, index_y)

            if call == 1:
                draw_white_cube(coordinates, display_surface)
            elif call == 0:
                draw_black_cube(coordinates, display_surface)
            elif call == 2:
                draw_question_mark(coordinates, display_surface)
            elif call == 3:
                draw_flag(coordinates, display_surface)


def draw_question_mark(coordinates, display_surface):
    """
    draw the question mark massage on display_surface
    """
    display_surface.blit(QUESTION_MARK, coordinates)


def get_center_position(text_surface):
    """
    :param text_surface: the text surface objict
    :return: the tuple x and y coordinates
    """
    # get the dimensions of the text surface
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()

    # calculate the position to center the text manually
    x_pos = (WINDOW_WIDTH - text_width) // 2
    y_pos = (WINDOW_HEIGHT - text_height) // 2

    return x_pos, y_pos


def calculate_centered_positions():
    """
    Calculates the coordinates for placing 1 question and 4 answers centered vertically.
    :return: A dictionary with the calculated coordinates for the question and the 4 answers
    """
    # Define vertical padding between the question and the answers
    vertical_padding = 20
    question_offset = 40

    move_up_offset = -100
    move_left_offset = - 180
    question_y = (WINDOW_HEIGHT // 2) - FONT_SIZE - question_offset
    # Calculate the y position of each answer, spaced
    answer_0_y = (WINDOW_HEIGHT // 2)
    answer_1_y = answer_0_y + FONT_SIZE + vertical_padding
    answer_2_y = answer_1_y + FONT_SIZE + vertical_padding
    answer_3_y = answer_2_y + FONT_SIZE + vertical_padding

    # 130 IS FOR MOVING IT LEFT as much as needed
    question_x = (WINDOW_WIDTH // 2) + move_left_offset
    answer_x = question_x
    return {
        "question": (question_x, question_y + move_up_offset),
        "answer_0": (answer_x, answer_0_y + move_up_offset),
        "answer_1": (answer_x, answer_1_y + move_up_offset),
        "answer_2": (answer_x, answer_2_y + move_up_offset),
        "answer_3": (answer_x, answer_3_y + move_up_offset),
    }


def draw_massage(text, position, display_surface):
    """
    :param text: the string to draw on screen
    :param position: x and y coordinates
    """
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
    text_surface = font.render(text, True, COLOR_TEXT)
    display_surface.blit(text_surface, position)


def draw_question_massage(the_number_of_question, questions, display_surface):
    """
    the function only need the number of the desirable question and answer to draw
    and shy will
    draw a question and the 3 answers passable on display_surface
    the_number_of_question: an int representing the index of the question
    """

    scroll_rect = SCROLL.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    draw_scroll(SCROLL, display_surface, scroll_rect)
    questions_to_draw = list(questions.keys())
    coordinates_of_text = calculate_centered_positions()

    draw_massage(questions_to_draw[the_number_of_question], coordinates_of_text["question"], display_surface)
    draw_massage(questions[questions_to_draw[the_number_of_question]][0], coordinates_of_text["answer_0"],
                 display_surface)
    draw_massage(questions[questions_to_draw[the_number_of_question]][1], coordinates_of_text["answer_1"],
                 display_surface)
    draw_massage(questions[questions_to_draw[the_number_of_question]][2], coordinates_of_text["answer_2"],
                 display_surface)
    draw_massage(questions[questions_to_draw[the_number_of_question]][3], coordinates_of_text["answer_3"],
                 display_surface)


def draw_player(coordinates, display_surface):
    """
    draw the player on the display_surface
    """
    display_surface.blit(PLAYER, coordinates)


def draw_flag(coordinates, display_surface):
    display_surface.blit(FLAG, coordinates)


def draw_win(display_surface):
    """
    Draw a win message on display_surface
    """
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE * 2)
    # Create the text surface for the win message
    win_text = font.render("You Win!", True, GOLD_COLOR)
    # Get the rectangle of the text to center it
    win_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    pygame.draw.rect(display_surface, (5, 5, 5), win_rect.inflate(20, 20))
    display_surface.blit(win_text, win_rect)
