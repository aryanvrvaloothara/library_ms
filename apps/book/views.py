from django.utils import timezone
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.book.models import Book, BookLog
from apps.book.serializers import BookSerializer, BookLogSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title',
                     'author__first_name',
                     'author__first_name'
                     ]


class BookLogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = BookLog.objects.all()
    serializer_class = BookLogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            book_log_obj = serializer.save()
            book_obj = book_log_obj.book

            if book_log_obj.book.available_book_count is None:
                book_obj.available_book_count = book_obj.total_book_count - 1
                book_obj.save()
            elif book_log_obj.book.available_book_count == 0:
                return Response({"message": 'Book not available.'
                })
            else:
                book_obj.available_book_count = book_obj.available_book_count - 1
                book_obj.save()
        else:
            pass
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def book_returned(self, request, pk=None):
        instance = self.get_object()
        book_obj = instance.book
        if instance.returned_date is None:
            book_obj.available_book_count = book_obj.available_book_count + 1
            book_obj.save()
            instance.returned_date = timezone.now()
            instance.save()
        else:
            return Response({"message": 'Book already returned'
                             })
        return Response({"message": 'Book returned'
                         })
