# Ventario

Sistema web de gestión de inventario y ventas para minimarket desarrollado con **Django**, diseñado para administrar productos, categorías, stock y ventas mediante una interfaz moderna e intuitiva, con soporte para escaneo de códigos de barras desde dispositivos móviles.

---

## Demo

**Aplicación:**
https://venta-e-inventario.onrender.com

### Credenciales de prueba

Usuario:
```
admin
```

Contraseña:
```
admin1234
```
---

## Características

- Autenticación de usuarios
- Gestión completa de productos con nombre, marca, categoría, precio y código de barras
- Control de stock con alertas visuales de stock bajo
- Escaneo de códigos de barras desde dispositivos móviles via QR
- Agregar stock desde el inventario o desde el escáner
- Gestión de categorías con contador de productos asociados
- Carrito de compras con búsqueda por nombre, marca o código
- Registro de ventas con descuento automático de stock
- Historial de ventas con detalle por transacción
- Formato de precios en CLP
- Diseño responsive compatible con móvil
- Interfaz moderna con Bootstrap 5
- Datos de demostración incluidos

---

## Tecnologías

|  Tecnología  | Uso |
|------------  |-----|
|   Django 6   | Framework Backend |
| Python 3.13  | Lenguaje |
| Bootstrap 5  | Interfaz |
| Choices.js   | Selectores con búsqueda |
|    ZXing     | Escaneo de códigos de barras |
| PostgreSQL   | Base de datos |
|   Gunicorn   | Servidor WSGI |
|    Render    | Despliegue |
| Git + GitHub | Control de versiones |

---

## Capturas

### Login

<img width="1902" height="904" alt="image" src="https://github.com/user-attachments/assets/aa864f77-cc93-4951-a37d-6909b8ad2e83" />


---

### Inventario

<img width="1891" height="907" alt="image" src="https://github.com/user-attachments/assets/3d237614-bd43-49a3-a47a-382095d4e1ce" />


---

### Escaner Movil
Desde PC

<img width="1898" height="906" alt="image" src="https://github.com/user-attachments/assets/5bdd84a4-fe4f-4059-8c75-cc0911c38ea4" />



Desde un dispositivo movil

<img width="720" height="1394" alt="image" src="https://github.com/user-attachments/assets/8466dbe6-8878-417a-8198-682b5009e67e" />



---

### Ventas

<img width="1904" height="906" alt="image" src="https://github.com/user-attachments/assets/88290777-3899-4aa3-9b1d-96fe1e2380de" />


---

### Historial de Ventas

<img width="1907" height="910" alt="image" src="https://github.com/user-attachments/assets/b94f155d-b95a-4070-aa7a-adbb20867ea3" />


---

### Categorias

<img width="1907" height="906" alt="image" src="https://github.com/user-attachments/assets/42390b17-c8f7-4551-86ca-2e8524175dbd" />


---

## Estructura del proyecto

```
Ventario/
│
├── productos/
│   ├── migrations/
│   ├── templatetags/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── inventario/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── registration/
│       └── login.html
│
├── manage.py
├── requirements.txt
├── build.sh
├── poblar_datos.py
└── README.md
```
## Instalacion

Clonar el repositorio
```bash
git clone https://github.com/MorteAeterna/Ventario.git
```

Entrar al proyecto
```bash
cd inventario
```

Crear entorno virtual
```bash
python -m venv venv
```

Activar entorno

Windows
```bash
venv\Scripts\activate
```

Linux / macOS
```bash
source venv/bin/activate
```

Instalar dependencias
```bash
pip install -r requirements.txt
```

Ejecutar migraciones
```bash
python manage.py migrate
```

Poblar datos de demostracion
```bash
python poblar_datos.py
```

Iniciar servidor
```bash
python manage.py runserver
```

Sin configuracion adicional necesaria. El proyecto usa SQLite por defecto al correr localmente.

---

## Funcionalidades principales

### Inventario
- Agregar, editar y eliminar productos
- Busqueda por nombre, marca o codigo de barras
- Filtro por categoria con actualizacion automatica
- Alertas visuales de stock bajo
- Productos con stock critico aparecen primero en la lista
- Agregar stock desde boton dedicado o escaner movil

### Escaner Movil
- Generacion de QR para acceso desde celular
- Escaneo de codigos de barras via camara
- Si el producto existe, suma stock automaticamente
- Si el producto no existe, abre formulario de registro
- Creacion de categorias desde el escaner sin salir del flujo
- Nota: para una lectura correcta, apuntar la camara con las barras en posicion vertical

### Ventas
- Carrito de compras con multiples productos
- Busqueda de productos por nombre, marca o codigo
- Calculo automatico de subtotal y total
- Validacion de stock antes de confirmar
- Descuento automatico de stock al confirmar venta

### Historial de Ventas
- Registro de todas las ventas realizadas
- Detalle por transaccion con productos, cantidades y precios
- Fecha y hora en zona horaria de Chile

### Categorias
- Crear, editar y eliminar categorias
- Contador de productos por categoria
- Creacion rapida desde el formulario de producto

---

## Autor

**Joaquin Mella**

GitHub: https://github.com/MorteAeterna

---

## Licencia

Este proyecto esta bajo la licencia MIT.
