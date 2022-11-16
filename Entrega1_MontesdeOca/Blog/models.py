from django.db import models
from django.contrib.auth.models import User


class ImagenArticulo(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    link_url = models.URLField(max_length = 200)

class Articulo(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=60)
    texto = models.TextField()
    fecha = models.DateField(null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ForeignKey(ImagenArticulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo