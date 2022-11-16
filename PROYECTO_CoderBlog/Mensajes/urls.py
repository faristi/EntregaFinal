from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView

urlpatterns = [

    path("enviar_mensaje/", views.enviar_mensaje, name="enviar_mensaje"),
    path("mostrar_mensajes/", views.mostrar_mensajes, name="mostrar_mensajes"),

]