import pandas as pd

questions = {"question1 text": ["option1", "option2", "option3", "option4", "2"],
             "question2 text": ["option1", "option2", "option3", "option4", "2"]}


def new_csv(data):
    df = pd.DataFrame(questions)
    df.to_csv("MazeGameData.csv")


def retrieve_data():
    df = pd.read_csv("MazeGameData.csv")
    df.pop("Unnamed: 0")
    df = df.to_dict()
    data = {}
    for key in df.keys():
        data[key] = list(df.get(key).values())
    return data


new_csv(questions)
print(retrieve_data())


