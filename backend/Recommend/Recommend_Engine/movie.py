import datetime
from collections import defaultdict
from backend.Recommend.yaml import callConfig
import numpy as np
import pandas as pd
from surprise import (SVD, Dataset, KNNBaseline, KNNBasic, Reader, SVDpp,
                      accuracy, dump)
from surprise.model_selection import cross_validate

import backend.Recommend.Recommend_Engine.pandasMongo as pdmo



def get_top_n(predictions, n=10):
    '''Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    '''

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


def precision_recall_at_k(predictions, k=10, threshold=3.5):
    '''Return precision and recall at k metrics for each user.'''

    # First map the predictions to each user.
    user_est_true = defaultdict(list)
    for uid, _, true_r, est, _ in predictions:
        user_est_true[uid].append((est, true_r))

    precisions = dict()
    recalls = dict()
    for uid, user_ratings in user_est_true.items():

        # Sort user ratings by estimated value
        user_ratings.sort(key=lambda x: x[0], reverse=True)

        # Number of relevant items
        n_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)

        # Number of recommended items in top k
        n_rec_k = sum((est >= threshold) for (est, _) in user_ratings[:k])

        # Number of relevant and recommended items in top k
        n_rel_and_rec_k = sum(((true_r >= threshold) and (est >= threshold))
                              for (est, true_r) in user_ratings[:k])

        # Precision@K: Proportion of recommended items that are relevant
        precisions[uid] = n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 1

        # Recall@K: Proportion of relevant items that are recommended
        recalls[uid] = n_rel_and_rec_k / n_rel if n_rel != 0 else 1

    return precisions, recalls


def getRecommendResult(modelId):
    if modelId == 0:
        Model = pdmo.read_mongo(callConfig('db'), 'scale_ratings')
    else:
        Model = pdmo.read_mongo(callConfig('db'), 'compare_ratings')
    # Command this to load faster/ Way more accurate
    movielensModel = pdmo.read_mongo(callConfig('db'), 'ratings')
    Model = Model.append(movielensModel)

    # reader used by surprise
    reader = Reader(rating_scale=(0.5, 5))

    data = Dataset.load_from_df(
        Model[["userId", "movieId", "rating"]], reader)
    print("Building trainset...")
    trainset = data.build_full_trainset()

    # First train an SVD algorithm on the movielens dataset.
    algo = SVD()
    print("Train algorithm...")
    algo.fit(trainset)

    # Run 5-fold cross-validation and print results
    if modelId == 0:
        modelName = "Scale"
    else:
        modelName = "Compare"
    print("Cross vaildate...")
    RMSE = cross_validate(algo, data, measures=[
                          'RMSE', 'MAE'], cv=5, verbose=True)

    print("Building testset...")
    testset = trainset.build_testset()
    testpredictions = algo.test(testset)
    print("Calculating testset accuracy...")
    accuRMSE = accuracy.rmse(testpredictions, verbose=True)
    # Than predict ratings for all pairs (u, i) that are NOT in the training set.
    # predictions = loaded_algo.test(trainset.build_anti_testset())

    return "Completed"
