import consts


def main_input():
    print("welcome to the Quiz Quest!\n"
          "we are gonna have so much fun!")
    # TODO: print explanation on each game

    games = []
    add_game = True
    while add_game:
        new_game = input(f"enter '{consts.MAZE}' to add maze game: ")
        while new_game not in consts.GAMES:
            print("invalid input. try again:")
            new_game = input(f"enter '{consts.MAZE}' to add maze game: ")
        games.append(new_game)

        is_stop = input(f"enough mini games? enter '{consts.STOP_INPUT}' to stop, "
                        "\npress enter to enter more games: ")
        if is_stop == consts.STOP_INPUT:
            add_game = False

    games_data = []
    for game in games:
        if game == consts.MAZE:
            games_data.append(main_maze_input())

    return games, games_data







def main_maze_input():
    data = {}
    add_question = True
    while add_question:
        new_q = question_input()
        data[new_q[0]] = new_q[1:]
        more = input(f"enough questions? enter '{consts.STOP_INPUT}' to stop, "
                     "\npress enter to enter more questions: ")
        if more == consts.STOP_INPUT:
            add_question = False
    return data


def question_input():
    count = 0
    done = False
    while not done:
        count += 1
        question = input(f"Hi teacher, please enter question number {count} - If you're done, enter done:").lower()
