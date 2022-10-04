from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        