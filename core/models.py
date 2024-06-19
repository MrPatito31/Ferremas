from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.cliente.first_name+" "+str(self.fecha)
    
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    despacho = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)+" "+self.producto.nombre+" "+str(self.venta.id)