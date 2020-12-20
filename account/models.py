from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Account(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='pictures/', blank=True, null=True)
    
    #Admin画面で、nameを表記させるためのもの
    def __str__(self): 
        return self.name

    #新規POST後に、どのURLに飛ばすか指定するためのもの
    def get_absolute_url(self):
        return reverse('blog-home')
