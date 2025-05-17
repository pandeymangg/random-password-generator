from django.urls import path
from . import views

app_name = 'generate'
urlpatterns = [
    path('', views.length, name='length'),
    path('password/', views.password, name='password'),
]
