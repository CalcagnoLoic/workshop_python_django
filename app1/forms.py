from django import forms
from app1.models import ModelFilm


class AddFilm(forms.ModelForm):
    class Meta:
        model = ModelFilm
        fields = '__all__'
