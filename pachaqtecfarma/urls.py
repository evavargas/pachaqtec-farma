from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ver_productos, CreateInvoice, ver_facturas
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.home, name="index"),
    path("login", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("listar-producto", login_required(ver_productos.as_view()), name="list.product"),
    path("verificar-dni", views.dni_verification, name="verificar-dni"),
    path('crear-factura', login_required(CreateInvoice.as_view()), name='create_invoice'),
    path('llenar-factura/<int:invoice_id>', login_required(views.llenar_factura), name='llenar_factura'),
    path('agregar-a-factura/<int:invoice_id>', login_required(views.agregar_factura), name='agregar_factura'),
    path('cerrar-factura/<int:invoice_id>', login_required(views.cerrar_factura), name='cerrar_factura'),
    path('ver-factura/<int:invoice_id>', login_required(views.ver_factura), name='ver_factura'),
    path("ver-facturas", login_required(ver_facturas.as_view()), name="list.invoices"),
]

