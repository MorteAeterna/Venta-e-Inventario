import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario.settings')
django.setup()

from productos.models import Categoria, Producto, Venta, DetalleVenta
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import random

# Limpiar datos existentes
Producto.objects.all().delete()
Categoria.objects.all().delete()
Venta.objects.all().delete()

# Categorías
bebidas = Categoria.objects.create(nombre="Bebidas")
lacteos = Categoria.objects.create(nombre="Lácteos")
snacks = Categoria.objects.create(nombre="Snacks")
limpieza = Categoria.objects.create(nombre="Limpieza")
panaderia = Categoria.objects.create(nombre="Panadería")
congelados = Categoria.objects.create(nombre="Congelados")
higiene = Categoria.objects.create(nombre="Higiene Personal")

# Productos
productos = [
    # Bebidas
    {"nombre": "Bebida 3L", "marca": "Coca-Cola", "categoria": bebidas, "cantidad": 24, "precio": 2490, "codigo": "7500435126748", "stock_minimo": 6},
    {"nombre": "Bebida 3L", "marca": "Pepsi", "categoria": bebidas, "cantidad": 18, "precio": 2290, "codigo": "7501055305017", "stock_minimo": 6},
    {"nombre": "Bebida 3L", "marca": "Kem", "categoria": bebidas, "cantidad": 20, "precio": 1990, "codigo": "7802800012345", "stock_minimo": 6},
    {"nombre": "Bebida 1.5L", "marca": "Coca-Cola", "categoria": bebidas, "cantidad": 36, "precio": 1590, "codigo": "7500435110830", "stock_minimo": 10},
    {"nombre": "Bebida 1.5L", "marca": "Sprite", "categoria": bebidas, "cantidad": 30, "precio": 1490, "codigo": "7500435113077", "stock_minimo": 10},
    {"nombre": "Agua Mineral 1.6L", "marca": "Cachantun", "categoria": bebidas, "cantidad": 48, "precio": 890, "codigo": "7802800023456", "stock_minimo": 12},
    {"nombre": "Agua Mineral 1.6L", "marca": "Vital", "categoria": bebidas, "cantidad": 40, "precio": 890, "codigo": "7802800034567", "stock_minimo": 12},
    {"nombre": "Jugo 1L", "marca": "Watts", "categoria": bebidas, "cantidad": 24, "precio": 1290, "codigo": "7802800045678", "stock_minimo": 8},
    {"nombre": "Jugo 1L", "marca": "Jumex", "categoria": bebidas, "cantidad": 20, "precio": 1190, "codigo": "7500435120340", "stock_minimo": 8},
    {"nombre": "Energizante 500ml", "marca": "Monster", "categoria": bebidas, "cantidad": 4, "precio": 1990, "codigo": "7802800056789", "stock_minimo": 6},
    {"nombre": "Energizante 500ml", "marca": "Red Bull", "categoria": bebidas, "cantidad": 3, "precio": 2290, "codigo": "7802800067890", "stock_minimo": 6},

    # Lácteos
    {"nombre": "Leche Entera 1L", "marca": "Soprole", "categoria": lacteos, "cantidad": 30, "precio": 990, "codigo": "7802800078901", "stock_minimo": 10},
    {"nombre": "Leche Entera 1L", "marca": "Colun", "categoria": lacteos, "cantidad": 28, "precio": 950, "codigo": "7802800089012", "stock_minimo": 10},
    {"nombre": "Yogurt 165g", "marca": "Soprole", "categoria": lacteos, "cantidad": 24, "precio": 590, "codigo": "7802800090123", "stock_minimo": 8},
    {"nombre": "Yogurt 165g", "marca": "Danone", "categoria": lacteos, "cantidad": 20, "precio": 650, "codigo": "7802800101234", "stock_minimo": 8},
    {"nombre": "Queso Laminado 150g", "marca": "Colun", "categoria": lacteos, "cantidad": 15, "precio": 1890, "codigo": "7802800112345", "stock_minimo": 5},
    {"nombre": "Mantequilla 200g", "marca": "Colun", "categoria": lacteos, "cantidad": 12, "precio": 1590, "codigo": "7802800123456", "stock_minimo": 4},

    # Snacks
    {"nombre": "Papas Fritas 180g", "marca": "Lays", "categoria": snacks, "cantidad": 20, "precio": 1490, "codigo": "7802800134567", "stock_minimo": 6},
    {"nombre": "Papas Fritas 180g", "marca": "Pringles", "categoria": snacks, "cantidad": 18, "precio": 1890, "codigo": "7802800145678", "stock_minimo": 6},
    {"nombre": "Galletas 200g", "marca": "Oreo", "categoria": snacks, "cantidad": 24, "precio": 1290, "codigo": "7802800156789", "stock_minimo": 8},
    {"nombre": "Galletas 200g", "marca": "Costa", "categoria": snacks, "cantidad": 20, "precio": 990, "codigo": "7802800167890", "stock_minimo": 8},
    {"nombre": "Chocolate 100g", "marca": "Ambrosoli", "categoria": snacks, "cantidad": 16, "precio": 890, "codigo": "7802800178901", "stock_minimo": 6},
    {"nombre": "Chocolate 100g", "marca": "Sahne-Nuss", "categoria": snacks, "cantidad": 14, "precio": 990, "codigo": "7802800189012", "stock_minimo": 6},
    {"nombre": "Maní 200g", "marca": "Kris", "categoria": snacks, "cantidad": 3, "precio": 790, "codigo": "7802800190123", "stock_minimo": 6},

    # Limpieza
    {"nombre": "Detergente 1kg", "marca": "Omo", "categoria": limpieza, "cantidad": 15, "precio": 3490, "codigo": "7802800201234", "stock_minimo": 4},
    {"nombre": "Detergente 1kg", "marca": "Ariel", "categoria": limpieza, "cantidad": 12, "precio": 3690, "codigo": "7802800212345", "stock_minimo": 4},
    {"nombre": "Cloro 1L", "marca": "Bioram", "categoria": limpieza, "cantidad": 20, "precio": 990, "codigo": "7802800223456", "stock_minimo": 6},
    {"nombre": "Esponja Multiuso", "marca": "Scotch-Brite", "categoria": limpieza, "cantidad": 2, "precio": 790, "codigo": "7802800234567", "stock_minimo": 5},
    {"nombre": "Limpiapisos 1L", "marca": "Mr. Músculo", "categoria": limpieza, "cantidad": 10, "precio": 2190, "codigo": "7802800245678", "stock_minimo": 4},

    # Panadería
    {"nombre": "Pan de Molde", "marca": "Ideal", "categoria": panaderia, "cantidad": 18, "precio": 1890, "codigo": "7802800256789", "stock_minimo": 6},
    {"nombre": "Pan de Molde", "marca": "Castaño", "categoria": panaderia, "cantidad": 15, "precio": 1790, "codigo": "7802800267890", "stock_minimo": 6},
    {"nombre": "Tostadas 200g", "marca": "Trigoro", "categoria": panaderia, "cantidad": 12, "precio": 1290, "codigo": "7802800278901", "stock_minimo": 4},

    # Congelados
    {"nombre": "Helado 1L", "marca": "Bresler", "categoria": congelados, "cantidad": 10, "precio": 2990, "codigo": "7802800289012", "stock_minimo": 3},
    {"nombre": "Helado 1L", "marca": "Savory", "categoria": congelados, "cantidad": 8, "precio": 3190, "codigo": "7802800290123", "stock_minimo": 3},
    {"nombre": "Pizza Congelada", "marca": "Dr. Oetker", "categoria": congelados, "cantidad": 6, "precio": 3990, "codigo": "7802800301234", "stock_minimo": 3},

    # Higiene
    {"nombre": "Shampoo 400ml", "marca": "Head & Shoulders", "categoria": higiene, "cantidad": 12, "precio": 3990, "codigo": "7802800312345", "stock_minimo": 4},
    {"nombre": "Shampoo 400ml", "marca": "Pantene", "categoria": higiene, "cantidad": 10, "precio": 3790, "codigo": "7802800323456", "stock_minimo": 4},
    {"nombre": "Pasta Dental 100g", "marca": "Colgate", "categoria": higiene, "cantidad": 20, "precio": 1490, "codigo": "7802800334567", "stock_minimo": 6},
    {"nombre": "Jabón 100g", "marca": "Dove", "categoria": higiene, "cantidad": 24, "precio": 990, "codigo": "7802800345678", "stock_minimo": 8},
    {"nombre": "Desodorante 150ml", "marca": "Rexona", "categoria": higiene, "cantidad": 4, "precio": 2490, "codigo": "7802800356789", "stock_minimo": 6},
]

