# import progress_screen
import pygame
import time
import progress_consts
import progress_screen

state = {"is_window_open": True,
         "soldier_location": (0, int(progress_consts.WINDOW_WIDTH / 2)),
         "current_game": 0,
         "pop_up_open": False,
         "next_stop": int(progress_consts.DISTANCE)}


def main():
    pygame.init()
    state["screen"] = progress_screen.screen_settings(progress_consts.SCREEN_SIZE)
    while state["is_window_open"]:
        user_events()

        if not state["pop_up_open"]:
            state["soldier_location"] = (round(state["soldier_location"][0] + 1), state["soldier_location"][1])
            progress_screen.draw_screen(state)
            time.sleep(0.01)

        if state["soldier_location"][0] == state["next_stop"]:
            progress_screen.draw_massage(progress_consts.STUDY_INFO[state["current_game"]], progress_consts.POP_WINDOW_FONT_SIZE, (0, 0, 0),
                         state["soldier_location"], state["screen"])
            state["pop_up_open"] = True


def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                state["enter_game"] = True


def solider_moving_right(soldier_position):
    soldier_position = list(soldier_position)
    soldier_position[0] += progress_consts.DISTANCE
    return tuple(soldier_position)





def pop_up_window(solider_position):
    if solider_position[1] == progress_consts.DISTANCE:
        progress_screen.draw_massage(progress_consts.STUDY_INFO[0], progress_consts.POP_WINDOW_FONT_SIZE, "black",
                     progress_consts.POP_WINDOW_FONT_LOCATION)


# state["soldier_location"] = solider_moving_right(state["soldier_location"])
main()
