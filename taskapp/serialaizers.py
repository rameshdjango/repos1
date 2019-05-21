
from rest_framework import serializers
from taskapp.models import imdb


class ImdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = imdb
        fields = ('id','popularity', 'director', 'genre', 'imdb_score','name')

        def imdbupdate(self, instance, validated_data):
            instance.popularity = validated_data.get('popularity', instance.popularity)
            instance.director = validated_data.get('director', instance.director)
            instance.genre = validated_data.get('genre', instance.genre)
            instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
            instance.name = validated_data.get('name', instance.name)
            instance.save()
            return instance

