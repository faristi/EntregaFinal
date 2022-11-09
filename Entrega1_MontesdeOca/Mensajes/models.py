from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model): 

    remitente=models.CharField(max_length=40)
    destinatario=models.ForeignKey(User, on_delete=models.CASCADE)
    camada=models.IntegerField() 