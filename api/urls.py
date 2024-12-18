
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/diary', include('diary.urls'))
    path('api/users', include('users.urls'))
]
