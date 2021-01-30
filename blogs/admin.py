from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog, Category, Tag


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'content', 'author', 'category', 'date', 'longitude', 'latitude', 'photo_image')

    def photo_image(self, obj):
        return mark_safe('<img src="{}" style="width:200px; height:auto;">'.format(obj.photo.url))


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)

