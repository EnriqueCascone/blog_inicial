from unittest.util import _MAX_LENGTH
from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    email = forms.EmailField()

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(max_length=64)
    fecha_publicada = forms.DateField()
    texto = forms.CharField(max_length=1000)

class NewsletterFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    email = forms.EmailField()
    contacto = forms.BooleanField()