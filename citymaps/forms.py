from django import forms
from .models import City

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields =  ['title', 'content', 'photo', 'completion','latitude','longitude','tag'] 