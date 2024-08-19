from django.contrib import admin
from .models import album
# Register your models here.
class ModelAlbum(admin.ModelAdmin):
    list_display=['title', 'image','created_at']
    search_fields=['title']


admin.site.register(album,ModelAlbum)