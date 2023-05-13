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

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Pesquisar produto', max_length=100)