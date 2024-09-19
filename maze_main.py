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


def maze_main(questions):
    """
    :param questions:  a dict of questions and answers
    """
    # initially the question to draw is in index 0
    the_number_of_question = 0
    pygame.init()
    user_events()
    been_there_loc = "X"
    while state["game_running"]:
        user_events()

        screen_maze.draw_grid(maze_grid)
        screen_maze.draw_player(consts.convert_index_to_cords(state["player_location"][0], state["player_location"][1]))
        pygame.display.update()

        if state["player_location"] == [12, 12]:
            state["game_running"] = False

        if maze_grid[state["player_location"][0]][state["player_location"][1]] == 2 and \
                maze_grid[state["player_location"][0]][state["player_location"][1]] != been_there_loc:
            been_there_loc = maze_grid[state["player_location"][0]][state["player_location"][1]]
            screen_maze.draw_question_massage(the_number_of_question, questions)
            pygame.display.update()

            not_pressd_one_of_answers_key = True
            while not_pressd_one_of_answers_key:
                for event in pygame.event.get():
                    # checking if keydown event happened or not
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            print("1")
                            not_pressd_one_of_answers_key = False

                        elif event.key == pygame.K_2:
                            print("2")
                            not_pressd_one_of_answers_key = False

                        elif event.key == pygame.K_3:
                            print("3")
                            not_pressd_one_of_answers_key = False

                        elif event.key == pygame.K_4:
                            print("4")
                            not_pressd_one_of_answers_key = False

            # FOR TESTING IF THE SCROLL SHOW UP
            the_number_of_question += 1
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
maze_main(database.questions)
