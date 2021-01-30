from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Completion(models.Model):
    name = models.CharField('カテゴリー', max_length=50)
   
    #Admin画面で、カテゴリーを表記させるためのもの
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('タグ', max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    title = models.CharField(verbose_name='建物名', max_length=100)
    subtitle = models.TextField(blank=True, null=True)
    content = RichTextUploadingField()
    owner = models.CharField(verbose_name='事業主', max_length=100)
    completion = models.ForeignKey(
                    Completion, verbose_name= '竣工年',
                    on_delete=models.PROTECT
            )
    use = models.CharField(verbose_name='用途', max_length=200)
    area = models.CharField(verbose_name='延床面積', max_length=200)
    floor = models.CharField(verbose_name='階数', max_length=200)
    image = models.CharField(verbose_name='完成イメージ', max_length=500)
    url = models.CharField(verbose_name='リンク先', max_length=500)
    source = models.CharField(verbose_name='出典元', max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='pictures/', blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    #タグ関連の表記
    tag = models.ManyToManyField(Tag, verbose_name='タグ')


    #Admin画面で、titleを表記させるためのもの
    def __str__(self): 
        return self.title

    #新規POST後に、どのURLに飛ばすか指定するためのもの
    def get_absolute_url(self):
        return reverse('citymap-detail', kwargs={'pk':self.pk})
