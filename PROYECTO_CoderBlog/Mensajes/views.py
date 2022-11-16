from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MensajeForm
from .models import Mensaje
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def enviar_mensaje(request):
    if request.method != "POST":
        form = MensajeForm()
    else:
        form = MensajeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.remitente = request.user.username
            form.save()
            return render(request, "Mensajes/mensaje_enviado.html")

    contexto = {"form": form}
    return render(request, "Mensajes/enviar_mensaje.html", contexto)

def mostrar_mensajes(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).all()
    return render(request, 'Mensajes/mostrar_mensajes.html', {'mensajes': mensajes})