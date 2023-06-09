from django.db import models

# Create your models here.
class Region(models.Model):
    IDRegion = models.AutoField(primary_key=True)
    nombreRegion = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.nombreRegion
    
class Comuna(models.Model):
    IDComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=20)
    costo_direccionComuna = models.IntegerField()
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreComuna

class Pregunta(models.Model):
    IDPreguntas = models.AutoField(primary_key=True)
    nombrePreguntas = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombrePregunta

class Rol(models.Model):
    IDRol = models.AutoField(primary_key=True)
    nombreRol = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreRol

class Usuario(models.Model):
    IDUsuario = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=20)
    apellidoUsuario = models.CharField(max_length=20)
    rutUsuario = models.IntegerField()
    fecha_creacion = models.DateField
    telefono = models.IntegerField()
    Correo = models.EmailField(max_length=20)
    clave = models.CharField (max_length=30)
    respuesta = models.CharField(max_length=30)
    Rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    Preguntas = models.ForeignKey(Pregunta,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreUsuaruo
    
    

class Direccion(models.Model):
    IDDireccion = models.AutoField(primary_key=True)
    nombreDireccion = models.CharField(max_length=20)
    N_de_Direccion = models.CharField(max_length=20)
    municipio = models.CharField(max_length=30) 
    nombre_municipio = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreDireccion

class Marca(models.Model):
    IDMarca = models.AutoField(primary_key=True)
    nombreMarca = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreMarca

class Tipo_de_ropa(models.Model):
    IDTipo_de_ropa = models.AutoField(primary_key=True)
    nombreTipo_de_ropa = models.CharField(max_length=20) 
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.nombreTipo_de_ropa

class Producto(models.Model):
    IDProducto = models.AutoField(primary_key=True) 
    nombreProducto = models.CharField(max_length=35)
    stock = models.IntegerField()
    talla = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)
    Precio = models.IntegerField()
    color = models.CharField(max_length=20)
    foto = models.ImageField(upload_to="PaginaWebb-django") 
    tipo_de_ropa = models.ForeignKey(Tipo_de_ropa,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreProducto
    
class Venta(models.Model):
    IDVenta = models.AutoField(primary_key=True)
    fecha_Venta = models.DateField
    total = models.IntegerField()
    fecha = models.DateField()
    fecha_despacho = models.DateField()
    estado = models.CharField(max_length=20)
    carrito = models.IntegerField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreVenta
    
class Detalle(models.Model):
    IDDetalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    sub_total = models.IntegerField()
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreDetalle




