from django.contrib import admin
from .models import Categoria, Producto

#Registro de modelo en panel admin
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #Definir que columnas se veran en la lista
    list_display = ['nombre', 'categoria', 'cantidad','precio', 'codigo', 'stock_bajo']
    #Filtro
    list_filter = ['categoria']
    #Busqueda por nombre o codigo
    search_fields = ['nombre', 'codigo']
