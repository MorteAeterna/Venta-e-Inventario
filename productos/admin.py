from django.contrib import admin
from .models import Categoria, Producto
from .models import Categoria, Producto, Venta, DetalleVenta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'total', 'usuario']

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal']
    
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
