from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'stock', 'price', 'category', 'image']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'profile_image']
