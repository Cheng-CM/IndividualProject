import pandas as pd


def UpdateModel(path):
    Model = pd.read_csv("./data/ml-latest-small/ratings.csv", low_memory=False)
    try:
        newFile = pd.read_csv(path, low_memory=False)
        Model = pd.concat(newFile)
    except Exception as e:
        print(e)
    Model.to_csv("./data/custom/ratings.csv", header=None)
