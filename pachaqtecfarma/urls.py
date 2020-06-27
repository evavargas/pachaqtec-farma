from django.urls import path
from .views import ver_productos
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("login", views.login, name="login"),
    path("listar-producto", ver_productos.as_view(), name="list.product"),
    path("verificar-dni", views.dni_verification, name="verificar-dni"),
]

