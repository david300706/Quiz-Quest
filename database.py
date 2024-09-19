import pandas as pd

questions = {"question1 text": ["option1", "option2", "option3", "option4", "2"],
             "question2 text": ["option1", "option2", "option3", "option4", "2"]}


def new_maze_csv(data, name):
    df = pd.DataFrame(data)
    df.to_csv(name)


def new_flag_csv(data, name):
    df = pd.DataFrame(data)
    df.to_csv(name)


def retrieve_data(name):
    df = pd.read_csv(name)
    df.pop("Unnamed: 0")
    df = df.to_dict()
    data = {}
    for key in df.keys():
        data[key] = list(df.get(key).values())
    return data


# new_csv(questions)
# print(retrieve_data())


