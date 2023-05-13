from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'stock', 'price', 'category', 'image']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'profile_image']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
