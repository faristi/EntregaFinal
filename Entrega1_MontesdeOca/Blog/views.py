
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .forms import ImagenArticuloForm, UserEditionForm, AvatarForm, InfoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Articulo, Avatar, Info
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return render(request, "Blog/home.html")

def about(request):
    return render (request, "Blog/about.html")

def signupuser(request):
    if request.method == 'GET':
        return render(request, "Blog/signupuser.html",{'form':UserCreationForm()})
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect("/")
            except IntegrityError:
                return render(request, 'Blog/signupuser.html', {'form':UserCreationForm(), 'error': "username alredy taken, select a new one"})
        else: #mismatch password
            return render(request, 'Blog/signupuser.html', {'form':UserCreationForm(), 'error': "passwords did not match"})

@login_required
def ver_perfil(request):
    user = request.user
    avatar_user = Avatar.objects.filter(user=request.user).first()
    info_user = Info.objects.filter(user=request.user).first()
    if avatar_user is not None:
        avatar_user_url = avatar_user.imagen.url
        tiene_avatar = True
    else:
        avatar_user_url = "/media/avatares/png-default-avatar-2.png"
        tiene_avatar = False
    if info_user is not None:
        descripcion = info_user.descripcion
        link_url = info_user.link_url
        tiene_info = True
    else:
        descripcion = "Agregue su Descripción en Editar Perfil"
        link_url = "Agregue su URL en Editar Perfil"
        tiene_info = False
    return render(request, "Blog/ver_perfil.html", {'user':user, 'avatar_user':avatar_user_url, 'tiene_avatar':tiene_avatar, 'descripcion':descripcion, 'link_url':link_url, 'tiene_info':tiene_info})

@login_required
def editar_perfil(request):
    user = request.user
    info = Info.objects.filter(user=request.user).first()
    if request.method != "POST":
        form_user = UserEditionForm(initial={"email": user.email, "first_name": user.first_name, "last_name": user.last_name})
        if info is not None:
            form_info = InfoForm(initial={"descripcion": info.descripcion, "link_url": info.link_url})
        else:
            form_info = InfoForm(initial={"descripcion": "Sin descripcion"})
    else:
        form_user = UserEditionForm(request.POST)
        form_info = InfoForm(request.POST)
        
        if form_user.is_valid() and form_info.is_valid():
            data_user = form_user.cleaned_data
            user.email = data_user["email"]
            user.first_name = data_user["first_name"]
            user.last_name = data_user["last_name"]
            user.save()
            Info.objects.filter(user=request.user).delete()
            form_info.instance.user = request.user
            form_info.save()
            return render(request, "Blog/home.html")

    contexto = {
        "user": user,
        "form_user": form_user,
        "form_info": form_info,
    }
    return render(request, "Blog/editar_perfil.html", contexto)

def loginuser(request):
    if request.method == 'GET': 
        return render(request, 'Blog/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username =request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'Blog/loginuser.html', {'form':AuthenticationForm(), 'error': "username and password did not match"})
        else:
            login(request, user)
            return redirect('/')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

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

@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.instance.user = request.user
            form.save()
            return render(request, "Blog/avatar_agregado.html")

    contexto = {"form": form}
    return render(request, "BLog/agregar_avatar.html", contexto)

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
    success_url = "/articulo/list"
    fields = ['titulo', 'subtitulo', 'texto', 'fecha', 'imagen']

class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = "/articulo/list"

class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = "/articulo/list"
    fields = ['titulo', 'subtitulo', 'texto', 'fecha', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

