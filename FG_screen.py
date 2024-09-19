import time
import scroll
import pygame
import FG_consts
import consts
from database import questions
from screen_maze import calculate_centered_positions, draw_massage, SCROLL


def screen():
    screen = pygame.display.set_mode(
        (FG_consts.SCREEN_WIDTH, FG_consts.SCREEN_HEIGHT))
    return screen


def draw_message(message, font_size, color, location, screen):
    font = pygame.font.SysFont(FG_consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_start_massage(screen):
    screen.fill(FG_consts.BACKGROUND_COLOR)
    draw_message(FG_consts.START_MESSAGE, FG_consts.START_FONT_SIZE,
                 FG_consts.START_COLOR, FG_consts.START_LOCATION, screen)


def draw_soldier(location, screen):
    soldier = FG_consts.SOLDIER_IMAGE.get_rect(
        topleft=(location[0] * FG_consts.FRAME_WIDTH, location[1] * FG_consts.FRAME_HEIGHT))
    screen.blit(FG_consts.SOLDIER_IMAGE, soldier)


def draw_night_soldier(location, screen):
    soldier = FG_consts.SOLDIER_NIGHT_IMAGE.get_rect(
        topleft=(location[0] * FG_consts.FRAME_WIDTH, location[1] * FG_consts.FRAME_HEIGHT))
    screen.blit(FG_consts.SOLDIER_NIGHT_IMAGE, soldier)


def draw_bushes(bushes, screen):
    for bush in bushes:
        bush_img = FG_consts.GRASS_IMAGE.get_rect(topleft=tuple(bush))
        screen.blit(FG_consts.GRASS_IMAGE, bush_img)


def draw_flag(screen):
    flag = FG_consts.FLAG_IMAGE.get_rect(topleft=(FG_consts.SCREEN_WIDTH - FG_consts.FLAG_WIDTH * FG_consts.FRAME_WIDTH,
                                                  FG_consts.SCREEN_HEIGHT - FG_consts.FLAG_HEIGHT * FG_consts.FRAME_HEIGHT))
    screen.blit(FG_consts.FLAG_IMAGE, flag)


def print_lost(screen):
    draw_message(FG_consts.LOST_MASSAGE, FG_consts.START_FONT_SIZE,
                 FG_consts.START_COLOR, FG_consts.LOST_LOCATION, screen)
    pygame.display.flip()
    time.sleep(3)


def print_won(screen):
    draw_message(FG_consts.WON_MASSAGE, FG_consts.START_FONT_SIZE,
                 FG_consts.START_COLOR, FG_consts.START_LOCATION)
    pygame.display.flip()
    time.sleep(3)


def draw_game(game_state):
    game_state["screen"].fill(FG_consts.BACKGROUND_COLOR)
    draw_bushes(game_state["bushes"], game_state["screen"])
    draw_soldier(game_state["soldier_location"], game_state["screen"])
    draw_flag(game_state["screen"])
    draw_guard(game_state["guard_location"], game_state["screen"])
    # draw_teleports(game_state["teleports"])
    pygame.display.flip()


def draw_grid(screen):
    for x in range(0, FG_consts.SCREEN_WIDTH, FG_consts.FRAME_WIDTH):
        for y in range(0, FG_consts.SCREEN_HEIGHT, FG_consts.FRAME_HEIGHT):
            rect = pygame.Rect(x, y, FG_consts.FRAME_WIDTH, FG_consts.FRAME_HEIGHT)
            pygame.draw.rect(screen, FG_consts.START_COLOR, rect, 1)


def draw_mines(mines, screen):
    for mine in mines:
        mine_img = FG_consts.MINE_IMAGE.get_rect(
            topleft=((mine[0] - 1) * FG_consts.FRAME_WIDTH, mine[1] * FG_consts.FRAME_HEIGHT))
        screen.blit(FG_consts.MINE_IMAGE, mine_img)


def show_mines(game_state):
    game_state["screen"].fill(FG_consts.NIGHT_COLOR)
    draw_grid(game_state["screen"])
    draw_mines(game_state["mines"], game_state["screen"])
    draw_night_soldier(game_state["soldier_location"], game_state["screen"])
    # draw_teleports(game_state["teleports"])
    pygame.display.flip()


def draw_guard(location, screen):
    guard = FG_consts.GUARD_IMAGE.get_rect(
        topleft=(location[0] * FG_consts.FRAME_WIDTH, location[1] * FG_consts.FRAME_HEIGHT))
    screen.blit(FG_consts.GUARD_IMAGE, guard)


# def draw_teleports(teleports):
#     for tp in teleports:
#         tp_img = FG_consts.TP_IMAGE.get_rect(
#             topleft=((tp[0] - 1) * FG_consts.FRAME_WIDTH, tp[1] * FG_consts.FRAME_HEIGHT))
#         screen.blit(FG_consts.TP_IMAGE, tp_img)


def draw_explo(location, screen):
    explo = FG_consts.EXPLOSION_IMAGE.get_rect(
        topleft=(location[0] * FG_consts.FRAME_WIDTH, location[1] * FG_consts.FRAME_HEIGHT))
    screen.blit(FG_consts.EXPLOSION_IMAGE, explo)


def draw_injury(location, screen):
    injury = FG_consts.INJURY_IMAGE.get_rect(
        topleft=(location[0] * FG_consts.FRAME_WIDTH, location[1] * FG_consts.FRAME_HEIGHT))
    screen.blit(FG_consts.INJURY_IMAGE, injury)


def draw_question_massage(the_number_of_question, questions, screen):
    """
    the function only need the number of the desirable question and answer to draw
    and shy will
    draw a question and the 3 answers passable on display_surface
    the_number_of_question: an int representing the index of the question
    """

    scroll_rect = SCROLL.get_rect(center=(consts.WINDOW_WIDTH / 2, consts.WINDOW_HEIGHT / 2))

    scroll.draw_scroll(SCROLL, screen, scroll_rect)
    questions_to_draw = list(questions.keys())
    coordinates_of_text = calculate_centered_positions()
    draw_massage(questions_to_draw[the_number_of_question], coordinates_of_text["question"])
    draw_massage(questions[questions_to_draw[the_number_of_question]][0], coordinates_of_text["answer_0"])
    draw_massage(questions[questions_to_draw[the_number_of_question]][1], coordinates_of_text["answer_1"])
    draw_massage(questions[questions_to_draw[the_number_of_question]][2], coordinates_of_text["answer_2"])
    draw_massage(questions[questions_to_draw[the_number_of_question]][3], coordinates_of_text["answer_3"])
