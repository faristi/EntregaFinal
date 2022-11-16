from django.db import models
from django.contrib.auth.models import User


class ImagenArticulo(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=60)
    texto = models.TextField()
    fecha = models.DateField(null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ForeignKey(ImagenArticulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo