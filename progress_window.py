# import progress_screen
import pygame

import progress_consts
import progress_screen

state = {"is_window_open": True,
         "soldier_location": (0, progress_consts.WINDOW_WIDTH / 2)}
import progress_consts

screen = pygame.display.set_mode((progress_consts.WINDOW_WIDTH, progress_consts.WINDOW_HEIGHT))

state = {"is_window_open": True}



def main():
    pygame.init()
    state["screen"] = progress_screen.screen_settings(progress_consts.SCREEN_SIZE)
    while state["is_window_open"]:
        user_events()

        progress_screen.draw_screen(state)











def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RETURN:
                state["enter_game"] = True


def solider_moving_right(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[1] += progress_consts.DISTANCE
    return tuple(soldier_position)


def draw_massage(massage, font_size, text_color, location):
    font = pygame.font.SysFont(progress_consts.FONT_NAME, font_size, bold=True)
    text_img = font.render(massage, True, text_color)
    text_width = text_img.get_width()
    text_height = text_img.get_height()
    location_x = location[0] - text_width / 2
    location_y = location[1] - text_height / 2
    screen.blit(text_img, (location_x, location_y))


def pop_up_window(solider_position):
    if solider_position[1] == progress_consts.DISTANCE:
        draw_massage(progress_consts.STUDY_INFO[0], progress_consts.POP_WINDOW_FONT_SIZE, "black",
                     progress_consts.POP_WINDOW_FONT_LOCATION)
