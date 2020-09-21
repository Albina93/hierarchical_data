from django import forms
from . import models
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
   
    
