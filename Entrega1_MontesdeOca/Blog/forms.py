from django.forms import ModelForm
from .models import Autor, Articulo, ImagenArticulo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "apellido", "profesion"]

class ImagenArticuloForm(ModelForm):
    class Meta:
        model = ImagenArticulo
        fields = ["nombre", "imagen"]

class UserEditionForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Primer Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        # help_texts = {k: "" for k in fields}



# class ArticuloForm(ModelForm):
#     class Meta:
#         model = Articulo
#         fields = ["titulo", "texto", "autor", "fecha"]