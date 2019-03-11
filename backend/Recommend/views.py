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


def getRandomId():
    count = Movies.objects.count()
    return randint(0, count)


class rMoviesViewSet(meviewsets.ModelViewSet):
    def get_queryset(self):
        idList = []
        for self in Movies.objects:
            idList.append(self.id)
        return Movies.objects.filter(id= idList[getRandomId()])
    queryset = get_queryset(Movies)
    serializer_class = MoviesSerializer


class MoviesViewSet(meviewsets.ModelViewSet):
    lookup_field = 'movieId'
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
