import FG_consts
import time

import FG_screen
import FG_soldier


def guard_movement(location, direction):
    if location[0] == 47 or location[0] == 0:
        direction = not direction
    if direction:
        location[0] += 1
        time.sleep(0.01)
    else:
        location[0] -= 1
        time.sleep(0.01)
    return location, direction


def guard_eat(state):
    x = FG_soldier.get_soldier_body(state["soldier_location"])
    y = get_guard_body(state["guard_location"])
    for i in range(6):
        for j in range(6):
            if x[i] == y[j]:
                FG_screen.draw_injury(state["soldier_location"], state["screen"])
                return True
    return False


def get_guard_body(location):
    body_cords1 = []
    for i in range(location[1], location[1] + FG_consts.GUARD_HEIGHT):
        for j in range(location[0], location[0] + FG_consts.GUARD_WIDTH):
            body_cords1.append((j, i))
    return body_cords1
