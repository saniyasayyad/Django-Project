from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ['id', 'name', 'price', 'description', 'image']

        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'})
            }
=======
        fields = ['id', 'name', 'price', 'description']
>>>>>>> aee1c01f7da304bc88bb1521251d8b687b9a59a6
