# import consts
import consts
# import screen
import pygame

import database
import maze_player
import screen_maze


def create_maze_grid():
    # 1 = wall 0 = path 2 = question 3 = flag
    grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1],
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
    return grid


maze_grid = create_maze_grid()

for x in create_maze_grid():
    print(x)

state = {"player_location": [2, 2],
         "game_running": True,
         "is_winning": False,
         "is_losing": False}


def maze_main():
    pygame.init()
    user_events()
    while state["game_running"]:
        user_events()

        screen_maze.draw_grid(maze_grid)
        screen_maze.draw_player(consts.convert_index_to_cords(state["player_location"][0], state["player_location"][1]))
        pygame.display.update()

        if state["player_location"] == [12, 12]:
            state["game_running"] = False
        if maze_grid[state["player_location"][0]][state["player_location"][1] - 1] == 2:
            screen_maze.draw_question_massage(database.retrieve_data())
            maze_grid[state["player_location"][0]][state["player_location"][1] - 1] = 0


def user_events():
    pygame.init()
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and maze_grid[state["player_location"][0]][
                state["player_location"][1] - 1] == 0 or event.key == pygame.K_UP and \
                maze_grid[state["player_location"][0]][
                    state["player_location"][1] - 1] == 2 or event.key == pygame.K_UP and \
                maze_grid[state["player_location"][0]][
                    state["player_location"][1] - 1] == 3:
                state["player_location"][1] -= 1

            if event.key == pygame.K_DOWN and maze_grid[state["player_location"][0]][
                state["player_location"][1] + 1] == 0 or event.key == pygame.K_DOWN and \
                maze_grid[state["player_location"][0]][
                    state["player_location"][1] + 1] == 2 or event.key == pygame.K_DOWN and \
                maze_grid[state["player_location"][0]][
                    state["player_location"][1] + 1] == 3:
                state["player_location"][1] += 1

            if event.key == pygame.K_RIGHT and maze_grid[state["player_location"][0] + 1][
                state["player_location"][1]] == 0 or event.key == pygame.K_RIGHT and \
                maze_grid[state["player_location"][0] + 1][
                    state["player_location"][1]] == 2 or event.key == pygame.K_RIGHT and \
                maze_grid[state["player_location"][0] + 1][
                    state["player_location"][1]] == 3:
                state["player_location"][0] += 1

            if event.key == pygame.K_LEFT and maze_grid[state["player_location"][0] - 1][
                state["player_location"][1]] == 0 or event.key == pygame.K_LEFT and \
                maze_grid[state["player_location"][0] - 1][
                    state["player_location"][1]] == 2 or event.key == pygame.K_LEFT and \
                maze_grid[state["player_location"][0] - 1][
                    state["player_location"][1]] == 3:
                state["player_location"][0] -= 1


user_events()
# maze_main()
