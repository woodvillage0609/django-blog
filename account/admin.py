from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'photo_image','id')

    def photo_image(self, obj):
        return mark_safe('<img src="{}" style="width:200px; height:auto;">'.format(obj.photo.url))


admin.site.register(Account, AccountAdmin)
