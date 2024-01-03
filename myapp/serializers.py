from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age']


class AuthorWithBooksSerializer(serializers.ModelSerializer):
    book_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'age', 'book_set']