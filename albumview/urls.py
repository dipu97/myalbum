
# from django.contrib import admin
from django.urls import path
from .import views
from .views import AlbumCreate,Delete, Update
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',AlbumCreate.as_view(), name='create'),
    path('<int:id>/delete/',Delete.as_view(), name='delete'),
    path('<int:id>/update/',Update.as_view(),name='update'),
]