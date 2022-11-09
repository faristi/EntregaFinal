from django.contrib import admin
from Blog.models import Articulo, Autor, ImagenArticulo

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Autor)              #Borrar o cambiar por Perfil
admin.site.register(ImagenArticulo)
