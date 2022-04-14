import django
from django.db import models

from apps.author.models import Author
from apps.user.models import User


class Book(models.Model):
    serial_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=45)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    total_book_count = models.IntegerField(default=0)
    available_book_count = models.IntegerField(null=True, blank=True)
    year_of_publication = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = "book"


class BookLog(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book', on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=django.utils.timezone.now)
    returned_date = models.DateTimeField(null=True, blank=True)

