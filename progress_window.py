# import progress_screen
import textwrap

import pygame
import time

import FG_main
import consts
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
            state["soldier_location"] = (round(state["soldier_location"][0] + 0.6), state["soldier_location"][1])
            # state["soldier_location"][1] = moving(state)
            progress_screen.draw_screen(state)
            time.sleep(0.005)

        if state["soldier_location"][0] == state["next_stop"]:
            progress_screen.draw_tk(progress_consts.STUDY_INFO[state["current_game"]])
            if progress_consts.GAMES[state["current_game"]] == consts.MAZE:
                maze_main.maze_main(database.retrieve_data(progress_consts.FILES[state["current_game"]]))
            elif progress_consts.GAMES[state["current_game"]] == consts.FLAG_GAME:
                FG_main.main(database.retrieve_data(progress_consts.FILES[state["current_game"]]))

            state["pop_up_open"] = False
            state["next_stop"] += int(progress_consts.DISTANCE)
            state["current_game"] += 1

        if state["soldier_location"][0] > progress_consts.WINDOW_WIDTH - 10:
            state["is_window_open"] = False


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




main()




