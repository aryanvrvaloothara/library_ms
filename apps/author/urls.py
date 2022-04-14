from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.author.views import AuthorViewSet

router = DefaultRouter()
router.register('details', AuthorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]