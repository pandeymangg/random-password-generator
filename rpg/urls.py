from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('generate.urls', namespace='generate')),
    path('admin/', admin.site.urls),
]