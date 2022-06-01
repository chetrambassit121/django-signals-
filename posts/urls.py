from django.contrib import admin
from django.urls import path, include
from posts import views  


urlpatterns = [
    path('posts/', views.post_view, name='posts'),
]
