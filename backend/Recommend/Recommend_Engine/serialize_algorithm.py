import os

import pandas as pd
from surprise import SVD, Dataset, Reader, dump
import pandasMongo as pdmo
# Model = pd.read_csv("./data/ml-latest-small/ratings.csv", low_memory=False)
Model = pdmo.read_mongo('movielens', 'ratings')
# reader used by surprise
reader = Reader(rating_scale=(0.5, 5))

# train an SVD algorithm on the dataset.
data = Dataset.load_from_df(Model[["userId", "movieId", "rating"]], reader)
trainset = data.build_full_trainset()

algo = SVD()
algo.fit(trainset)

# Compute predictions of ratings for all pairs (u, i) that are NOT in the training set.
predictions = algo.test(trainset.build_anti_testset())

# Dump algorithm and reload it.
file_name = ('./data/ml-latest-small/ml-latest-small_testset')
dump.dump(file_name, algo=algo)
_, loaded_algo = dump.load(file_name)

# We now ensure that the algo is still the same by checking the predictions.
predictions_loaded_algo = loaded_algo.test(trainset.build_anti_testset())
assert predictions == predictions_loaded_algo
print('Predictions are the same')
