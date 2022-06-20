from django.shortcuts import render, redirect, get_object_or_404
from .models import*
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.
class ProductoViewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

def index(request):
    return render(request, 'dogs/index.html')

def quienes(request):
    return render(request, 'dogs/quienessomos.html')

def galeria(request):
  
    return render(request, 'dogs/galeria.html')

def contacto(request):
    data = {
        'contacto': ContactoForm()
     }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Solicitud Enviada"
        else:
            data["form"] = formulario

    return render(request, 'dogs/contactanos.html', data)


def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Guardado Correctamente"
        
        
    return render(request, 'dogs/producto/agregar.html', data)

def listarpreducto(request):
    productos= producto.objects.all()

    data ={
        'productos': productos
    }
    return render(request, 'dogs/producto/lista.html', data)

def modificarproducto( request, id):
    
    producto = get_object_or_404(producto, id=id)

    data = {
        'form': ProductoForm(instance=producto) 
    }

    
    return render(request, 'dogs/producto/modificar.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="Inicio")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)




