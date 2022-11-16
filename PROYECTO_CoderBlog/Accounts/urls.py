from django.urls import path
from . import views
from Blog.views import home
from django.contrib.auth.views import LogoutView, PasswordChangeView

urlpatterns = [

    path("agregar_avatar/", views.agregar_avatar, name="agregar_avatar"),
    path("accounts/profile/edit/", views.editar_perfil, name="editarPerfil"),
    path("accounts/profile/", views.ver_perfil, name="verPerfil"),

    #Authentication
    path('accounts/signup/', views.signupuser, name= 'signupuser'),
    path('logout/', LogoutView.as_view(template_name='Accounts/logoutuser.html'), name= 'logoutuser'),
    path('accounts/login/', views.loginuser, name= 'loginuser'),
    path('password/', PasswordChangeView.as_view(), name='password_change'),
    path("", home, name='password_change_done'),

]