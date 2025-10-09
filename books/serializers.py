from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author_id', 'genre', 'title', 'publication_year', 'isbn', 'page_count', 'rating', 'is_available', 'description']


    def create(self, validated_data):
        return Book(**validated_data)

