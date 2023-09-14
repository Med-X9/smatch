from django import forms
from .models import Projet

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description', 'slug', 'categorie', 'client', 'image']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    emailid = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=20, required=False)
    msg = forms.CharField(widget=forms.Textarea, required=True)
