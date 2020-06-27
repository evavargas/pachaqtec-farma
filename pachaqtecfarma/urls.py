from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("verificar-dni",views.dni_verification, name="verificar-dni")
    ]

