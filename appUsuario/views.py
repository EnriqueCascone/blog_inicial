from django.shortcuts import render

def inicio(request):
    return render(request, 'appUsuario/index.html')

def crear_usuarios(request):
    return render(request, 'appUsuario/crearusuarios.html')

def usuarios(request):
    return render(request, 'appUsuario/usuarios.html')

def crear_post(request):
    return render(request, 'appUsuario/crear_post.html')

def posteos(request):
    return render(request, 'appUsuario/posteos.html')

def contacto(request):
    return render(request, 'appUsuario/contacto.html')