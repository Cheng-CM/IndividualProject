# Movie Recommendation System

Indivdual project: Recommendation Systems based on movie comparison in Surprise, Django, Vue.js and MongoDB.

![Result.gif](https://upload.cc/i1/2020/02/01/W3FAxK.gif)

## What is this

This is a experiment to see which rating method (5 stars, Item comparison) are more effective in dealing with user opinions.

## Example

### Search for movies

![Search.png](https://upload.cc/i1/2020/02/02/z4ctb3.png)
Users can select the movie from the list by drag-and-dropping the movie items. Users can search for the movies using the searching function, and also movie list will generate random movies from database.

### Rate movies

![5Stars.png](https://upload.cc/i1/2020/02/02/yWTFIi.png)
This is the interface of the 5-star scale ratings that act as the control group.
![comparison.png](https://upload.cc/i1/2020/02/02/5Nsezi.png)
User then use the proposed item comparison scale method to rate movies, user the drag
and drop the movie poster from the top to organize the queue/slider, where user can move
the slider buttons to rate the movies.

### Generate recommendations predictions

![recommendations.png](https://upload.cc/i1/2020/02/02/LzKkv0.png)
After they rated the movie using both of the methods, user can view the prediction movie list from the system, which are generated using recommendation engine with the SVD algorithms.
## Results
![Results.png](https://upload.cc/i1/2020/02/02/ZjoctV.png)
However, from the data collected, it shows that the sum of precision from item comparison are lower than scale method.
### RMSE

![RMSE.png](https://upload.cc/i1/2020/02/02/v7k6YG.png)
The figure above shows the answers users in experiments had given, it shows that after 23
experiments conducted, the RMSE mean in for each experiments are close to 1, where
item-comparison method has a lower mean of RMSE, as lower is better for RMSE and MAE.
### MAE

![MAE.png](https://upload.cc/i1/2020/02/02/pB7yvz.png)
For MAE, The figure above shows a similar result, after experiments had completed, the the
MAEmean in for each experiments are close to 0.75, where item-comparison method has a
lower mean of MAE, which show again, Item comparison method are slightly better than a 5
star-scale method in the control group.
## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

### Config setup

### Database import

```sh
install requirements
run python manage.py runserver
```

### Backend

```sh
install requirements
python manage.py runserver
```

### Frontend

```sh
cd frontend
yarn install
yarn serve
```

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)