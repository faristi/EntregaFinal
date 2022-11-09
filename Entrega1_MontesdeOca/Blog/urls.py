from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),

    path('articulo/list', views.ArticuloList.as_view(), name='listArticulos'),
    path('articulo/<pk>', views.ArticuloDetalle.as_view(), name='verArticulo'),
    path('editar/<pk>', views.ArticuloEdit.as_view(), name='editarArticulo'),
    path('borrar/<pk>', views.ArticuloDelete.as_view(), name='borrarArticulo'),
    path('nuevo/', views.ArticuloCreate.as_view(), name='nuevoArticulo'),

    path("agregarImagen", views.agregarImagen, name="agregarImagen"),
    path("editarPerfil", views.editar_perfil, name="editarPerfil"),
    path("verPerfil", views.ver_perfil, name="verPerfil"),

    #Authentication
    path('signup/', views.signupuser, name= 'signupuser'),
    path('logout/', LogoutView.as_view(template_name='Blog/logoutuser.html'), name= 'logoutuser'),
    path('login/', views.loginuser, name= 'loginuser'),

    #path('logout/', views.logoutuser, name= 'logoutuser'),
    # path("crearAutor", views.crearAutor, name="crearAutor"),
    # path("crearArticulo", views.crearArticulo, name="crearArticulo"),
    # path("articulos", views.articulos, name="articulos"),
    # path("crearLector", views.crearLector, name="crearLector"),
    # path("reseñas", views.reseñas, name="reseñas"),
    # path("crearReseña", views.crearReseña, name="crearReseña"),
    # path("buscar", views.buscar, name="buscar"),
]
