def main_input():
    pass
def main_maze_input():
    pass
def question_input(): # TODO: input validation check
    question_list = []


    question = input(f"Hi teacher, please enter a question you would like to have in your quiz: ").lower()
    question_list.append(question)
    print('Please enter the answers you wish to have in your multiple choice question')

    for i in range(1,5):
        answer_option = input(f'please Enter answer number {i} for your multiple choice question: ')
        question_list.append(answer_option)
    correct_answer_num = int(input('please Enter the number of the correct answer: '))
    question_list.append(correct_answer_num - 1)
    return question_list
print(question_input())




