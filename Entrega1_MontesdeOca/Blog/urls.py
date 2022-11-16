from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),

    path('articulo/list', views.ArticuloList.as_view(), name='listArticulos'),
    path('articulo/<pk>', views.ArticuloDetalle.as_view(), name='verArticulo'),
    path('editar/<pk>', views.ArticuloEdit.as_view(), name='editarArticulo'),
    path('borrar/<pk>', views.ArticuloDelete.as_view(), name='borrarArticulo'),
    path('nuevo/', views.ArticuloCreate.as_view(), name='nuevoArticulo'),

    path("agregar_avatar", views.agregar_avatar, name="agregar_avatar"),
    path("agregar_imagen", views.agregar_imagen, name="agregar_imagen"),
    path("editarPerfil", views.editar_perfil, name="editarPerfil"),
    path("verPerfil", views.ver_perfil, name="verPerfil"),

    #Authentication
    path('signup/', views.signupuser, name= 'signupuser'),
    path('logout/', LogoutView.as_view(template_name='Blog/logoutuser.html'), name= 'logoutuser'),
    path('login/', views.loginuser, name= 'loginuser'),
    path('password/', PasswordChangeView.as_view(), name='password_change'),
    path("", views.home, name='password_change_done'),
]
