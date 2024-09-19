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
    print("ggggggggggggggggg")
    print(df)

    if name[:4] == "Maze":
        data = {}
        for key in df.keys():
            answers = list(df.get(key).values())
            answers[4] = int(answers[4])
            answers[4] += 1
            answers[4] = str(answers[4])
            data[key] = answers

        print(data)
        return data

    elif name[:4] == "Flag":
        print(df["facts"])
        return df["facts"]



# new_csv(questions)
# print(retrieve_data())


