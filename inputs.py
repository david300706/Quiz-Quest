import consts
import database


def main_input():
    print("welcome to the Quiz Quest!\n"
          "we are gonna have so much fun!")
    # TODO: print explanation on each game

    games = []
    add_game = True
    while add_game:
        new_game = input(f"enter '{consts.MAZE}' to add maze game, '{consts.FLAG_GAME}' to add flag game,  : ")
        while new_game not in consts.GAMES:
            print("invalid input. try again:")

            new_game = input(f"enter '{consts.MAZE}' to add maze game', {consts.FLAG_GAME}' to add flag game,  : ")

        games.append(new_game)

        is_stop = input(f"enough mini games? enter '{consts.STOP_INPUT}' to stop, "
                        "\npress enter to enter more games: ")
        if is_stop == consts.STOP_INPUT:
            add_game = False

    for i in range(len(games)):

        if games[i] == consts.MAZE:
            study = []
            games_data = []
            files = []
            data_ = {}
            data, study_data = main_maze_input()
            data_[list(data.keys())[0]] = list(data.values())[0]
            games_data.append(data)
            study.append(study_data)
            database.new_csv(data_, f"Maze{i}.csv")
            files.append(f"Maze{i}.csv")

        # elif##3
        #     data, study_data = main_maze_input()
        #     data_[list(data.keys())[0]] = list(data.values())[0]
        #     games_data.append(data)
        #     study.append(study_data)
        #     database.new_csv(data_, f"Maze{i}.csv")
        #     files.append(f"Maze{i}.csv")
    return games, games_data, study, files


def main_maze_input():
    study_data = input("enter all info on the maze's subject: ")
    data = {}
    add_question = True
    while add_question:
        new_q = question_input()
        data[new_q[0]] = new_q[1:]
        more = input(f"enough questions? enter '{consts.STOP_INPUT}' to stop, "
                     "\npress enter to enter more questions: ")
        if more == consts.STOP_INPUT:
            add_question = False
    return data, study_data


def question_input():
    question_list = []
    question = input(f" please enter a question you would like to have in your quiz: ").lower()
    question_list.append(question)
    print('Please enter the answers you wish to have in your multiple choice question')

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
