from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Articulo(models.Model):
    titulo = models.CharField(max_length=64)
    fecha_publicada = models.DateField()
    texto = models.TextField(max_length=1000)
    def __str__(self):
        return f'{self.fecha_publicada} - {self.titulo}'

class Newsletter(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    contacto = models.BooleanField()
    def __str__(self):
        return f'{self.apellido}, {self.nombre}. Quiere suscribirse? {self.contacto}'
