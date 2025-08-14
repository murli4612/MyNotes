from rest_framework import serializers
from .models import Movie ,Review

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         # field = '__all__'
#         exclude = ()
#         # include = ('title','release_year','created_at')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ()
        # fields = '__all__'
        # read_only_fields = ['movie', 'created_at']

class MovieSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        exclude = ()
        # fields = '__all__'
