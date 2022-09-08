from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()

class Articulo(models.Model):
    titulo = models.CharField(max_length=64)
    fecha_publicada = models.DateField()
    texto = models.TextField(max_length=1000)

class Newsletter(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    contacto = models.BooleanField()
