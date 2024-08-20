
# from django.contrib import admin
from django.urls import path
from .import views
from .views import AlbumCreate
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',AlbumCreate.as_view(), name='create'),
]