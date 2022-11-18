import datetime
from .models.movie import Movie
from .models.actor import Actor
from .models.comment import Comment
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    # def validate_birthdate(self, value):
    #     date = datetime.datetime(1950, 1, 1)
    #     if not value.year < date.year:
    #         return ValidationError(detail="Hey birthdate > 01.01.1950")

class MovieSerializer(serializers.ModelSerializer):
    # actor = ActorSerializer()
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genre', 'actor', 'watched')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("movie", "text", "created_date")