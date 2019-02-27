# Create your views here.
from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets

from MoviesRecommendation.Recommend.models import Titles
from MoviesRecommendation.Recommend.serializers import TitlesSerializer

class TitlesViewSet(meviewsets.ModelViewSet):
    lookup_field = 'tconst'
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
