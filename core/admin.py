from django.contrib import admin
from .models import Region, Comuna, Pregunta, Rol, Usuario, Direccion, Marca, Tipo_de_ropa, Producto, Detalle, Venta
# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Pregunta)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Direccion)
admin.site.register(Marca)
admin.site.register(Tipo_de_ropa)
admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(Venta)