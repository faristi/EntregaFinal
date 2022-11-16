from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

    path('pages/', views.ArticuloList.as_view(), name='listArticulos'),
    path('pages/<pk>', views.ArticuloDetalle.as_view(), name='verArticulo'),
    path('editar/<pk>', views.ArticuloEdit.as_view(), name='editarArticulo'),
    path('borrar/<pk>', views.ArticuloDelete.as_view(), name='borrarArticulo'),
    path('nuevo/', views.ArticuloCreate.as_view(), name='nuevoArticulo'),

    path("agregar_imagen/", views.agregar_imagen, name="agregar_imagen"),

]
