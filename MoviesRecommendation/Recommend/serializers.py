from rest_framework_mongoengine import serializers
from MoviesRecommendation.Recommend.models import Titles

class TitlesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Titles
        fields = '__all__'