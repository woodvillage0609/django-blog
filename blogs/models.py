from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)
   
    #Admin画面で、カテゴリーを表記させるためのもの
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('タグ', max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='pictures/', blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    category = models.ForeignKey(
                    Category, verbose_name= 'カテゴリー',
                    on_delete=models.PROTECT
            )
    #タグ関連の表記
    tag = models.ManyToManyField(Tag, verbose_name='タグ')
    relation = models.ManyToManyField('self', verbose_name='関連', blank=True, null=True)

    #Admin画面で、titleを表記させるためのもの
    def __str__(self): 
        return self.title

    #新規POST後に、どのURLに飛ばすか指定するためのもの
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk':self.pk})