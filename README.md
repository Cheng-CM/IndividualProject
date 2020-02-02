# Movie Recommendation System

Indivdual project: Recommendation Systems based on movie comparison in **Surprise**, **Django**, **Vue.js** and **MongoDB**. Movie posters provided by The Movie Database API.

![Result.gif](https://upload.cc/i1/2020/02/01/W3FAxK.gif)

## What is this

This is a experiment to see which rating method (5 stars, Item comparison) are more effective in dealing with user opinions.

## Preview

### Search for movies

![Search.png](https://upload.cc/i1/2020/02/02/z4ctb3.png)
>Users can select the movie from the list by drag-and-dropping the movie items. Users can search for the movies using the searching function, and also movie list will generate random movies from database.

### Rate movies

![5Stars.png](https://upload.cc/i1/2020/02/02/yWTFIi.png)

>This is the interface of the 5-star scale ratings that act as the control group.

![comparison.png](https://upload.cc/i1/2020/02/02/5Nsezi.png)
>User then use the proposed item comparison scale method to rate movies, user the drag
and drop the movie poster from the top to organize the queue/slider, where user can move
the slider buttons to rate the movies.

### Generate recommendations predictions

![recommendations.png](https://upload.cc/i1/2020/02/02/LzKkv0.png)

>After they rated the movie using both of the methods, user can view the prediction movie list from the system, which are generated using recommendation engine with the SVD algorithms.

## Results

### RMSE

![RMSE.png](https://upload.cc/i1/2020/02/02/v7k6YG.png)

>The figure above shows the answers users in experiments had given, the RMSE mean in for each experiments are close to 1, where item-comparison method has a lower mean of RMSE, as lower is better for RMSE and MAE.

### MAE

![MAE.png](https://upload.cc/i1/2020/02/02/pB7yvz.png)
>For MAE, The figure above shows a similar result, after experiments had completed, the the MAEmean in for each experiments are close to 0.75, where item-comparison method has a lower mean of MAE, which show again, Item comparison method are slightly better than a 5 star-scale method in the control group.

## Development setup

Required:

* **Python3**
* **MongoDB**
* **Node.js**

### Config setup

`config.json` and `mongo-config.yml` is required to connected to mongodb:

#### config.json

Place it in `frontend/src/`

api_key can requested in The Movie Database API page.

[The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)

It look like this:

```json
{
        "development": {
                "config_id": "development",
                "database": "localhost",
                "db_port": "8000",
                "api_key": "your_api_key_here"
        }
}
```

#### mongo-config

Place it in `./`

It look like this:

```yml
uri: "localhost"
port: 27017
db: "movies"
collections:
  - "links"
  - "movies"
  - "ratings"
  - "tags"
  - "UserChoices"
  - "regressionresult"
  - "scale_ratings"
  - "compare_ratings"
```

### Database import

import MongoDB using `mongorestore.exe` in `\MongoDB\Server\[Version]\bin`

```sh
mongorestore --db movies --verbose [path]/data/dataset
```

### Backend

```sh
pip install -r requirements.txt
python manage.py runserver
```

### Frontend

```sh
cd frontend
yarn install
yarn serve
```

## Author

Made by Cheng-CM – chengchakman@gmail.com

[https://github.com/Cheng-CM](https://github.com/Cheng-CM/)