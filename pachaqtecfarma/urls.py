from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ver_productos, CreateInvoice
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("login", views.login, name="login"),
    path("listar-producto", ver_productos.as_view(), name="list.product"),
    path("verificar-dni", views.dni_verification, name="verificar-dni"),
    path('crear-factura', CreateInvoice.as_view(), name='create_invoice'),
    path('llenar-factura/<int:invoice_id>', views.llenar_factura, name='llenar_factura'),
]

