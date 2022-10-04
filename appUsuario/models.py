from email.mime import image
from django.db import models
from django.contrib.auth.models import User

class Moto(models.Model):
    marca = models.CharField(max_length=128)
    modelo = models.CharField(max_length=128)
    cilindrada = models.IntegerField()
    def __str__(self):
        return f'{self.marca}, {self.modelo}'

class Articulo(models.Model):
    titulo = models.CharField(max_length=64)
    subtitulo = models.CharField(max_length=64)
    fecha_publicada = models.DateField()
    texto = models.TextField(max_length=1000)
    usuario = User.first_name
    def __str__(self):
        return f'{self.fecha_publicada} - {self.titulo}'

class Newsletter(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    contacto = models.BooleanField()
    def __str__(self):
        return f'{self.apellido}, {self.nombre}. Quiere suscribirse? {self.contacto}'


class Avatar(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"    