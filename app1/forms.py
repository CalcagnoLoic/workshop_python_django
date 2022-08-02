from django import forms
from app1.models import ModelFilm


class AddFilm(forms.Form):
    class Meta:
        model = ModelFilm
        fields = '__all__'


class ContactUs(forms.Form):
    name = forms.CharField(max_length=150, label="Nom et prénom ", widget=forms.TextInput(attrs={'Placeholder': 'Votre nom et prénom'}))
    email = forms.EmailField(label="Votre email ", widget=forms.TextInput(attrs={'Placeholder': 'Votre email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'Placeholder': 'Votre message...'}), label="Votre message ")
