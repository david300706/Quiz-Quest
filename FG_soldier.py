import FG_gamefield
import FG_consts
import FG_screen


def get_soldier_body(location):
    body_cords2 = []
    for i in range(location[1], location[1] + FG_consts.SOLDIER_HEIGHT):
        for j in range(location[0], location[0] + FG_consts.SOLDIER_WIDTH):
            body_cords2.append((j, i))
    return body_cords2


def soldier_feet_cords(soldier):
    soldier_feet = [[0, 0], [0, 0]]
    soldier_feet[0][1] = soldier[1] + FG_consts.SOLDIER_HEIGHT - 1
    soldier_feet[0][0] = soldier[0]
    soldier_feet[1][0] = soldier[0] + 1
    soldier_feet[1][1] = soldier[1] + FG_consts.SOLDIER_HEIGHT - 1
    return soldier_feet


def is_eliminated(state):
    legs = soldier_feet_cords(state["soldier_location"])
    for feet in legs:
        if state["game_field"][feet[1]][feet[0]] == "mine":
            return True
    return False


def is_winning(state):
    x = soldier_feet_cords(state["soldier_location"])
    for feet in x:
        if feet[0] >= FG_consts.GRID_WIDTH - FG_consts.FLAG_WIDTH and \
                feet[1] >= FG_consts.GRID_HEIGHT - FG_consts.FLAG_HEIGHT:
            return True
    return False
