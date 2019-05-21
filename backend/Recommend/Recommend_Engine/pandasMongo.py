import pandas as pd
from pymongo import MongoClient
from bson.json_util import dumps


def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (
            username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db]


def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port,
                        username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df


def insert_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port,
                        username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    db[collection].insert_one(query)

def read_mongo_as_JSON(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
        # Connect to MongoDB
    db = _connect_mongo(host=host, port=port,
                        username=username, password=password, db=db)
    # Make a query to the specific DB and Collection
    data = dumps(db[collection].find(query))
    return data

def search(db, collection, string, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port,
                        username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    db[collection].create_index([('title', 'text')])
    data = dumps(db[collection].find({"$text": {"$search": string}}).limit(10))
    return data
