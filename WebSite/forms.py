from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'email', 'product', 'price']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'product': forms.HiddenInput(),
            'price': forms.HiddenInput(),
        }