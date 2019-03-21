from rest_framework_mongoengine import serializers

from backend.Recommend.models import (Links, Movies, Ratings, Tags,
                                      compare_ratings,scale_ratings)


class MoviesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class RatingsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'


class sRatingsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = scale_ratings
        fields = '__all__'

class cRatingsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = compare_ratings
        fields = '__all__'


class LinksSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Links
        fields = '__all__'


class TagsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
