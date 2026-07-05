import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', 'admin1234')
    print("Superusuario creado")
else:
    print("El superusuario ya existe")