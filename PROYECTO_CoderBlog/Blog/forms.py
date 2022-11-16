from django.forms import ModelForm
from .models import ImagenArticulo
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class ImagenArticuloForm(ModelForm):
    class Meta:
        model = ImagenArticulo
        fields = ["nombre", "imagen"]



