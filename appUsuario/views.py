import email
from urllib import request
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from appUsuario.forms import UsuarioFormulario, ArticuloFormulario, NewsletterFormulario, UserCreationForm, UserRegisterForm
from appUsuario.models import Usuario, Articulo, Newsletter
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView



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

@login_required
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

def editar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == 'POST':
        formulario = ArticuloFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data['titulo']
            articulo.fecha_publicada = data['fecha_publicada']
            articulo.texto = data['texto']
            articulo.save()
            return redirect(reverse('inicio'))
    else:
        inicial = {
            'titulo':articulo.titulo,
            'fecha_publicada': articulo.fecha_publicada,
            'texto': articulo.texto,
        }
        formulario = ArticuloFormulario(initial=inicial)
    return render(request,'appUsuario/crear_post_form.html',{"formulario": formulario})

def ver_articulo(request, id):
    articulo = Articulo.objects.get(id=id)    
    return render(request, 'appUsuario/ver_articulo.html',{"articulo": articulo})


#LOGIN, LOGOUT Y MAS // Por hacer: que muestre los mensajes y redirija a la principal correctamente ERIK 
def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm (request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return render(request, 'appUsuario/index.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'appUsuario/index.html', {"mensaje": "Error datos incorrectos"})

        else:

                return render(request, 'appUsuario/index.html', {"mensaje": "Error formulario erroneo"})
    form = AuthenticationForm()

    return render(request, 'appUsuario/login.html', {"form": form})


def register(request): #Por hacer: que muestre los mensajes y redirija a la principal correctamente ERIK 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 

        if form.is_valid():
            username = form.cleaned_data['username'] 
            form.save() 
            return render(request, 'appUsuario/index.html', {"mensaje": "Usuario Creado :D"})
    else:
        form = UserRegisterForm() 
    
    return render(request, "appUsuario/register.html", {"form":form})

class CustomLogoutView(LogoutView):
    template_name = 'appUsuario/logout.html'
    next_page = reverse_lazy('logout')

def nosotros(request):
    return render(request, 'appUsuario/about.html')


