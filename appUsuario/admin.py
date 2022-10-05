from django.contrib import admin

from appUsuario.models import Usuario, Newsletter, Articulo, Avatar, ImagenArticulo
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Newsletter)
admin.site.register(Articulo)
admin.site.register(Avatar)
admin.site.register(ImagenArticulo)