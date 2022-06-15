from django.urls import path
from .views import *
from . import views


urlpatterns=[
    path('', index,name="Inicio"),
    
    path('quienessomos/', quienes, name='QuienesSomos'),

    path('galeria/', galeria, name='Galeria'),

    path('contactanos/', contacto, name='Contactanos'),

    path('agregar-producto/', agregar_producto, name="agregar_producto"),

    path('listar-producto/', listarpreducto, name="listar_producto"),

    path('modificar-producto/<id>/', modificarproducto, name="modificar_productos"),

    path('registro/', registro,name="registro"),




   
    
]
