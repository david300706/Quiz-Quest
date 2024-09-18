# import consts
import consts
# import screen
import pygame
import screen_maze


def create_maze_grid():
    '''
    0 = path
    1 = block
    2 = question
    :return:
    '''
    maze_grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                 [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 2, 1, 1, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                 [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                 [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                 [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 2, 1, 1, 1],
                 [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 3, 0, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    return maze_grid


maze_grid = create_maze_grid()


def convert_index_to_cords(index_x, index_y):
    cords_y = consts.FRAME_HEIGHT * index_y
    cords_x = consts.FRAME_WIDTH * index_x
    return cords_x, cords_y


for x in create_maze_grid():
    print(x)

state = {"player_location": [2, 2],
         "game_running": True}


def maze_main():
    pygame.init()
    user_events()
    while state["game_running"]:
        user_events()


def user_events():
    pygame.init()
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and maze_grid[state["player_location"][0]][
                state["player_location"][1] - 1] == 0 or event.key == pygame.K_UP and maze_grid[state["player_location"][0]][
                state["player_location"][1] - 1] == 2:
                state["player_location"][1] -= 1
                print(state["player_location"])

            if event.key == pygame.K_DOWN and maze_grid[state["player_location"][0]][
                state["player_location"][1] + 1] == 0 or event.key == pygame.K_DOWN and maze_grid[state["player_location"][0]][
                state["player_location"][1] + 1] == 2:
                state["player_location"][1] += 1
                print(state["player_location"])

            if event.key == pygame.K_RIGHT and maze_grid[state["player_location"][0] + 1][
                state["player_location"][1]] == 0 or event.key == pygame.K_RIGHT and maze_grid[state["player_location"][0] + 1][
                state["player_location"][1]] == 2:
                state["player_location"][0] += 1
                print(state["player_location"])

            if event.key == pygame.K_LEFT and maze_grid[state["player_location"][0] - 1][
                state["player_location"][1]] == 0 or event.key == pygame.K_LEFT and maze_grid[state["player_location"][0] - 1][
                state["player_location"][1]] == 2:
                state["player_location"][0] -= 1
                print(state["player_location"])


user_events()
maze_main()
