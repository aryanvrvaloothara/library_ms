from rest_framework import serializers

from apps.author.models import Author
from apps.book.serializers import BookSerializer


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = '__all__'