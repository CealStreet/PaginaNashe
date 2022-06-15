from django import forms
from .models import Contacto, producto 
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'
       
class CustomUserCreationForm(UserCreationForm):
    pass
    