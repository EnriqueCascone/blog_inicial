import email
from urllib import request
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from appUsuario.forms import UsuarioFormulario
from appUsuario.models import Usuario, Articulo, Newsletter

def inicio(request):
    return render(request, 'appUsuario/index.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "appUsuario/usuarios.html", {'usuarios': usuarios})
    
def crear_post(request):
    return render(request, 'appUsuario/crear_post.html')

def posteos(request):
    return render(request, 'appUsuario/posteos.html')

def contacto(request):
    return render(request, 'appUsuario/contacto.html')

def crear_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = Usuario(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            usuario.save()
            return render(request, "appUsuario/index.html", {"exitoso": True})
    else: 
        formulario = UsuarioFormulario()  
    return render(request, "appUsuario/form_usuarios.html", {"formulario": formulario})


def busquedaUsuario(request):
    return render(request, 'appUsuario/busquedaUsuario.html')

def buscar_usuario(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        return render(request, "appUsuario/usuarios.html", {'usuarios': usuarios})
    else: 
        return render(request, "appUsuario/usuarios.html", {'usuarios': []})
        
        
    
        

    
