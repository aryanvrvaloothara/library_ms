from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.book.views import BookViewSet, BookLogViewSet

router = DefaultRouter()
router.register('details', BookViewSet)

router1 = DefaultRouter()
router1.register('details', BookLogViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('log/', include(router1.urls)),
]