
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .forms import ImagenArticuloForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Articulo
from Accounts.models import Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, "Blog/home.html")

def about(request):
    return render (request, "Blog/about.html")

@login_required
def agregar_imagen(request):
    if request.method != "POST":
        form = ImagenArticuloForm()
    else:
        form = ImagenArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "Blog/imagen_agregada.html")

    contexto = {"form": form}
    return render(request, "Blog/agregar_imagen.html", contexto)



############# Clases basadas en vistas para ver, editar y eliminar Articulos

class ArticuloList(ListView):
    model = Articulo
    template_name = "Blog/articulos_list.html"

class ArticuloDetalle(DetailView):
    model = Articulo
    template_name = "Blog/articulo_detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar_autor = Avatar.objects.filter(user__username=kwargs['object'].autor).first()
        if avatar_autor is not None:
            avatar_autor_url = avatar_autor.imagen.url
        else:
            avatar_autor_url = "/media/avatares/png-default-avatar-2.png"
        context['avatar_autor'] = avatar_autor_url
        return context

class ArticuloEdit(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = "/pages"
    fields = ['titulo', 'subtitulo', 'texto', 'fecha', 'imagen']

class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = "/pages"

class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = "/pages"
    fields = ['titulo', 'subtitulo', 'texto', 'fecha', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