productos_creados = []
for p in productos:
    producto = Producto.objects.create(**p)
    productos_creados.append(producto)
    print(f" {producto.nombre} - {producto.marca}")

# Ventas de ejemplo
admin = User.objects.filter(username='admin').first()

def crear_venta(dias_atras, items):
    venta = Venta.objects.create(usuario=admin, total=0)
    venta.fecha = datetime.now() - timedelta(days=dias_atras)
    total = 0
    for producto, cantidad in items:
        subtotal = producto.precio * cantidad
        total += subtotal
        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=producto.precio,
            subtotal=subtotal
        )
    venta.total = total
    venta.save()
    print(f"Venta #{venta.id} - ${total:,} CLP")

# Obtener productos por nombre y marca
def get_producto(nombre, marca):
    return Producto.objects.get(nombre=nombre, marca=marca)

crear_venta(0, [
    (get_producto("Bebida 3L", "Coca-Cola"), 2),
    (get_producto("Papas Fritas 180g", "Lays"), 1),
    (get_producto("Agua Mineral 1.6L", "Cachantun"), 3),
])

crear_venta(0, [
    (get_producto("Leche Entera 1L", "Soprole"), 2),
    (get_producto("Pan de Molde", "Ideal"), 1),
    (get_producto("Yogurt 165g", "Danone"), 3),
])

crear_venta(1, [
    (get_producto("Energizante 500ml", "Monster"), 1),
    (get_producto("Chocolate 100g", "Sahne-Nuss"), 2),
    (get_producto("Galletas 200g", "Oreo"), 1),
])

crear_venta(1, [
    (get_producto("Detergente 1kg", "Ariel"), 1),
    (get_producto("Cloro 1L", "Bioram"), 2),
    (get_producto("Esponja Multiuso", "Scotch-Brite"), 3),
])

crear_venta(2, [
    (get_producto("Helado 1L", "Savory"), 2),
    (get_producto("Bebida 1.5L", "Sprite"), 3),
    (get_producto("Papas Fritas 180g", "Pringles"), 2),
])

crear_venta(3, [
    (get_producto("Shampoo 400ml", "Pantene"), 1),
    (get_producto("Pasta Dental 100g", "Colgate"), 2),
    (get_producto("Jabón 100g", "Dove"), 3),
])

crear_venta(5, [
    (get_producto("Pizza Congelada", "Dr. Oetker"), 2),
    (get_producto("Jugo 1L", "Watts"), 3),
    (get_producto("Bebida 3L", "Pepsi"), 1),
])

crear_venta(7, [
    (get_producto("Queso Laminado 150g", "Colun"), 2),
    (get_producto("Mantequilla 200g", "Colun"), 1),
    (get_producto("Pan de Molde", "Castaño"), 2),
])

print("\nDatos de ejemplo creados exitosamente.")