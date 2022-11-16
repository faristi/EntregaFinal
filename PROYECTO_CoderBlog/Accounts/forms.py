from django.forms import ModelForm
from .models import Avatar, Info
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class AvatarForm(ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Avatar
        fields = ["imagen"]

class InfoForm(ModelForm):
    descripcion = forms.CharField(label="Ingresar Desciripción")
    link_url = forms.URLField(label="URL a Biografía")
    
    class Meta:
        model = Info
        fields = ["descripcion", "link_url"]

class UserEditionForm(UserChangeForm):
    email = forms.EmailField(label="Modificar email")
    first_name = forms.CharField(label="Primer Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        # help_texts = {k: "" for k in fields}