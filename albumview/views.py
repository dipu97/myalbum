from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    album_data=album.objects.all()
    context={
     'album_data':album_data
    }

    return render(request,'index.html',context)