from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):
  
    class Meta:
        model = Contacto
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    image = forms.ImageField(required=False)
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombre
    class Meta:
        model = producto
        fields = '__all__'
       
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]