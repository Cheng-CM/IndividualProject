# Create your views here.
from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets

from MoviesRecommendation.Recommend.models import Test, Titles
from MoviesRecommendation.Recommend.serializers import TestSerializer, TitlesSerializer


class TestViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TitlesViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Titles.objects.all()
    serializer_class = TestSerializer
