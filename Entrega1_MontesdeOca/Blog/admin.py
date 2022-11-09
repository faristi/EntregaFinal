from django.contrib import admin
from Blog.models import Articulo, ImagenArticulo

# Register your models here.

admin.site.register(Articulo)
admin.site.register(ImagenArticulo)

#admin.site.register(Autor)              #Borrar o cambiar por Perfil
