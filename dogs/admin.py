from django.contrib import admin
from .models import *

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre","precio", "descripcion"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_filter=["precio"]
    list_per_page= 5

admin.site.register(producto, ProductoAdmin)
admin.site.register(Contacto)