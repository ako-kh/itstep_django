from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['is_available', 'wishlist']

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['wishlist']
