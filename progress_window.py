# import progress_screen
import pygame
import time

import database
import progress_consts
import progress_screen
import maze_main

state = {"is_window_open": True,
         "soldier_location": (0, int(progress_consts.WINDOW_WIDTH / 2)),
         "current_game": 0,
         "pop_up_open": False,
         "next_stop": int(progress_consts.DISTANCE)}


# state["current_line"] = get_line()


def main():
    pygame.init()
    user_events()
    state["screen"] = progress_screen.screen_settings(progress_consts.SCREEN_SIZE)
    while state["is_window_open"]:
        user_events()

        if not state["pop_up_open"]:
            state["soldier_location"] = (round(state["soldier_location"][0] + 1), state["soldier_location"][1])
            # state["soldier_location"][1] = moving(state)
            progress_screen.draw_screen(state)
            time.sleep(0.005)

        if state["soldier_location"][0] == state["next_stop"]:
            progress_screen.draw_tk(progress_consts.STUDY_INFO[state["current_game"]])
            # progress_screen.draw_massage(progress_consts.STUDY_INFO[state["current_game"]],
            #                              progress_consts.POP_WINDOW_FONT_SIZE, (0, 0, 0),
            #                              state["soldier_location"], state["screen"])
            ##database.retrieve_data(progress_consts.FILES[state["current_game"]])

            maze_main.maze_main()
            state["pop_up_open"] = True


def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and state["pop_up_open"]:
                # maze_main.maze_main(database.retrieve_data(progress_consts.FILES[state["current_game"]]))
                state["enter_game"] = True


def solider_moving_right(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[0] += progress_consts.DISTANCE
    return tuple(soldier_position)


# state["soldier_location"] = solider_moving_right(state["soldier_location"])
# def solider_moving_right(soldier_position):
#     soldier_position = list(soldier_position)
#     soldier_position[1] += progress_consts.DISTANCE
#     return tuple(soldier_position)
#
#
# def draw_massage(massage, font_size, text_color, location):
#     font = pygame.font.SysFont(progress_consts.FONT_NAME, font_size, bold=True)
#     text_img = font.render(massage, True, text_color)
#     text_width = text_img.get_width()
#     text_height = text_img.get_height()
#     location_x = location[0] - text_width / 2
#     location_y = location[1] - text_height / 2
#     screen.blit(text_img, (location_x, location_y))
#
#
# def pop_up_window(solider_position):
#     if solider_position[1] == progress_consts.DISTANCE:
#         draw_massage(progress_consts.STUDY_INFO[0], progress_consts.POP_WINDOW_FONT_SIZE, "black",
#                      progress_consts.POP_WINDOW_FONT_LOCATION)


def moving(state):
    print(get_line(state["soldier_location"], progress_consts.STOPS[state["next_stop"]]))
    return get_line(state["soldier_location"], progress_consts.STOPS[state["next_stop"]])


def get_line(current, next):
    cx = current[0]
    cy = current[1]
    nx = next[0]
    ny = next[1]
    M = (cy - ny) / (cx - nx)
    b = ny - M * nx
    y = M * cx + 1 + b
    return y


main()

main()
