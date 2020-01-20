# Create your views here.
from random import randint

from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets

from backend.Recommend.models import (Links, Movies, Ratings, Tags,
                                      scale_ratings, compare_ratings)
from backend.Recommend.serializers import (LinksSerializer, MoviesSerializer,
                                           RatingsSerializer, TagsSerializer,
                                           sRatingsSerializer, cRatingsSerializer)
from django.http import HttpResponse

idList = []
for self in Movies.objects:
    idList.append(self.id)


def getRandomId():
    count = Movies.objects.count()
    return idList[randint(0, count)] if count != 0 else None
    
class rMoviesViewSet(meviewsets.ModelViewSet):
    def get_queryset(self):
        return Movies.objects.filter(id=getRandomId())
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
    queryset = compare_ratings.objects.all()
    serializer_class = cRatingsSerializer

class sRatingsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = scale_ratings.objects.all()
    serializer_class = sRatingsSerializer


class gcRatingsViewSet(meviewsets.ModelViewSet):
    def get_queryset(self):
        return scale_ratings.objects.all().order_by('-userId').limit(1)
    queryset = get_queryset(scale_ratings)
    serializer_class = sRatingsSerializer

class LinksViewSet(meviewsets.ModelViewSet):
    lookup_field = 'movieId'
    queryset = Links.objects.all()
    serializer_class = LinksSerializer


class TagsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer