# import progress_screen
import pygame.event

import progress_consts
import progress_screen

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


def movement():
    pass
main()





