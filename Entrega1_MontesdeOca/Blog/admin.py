from django.contrib import admin
from Blog.models import Articulo, ImagenArticulo, Avatar, Info

# Register your models here.

admin.site.register(Articulo)
admin.site.register(ImagenArticulo)
admin.site.register(Avatar)
admin.site.register(Info)
