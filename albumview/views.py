from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import AlbumForm
from .models import album
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views here.

class AlbumCreate(LoginRequiredMixin, CreateView):
    model=album
    form_class=AlbumForm
    template_name='album/create.html'
    success_url='/'

class Delete(LoginRequiredMixin, DeleteView):
    template_name='album/delete.html'
    def get_object(self):
        id=self.kwargs.get('id')
        return get_object_or_404(album,id=id)
    def get_success_url(self):
        return reverse('index')
class Update(LoginRequiredMixin, UpdateView):
    template_name='album/edit.html'
    form_class=AlbumForm
    def get_object(self):
        id=self.kwargs.get('id')
        return get_object_or_404(album,id=id)
    def get_success_url(self):
        return reverse('index')
def index(request):
    album_data=album.objects.all()
    context={
     'album_data':album_data
    }

    return render(request,'index.html',context)