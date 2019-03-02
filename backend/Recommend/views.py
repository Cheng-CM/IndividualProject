# Create your views here.
from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets

from backend.Recommend.models import Movies, Ratings, Links, Tags
from backend.Recommend.serializers import MoviesSerializer, RatingsSerializer, LinksSerializer, TagsSerializer


class MoviesViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class RatingsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

class LinksViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class TagsViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer