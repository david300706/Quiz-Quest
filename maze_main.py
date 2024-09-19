# import consts
import consts
# import screen
import pygame
import random

import database
import maze_player
import screen_maze


def add_qustions_to_grid(grid, questions):
    list_of_loc_to_add = []
    num_of_qustion_mark_to_add = len(list(questions.keys()))
    for i in range(num_of_qustion_mark_to_add):
        y = random.randint(3, consts.GRID_HEIGHT - 1)
        x = 1
        while grid[y][x] != 0:
            x = random.randint(1, consts.GRID_WIDTH - 1)
        list_of_loc_to_add.append([y, x])
    print(list_of_loc_to_add)
    return list_of_loc_to_add


def create_maze_grid(questions):
    # 1 = wall 0 = path 2 = question 3 = flag
    grid = random.choice(consts.mazes)
    list_of_loc = add_qustions_to_grid(grid, questions)
    for i in list_of_loc:
        grid[i[0]][i[1]] = 2
        print(grid)
    return grid


maze_grid = create_maze_grid(database.questions)

# for x in create_maze_grid():
#   print(x)

state = {"player_location": [1, 1],
         "game_running": True,
         "is_winning": False,
         "is_losing": False,
         "answer": None,
         "score": 0}


def inital_the_screen():
    pygame.init()
    display_surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    return display_surface


def maze_main(questions):
    """
    :param questions:  a dict of questions and answers
    """
    # initially the question to draw is in index 0
    list_of_kys = list(questions.keys())
    display_surface = inital_the_screen()
    the_number_of_question = 0
    pygame.init()
    user_events()
    been_thare_location = "X"
    while state["game_running"]:
        user_events()

        screen_maze.draw_grid(maze_grid, display_surface)
        screen_maze.draw_player(consts.convert_index_to_cords(state["player_location"][0], state["player_location"][1]),
                                display_surface)
        pygame.display.update()
        if the_number_of_question != len(list_of_kys):
            current_question = list_of_kys[the_number_of_question]
        if state["player_location"] == [13, 13]:
            state["game_running"] = False
        if maze_grid[state["player_location"][0]][state["player_location"][1]] == 2 and state[
            "player_location"] != been_thare_location:
            print("b", been_thare_location)
            been_thare_location = state["player_location"]
            screen_maze.draw_question_massage(current_question, questions, display_surface)

        if maze_grid[state["player_location"][0]][state["player_location"][1]] == 2 and \
            maze_grid[state["player_location"][0]][state["player_location"][1]] != been_thare_location:


            been_thare_location = maze_grid[state["player_location"][0]][state["player_location"][1]]
            screen_maze.draw_question_massage(current_question, questions, display_surface)

            pygame.display.update()

            not_pressd_one_of_answers_key = True
            while not_pressd_one_of_answers_key:
                for event in pygame.event.get():
                    # checking if keydown event happened or not
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if questions[current_question][4] == 1:
                                state["score"] += 1
                            not_pressd_one_of_answers_key = False

                        elif event.key == pygame.K_2:
                            if questions[current_question][4] == 2:
                                state["score"] += 1
                            not_pressd_one_of_answers_key = False

                        elif event.key == pygame.K_3:
                            if questions[current_question][4] == 3:
                                state["score"] += 1
                            not_pressd_one_of_answers_key = False

                        elif event.key == pygame.K_4:
                            if questions[current_question][4] == 4:
                                state["score"] += 1
                            not_pressd_one_of_answers_key = False
            screen_maze.draw_score(state["score"], display_surface)
            # FOR TESTING IF THE SCROLL SHOW UP
            if the_number_of_question <= len(list_of_kys):
                the_number_of_question += 1
            maze_grid[state["player_location"][0]][state["player_location"][1]] = 0


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
maze_main(database.questions)
