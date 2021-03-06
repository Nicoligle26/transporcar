from django.db import models

# Create your models here.


class User (models.Model):
    documento = models.CharField(max_length=10)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)

    def __str__(self):
        return self.nombres+" "+self.apellidos+" "+self.documento


class Conductor (models.Model):
    documento = models.CharField(max_length=10)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)
    licencia = models.CharField(max_length=45)
    salario = models.DecimalField(
        max_digits=15, decimal_places=2)  # 15 entero, 4 decimales

    def __str__(self):
        return self.documento+" "+self.apellidos+" "+self.nombres
