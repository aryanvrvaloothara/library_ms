from rest_framework import serializers

from apps.book.models import Book, BookLog


class BookSerializer(serializers.ModelSerializer):
    available_book_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookLog
        fields = '__all__'