from rest_framework_mongoengine import serializers
from MoviesRecommendation.Recommend.models import Test,Titles


class TestSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TitlesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Titles
        fields = '__all__'