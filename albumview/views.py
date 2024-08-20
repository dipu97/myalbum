
from django.shortcuts import render

from .forms import AlbumForm
from .models import album
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views here.

class AlbumCreate(CreateView):
    model=album
    form_class=AlbumForm
    template_name='album/create.html'
    success_url='/'
def index(request):
    album_data=album.objects.all()
    context={
     'album_data':album_data
    }

    return render(request,'index.html',context)