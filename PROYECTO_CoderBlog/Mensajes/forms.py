from django.forms import ModelForm
from .models import Mensaje
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = ["destinatario", "texto"]