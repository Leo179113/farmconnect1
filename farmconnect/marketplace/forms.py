from django import forms
from .models import CustomUser, Product, Order, Message

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'is_farmer', 'is_consumer')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255, required=False)
