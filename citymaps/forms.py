from django import forms
from .models import City

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields =  ['title', 'content', 'owner', 'completion','use', 'area', 'floor', 'image', 'url', 'source', 'photo', 'latitude','longitude','tag'] 