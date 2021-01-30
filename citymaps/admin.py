from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import City, Completion, Tag


# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'content', 'completion', 'owner', 'use', 'area', 'floor', 'date', 'longitude', 'latitude', 'photo_image')

    def photo_image(self, obj):
        return mark_safe('<img src="{}" style="width:200px; height:auto;">'.format(obj.photo.url))


admin.site.register(City, CityAdmin)
admin.site.register(Completion)
admin.site.register(Tag)