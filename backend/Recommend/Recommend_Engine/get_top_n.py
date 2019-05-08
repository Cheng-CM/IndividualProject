from collections import defaultdict

import pandas as pd
from surprise import SVD, Dataset, Reader, dump
from surprise.model_selection import cross_validate
import backend.Recommend.Recommend_Engine.pandasMongo as pdmo


Model = pdmo.read_mongo('movielens', 'ratings')

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

# Model = pd.read_csv("./data/ml-latest-small/ratings.csv", low_memory=False)

def getScaleRecommendResult():
    # Model = pd.read_csv("./data/ml-latest-small/ratings.csv", low_memory=False)
    scale_ratings = pdmo.read_mongo('movielens', 'scale_ratings')
    scale_ratings = scale_ratings.append(Model)
    # compare_ratings = pdmo.read_mongo('movielens', 'compare_ratings')

    # reader used by surprise
    reader = Reader(rating_scale=(0, 5))

    data = Dataset.load_from_df(scale_ratings[["userId", "movieId", "rating"]], reader)
    trainset = data.build_full_trainset()

    # First train an SVD algorithm on the movielens dataset.
    algo = SVD()
    algo.fit(trainset)

    # # Load dumped algorithm.
    # file_name = ('./data/ml-latest-small/ml-latest-small_testset')
    # _, loaded_algo = dump.load(file_name)


    # Run 5-fold cross-validation and print results
    RMSE = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    print(RMSE)

    # Than predict ratings for all pairs (u, i) that are NOT in the training set.
    # predictions = loaded_algo.test(trainset.build_anti_testset())
    predictions = algo.test(trainset.build_anti_testset())


    top_n = get_top_n(predictions, n=10)

    # Print the recommended items for each user
    # for uid, user_ratings in top_n.items():
    #     print(uid, [iid for (iid, _) in user_ratings])
    return(top_n)


def getCompareRecommendResult():
    
    compare_ratings = pdmo.read_mongo('movielens', 'compare_ratings')
    compare_ratings = compare_ratings.append(Model)
    
    # reader used by surprise
    reader = Reader(rating_scale=(0.5, 5))

    data = Dataset.load_from_df(compare_ratings[["userId", "movieId", "rating"]], reader)
    trainset = data.build_full_trainset()

    # First train an SVD algorithm on the movielens dataset.
    algo = SVD()
    algo.fit(trainset)

    # Run 5-fold cross-validation and print results
    RMSE = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    print(RMSE)
    # Than predict ratings for all pairs (u, i) that are NOT in the training set.
    predictions = algo.test(trainset.build_anti_testset())

    top_n = get_top_n(predictions, n=10)

    return(top_n)
