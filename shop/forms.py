from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'image_url']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
