from django.shortcuts import render, redirect
from .carro import Carro
from dogs.models import producto

# Create your views here.
def agregar_producto(requets, producto_id):

    carro=Carro(requets)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")

def eliminar_producto(requets, producto_id):

    carro=Carro(requets)
    producto=producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(requets, producto_id):

    carro=Carro(requets)
    producto=producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

def limpiar_carro(requets, producto_id):

    carro=Carro(requets)
    carro.limpiar_carro()
    return redirect("Tienda")