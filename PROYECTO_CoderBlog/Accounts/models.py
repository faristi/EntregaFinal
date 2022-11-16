from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    link_url = models.URLField(max_length = 200)