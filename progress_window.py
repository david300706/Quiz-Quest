# import progress_screen
import pygame.event

state = {"is_window_open": True}

def main():
    pygame.init()

    while state["is_window_open"]:











def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RETURN:
                state["enter_game"] = True


def movement():
    pass






