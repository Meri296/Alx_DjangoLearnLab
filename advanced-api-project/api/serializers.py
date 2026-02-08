from rest_framework import serializers
from datetime import date
from .models import Author, Book


# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation: publication year must not be in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: shows all books written by this author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
