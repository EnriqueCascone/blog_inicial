from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    email = forms.EmailField()
