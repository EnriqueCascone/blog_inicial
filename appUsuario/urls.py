from django.urls import path
from appUsuario import views

urlpatterns = [
path('', views.inicio, name="inicio"),
path('crear_usuario/', views.crear_usuario, name="crear_usuario"),
path('usuarios/', views.usuarios, name="usuarios"),
path('crear_post/', views.crear_post, name="crear_post"),
path('posteos/', views.posteos, name="posteos"),
path('contacto/', views.contacto, name="contacto"),
path('busquedaUsuario/', views.busquedaUsuario, name="busquedaUsuario"),
path('buscar_usuario/', views.buscar_usuario, name="buscar_usuario"),
path('eliminar_articulo/<int:id>', views.eliminarArticulo, name="eliminar_articulo"),
]