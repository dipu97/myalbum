from django.urls import reverse
from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class album(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=256)
    image=CloudinaryField('image',use_filename=True,
                        unique_filename=True,
                        folder='myalbum/photo')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_delete_url(self):
        return reverse('delete', kwargs={'id':self.id})
    def get_update_url(self):
        return reverse('update',kwargs={'id':self.id})