from django.urls import path
from appUsuario import views

urlpatterns = [
path('', views.inicio, name="inicio"),
path('crear_usuario/', views.crear_usuarios, name="crear_usuario"),
path('usuarios/', views.usuarios, name="usuarios"),
path('crear_post/', views.crear_post, name="crear_post"),
path('posteos/', views.posteos, name="posteos"),
path('contacto/', views.contacto, name="contacto"),
]