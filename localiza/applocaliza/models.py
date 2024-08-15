from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.nombre

class empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    puesto = models.CharField(max_length=20)

    def __str__(self):
        return self.puesto

class reserva(models.Model):
    fecha_de_entrega = models.DateField()
    fecha_de_devolucion = models.DateField()
       

class Vehiculo(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria

