from django.db import models

class cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    puesto = models.CharField(max_length=20)

class reserva(models.Model):
    fecha_de_entrega = models.DateField()
    fecha_de_devolucion = models.DateField()
    
    

class vehiculo(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)

