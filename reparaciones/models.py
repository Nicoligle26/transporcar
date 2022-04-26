from django.db import models

from vehiculos.models import Vehiculo

# Create your models here.

class Reparacion (models.Model):
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=15, decimal_places=2)
    descripcion = models.CharField(max_length=80)
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.fecha)+" "+str(self.costo)+" "+self.descripcion

class Servicio (models.Model):
    descripcion = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.descripcion+" "+str(self.precio)

class Detalle(models.Model):
    costo=models.DecimalField(max_digits=15,decimal_places=0)
    cantidad=models.IntegerField(default=1)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE,null=True,blank=True)
    reparacion=models.ForeignKey(Reparacion,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.costo)+" "+str(self.cantidad)