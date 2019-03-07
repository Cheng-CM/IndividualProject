# Create your views here.
from random import randint

from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets

from backend.Recommend.models import (Links, Movies, Ratings, Tags,
                                      custom_ratings)
from backend.Recommend.serializers import (LinksSerializer, MoviesSerializer,
                                           RatingsSerializer, TagsSerializer,
                                           cRatingsSerializer,
                                           rMoviesSerializer)


class rMoviesViewSet(meviewsets.ModelViewSet):
    def update():
        count = Movies.objects.count()
        rint = randint(1, count)
        return rint
    # queryset = Movies.objects(movieId = update())
    queryset = Movies.objects[0:20]
    serializer_class = MoviesSerializer


class MoviesViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class RatingsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class cRatingsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = custom_ratings.objects.all()
    serializer_class = cRatingsSerializer


class LinksViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class TagsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
