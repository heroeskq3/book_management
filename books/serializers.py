from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
        extra_kwargs = {
            'title': {'help_text': 'The title of the book'},
            'author': {'help_text': 'The author of the book'},
            'published_date': {'help_text': 'The date when the book was published'},
        }
