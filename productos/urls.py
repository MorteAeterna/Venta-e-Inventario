from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('escanear/', views.escanear, name='escanear'),
    path('escanear/procesar/', views.procesar_escaneo, name='procesar_escaneo'),
    path('qr/', views.generar_qr, name='generar_qr'),
    path('stock/<int:pk>/', views.agregar_stock, name='agregar_stock'),
    path('ventas/', views.nueva_venta, name='nueva_venta'),
    path('ventas/', views.nueva_venta, name='nueva_venta'),
    path('ventas/agregar-item/', views.agregar_item_carrito, name='agregar_item_carrito'),
    path('ventas/eliminar-item/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('ventas/confirmar/', views.confirmar_venta, name='confirmar_venta'),
    path('ventas/historial/', views.historial_ventas, name='historial_ventas'),
    path('ventas/detalle/<int:pk>/', views.detalle_venta, name='detalle_venta'),
    path('categorias/crear-ajax/', views.crear_categoria_ajax, name='crear_categoria_ajax'),
]