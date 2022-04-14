from django.contrib import admin
from django.urls import path, include

from apps.user.views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # authentication apis
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('user/', include('apps.user.urls')),
    path('book/', include('apps.book.urls')),
    path('author/', include('apps.author.urls')),
]
