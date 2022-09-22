import email
from urllib import request
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from appUsuario.forms import UsuarioFormulario, ArticuloFormulario, NewsletterFormulario
from appUsuario.models import Usuario, Articulo, Newsletter

def inicio(request):
    articulos = Articulo.objects.all()
    contexto = {"articulos": articulos}
    borrado = request.GET.get('borrado', None)
    contexto['borrado'] = borrado
    return render(request, 'appUsuario/index.html', contexto)
    # return render(request, 'appUsuario/index.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "appUsuario/usuarios.html", {'usuarios': usuarios})
    
def crear_post(request):
    return render(request, 'appUsuario/crear_post_form.html')

def posteos(request):
    return render(request, 'appUsuario/posteos.html')

def contacto(request):
    return render(request, 'appUsuario/contacto_form.html')

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
    usuarios = Usuario.objects.all()
    return render(request, 'appUsuario/busquedaUsuario.html', {"usuarios": usuarios})

def buscar_usuario(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
        return render(request, "appUsuario/busquedaUsuario.html", {'usuarios': usuarios})
    else: 
        return render(request, "appUsuario/busquedaUsuario.html", {'usuarios': []})


#Desde el formulario de publicacion
def crear_post(request):
    if request.method == 'POST':
        formulario = ArticuloFormulario(request.POST)
        if formulario.is_valid(): #Se corrobora que el formulario sea válido según los datos de forms.py
            data = formulario.cleaned_data
            articulo = Articulo(titulo = data["titulo"], fecha_publicada=data["fecha_publicada"],texto=data["texto"])
            articulo.save()
            return render(request, 'appUsuario/crear_post_form.html',{"exitoart": True})
    else:
        formulario = ArticuloFormulario()
    return render(request,'appUsuario/crear_post_form.html',{"formulario": formulario})


#Desde el formulario de Contacto
def suscripcion_newsletter(request): 
    if request.method =="POST":
        formulario = NewsletterFormulario(request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            newsletter = Newsletter(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],contacto=data["contacto"])
            newsletter.save()
            return render(request,'appUsuario/index.html',{"exitonew": True})
        else:
            formulario=NewsletterFormulario()
        return render(request, 'appUsuario/contacto_form.html',{"formulario": formulario})

def eliminarArticulo(request, id):
    articulo = Articulo.objects.get(id=id)
    borrado_id = articulo.id
    articulo.delete()
    url = f"{reverse('inicio')}?borrado={borrado_id}" #Es como usar la etiqueta de URL en el html
    return redirect(url)