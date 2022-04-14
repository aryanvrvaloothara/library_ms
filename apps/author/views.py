from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.author.models import Author
from apps.author.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
