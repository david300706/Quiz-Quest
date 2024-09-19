import consts
import database


def main_input():
    print("welcome to the Quiz Quest!\n"
          "we are gonna have so much fun!")
    # TODO: print explanation on each game
    print('Here are explanations of the games: ')
    print("MAZE GAME: The MAZE GAME is a game that combines fun with a very interesting quiz on a topic of your choice.")
    print('FLAG GAME: the FLAG GAME is a tactical game with intresting strategy: you have to avoid the mines! and reach the flag to win.')


    games = []
    add_game = True
    while add_game:
        new_game = input(f"enter '{consts.MAZE}' to add maze game, '{consts.FLAG_GAME}' to add flag game,  : ")
        while new_game not in consts.GAMES:
            print("invalid input. try again:")

            new_game = input(f"enter '{consts.MAZE}' to add maze game', {consts.FLAG_GAME}' to add flag game,  : ")

        games.append(new_game)
        print()
        is_stop = input(f"enough mini games? enter '{consts.STOP_INPUT}' to stop, "
                        "\npress enter to enter more games: ")
        if is_stop == consts.STOP_INPUT:
            add_game = False

    study = []
    games_data = []
    files = []
    for i in range(len(games)):

        data_ = {}
        if games[i] == consts.MAZE:
            data, study_data = main_maze_input()
            for j in list(data.keys()):
                data_[j] = data.get(j)
            games_data.append(data)
            study.append(study_data)
            database.new_maze_csv(data_, f"Maze{i + 1}.csv")
            files.append(f"Maze{i + 1}.csv")

        elif games[i] == consts.FLAG_GAME:
            facts, desc = facts_input()
            study.append(desc)

            data_["facts"] = facts
            database.new_flag_csv(data_, f"Flag{i + 1}.csv")
            files.append(f"Flag{i + 1}.csv")

    return games, games_data, study, files


def main_maze_input():
    study_data = input("enter all info on the maze's subject: ")
    data = {}
    add_question = True
    while add_question:
        new_q = question_input()
        data[new_q[0]] = new_q[1:]
        print()
        more = input(f"enough questions? enter '{consts.STOP_INPUT}' to stop, "
                     "\npress enter to enter more questions: ")
        if more == consts.STOP_INPUT:
            add_question = False
    return data, study_data


def question_input():
    question_list = []
    question = input(f" please enter a question you would like to have in your quiz: ").lower()
    question_list.append(question)
    print()
    print('Please enter the answers you wish to have in your multiple choice question')
    print()
    for i in range(1, 5):
        answer_option = input(f'please Enter answer number {i} for your multiple choice question ')

        question_list.append(answer_option)
    input_ = False
    while not input_:
        correct_answer_num = int(input('please Enter the number of the correct answer: '))
        if correct_answer_num < 5 and correct_answer_num > 0:
            input_ = True
        else:
            print('invalid number, the correct answer has to be in range ')
        question_list.append(correct_answer_num - 1)
    return question_list


# main_input()
def facts_input():
    print()
    descr = input("enter initial info to study: ")
    print()
    done = False
    facts_list = []
    while not done:
        fact = input(
            "please enter a fact you would like to have in your FLAG GAME if your'e done enter 'done': ").lower()
        if fact == 'done':
            done = True
        else:
            facts_list.append(fact)
    return facts_list, descr
