from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenViewBase

from apps.user.models import User
from apps.user.serializers import UserSerializer, MyAuthTokenSerializer


class MyTokenObtainPairView(TokenViewBase):
    serializer_class = MyAuthTokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

