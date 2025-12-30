from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
            'description': 'Description',
            }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'e.g 1','class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g Widget','class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': 'e.g WGT-001','class': 'form-control'}),
            'price': forms.FloatField(attrs={'placeholder': 'e.g 19.99','  class': 'form-control'}),
            'quantity': forms.IntegerField(attrs={'placeholder': 'e.g 100','class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'e.g Acme Corp','class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Product description here','class': 'form-control', 'rows': 3}),
        }
          