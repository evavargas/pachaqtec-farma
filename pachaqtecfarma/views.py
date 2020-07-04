from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Client, Product, Invoice, Resume
from .forms import DNIForm, InvoiceForm
from django.db.models import Sum, F
from django.urls import reverse_lazy, reverse


# Create your views here.
class ver_productos(ListView):
    model = Product
    template_name = "forms/list_products.html"
    queryset = Product.objects.all()
    context_object_name = "products"


class ver_facturas(ListView):
    model = Invoice
    template_name = "listar-facturas.html"
    queryset = Invoice.objects.all()
    context_object_name = "facturas"


def home(request):
    return render(request, "base.html", {})


def dni_verification(request):
    if request.method == "POST":
        form = DNIForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data["dni"]
            cliente = Client.objects.get(dni=dni)
            invoice = Invoice.objects.filter(client=cliente)
            product = Product.objects.all()
            return render(
                request,
                "cliente.html",
                {"cliente": cliente, "facturas": invoice, "productos": product,},
            )

    else:
        form = DNIForm()

    return render(request, "forms/client_form.html", {"form": form})


def login(request):
    return render(request, "forms/signIn.html", {})


class CreateInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = "forms/create_invoice.html"
    # success_url = reverse_lazy('farma:list.product')
    def get_success_url(self):
        # success_url = reverse_lazy("farma:llenar_factura", {"id": self.object.pk})
        # return success_url
        return reverse("farma:llenar_factura", kwargs={"invoice_id": self.object.id})


def llenar_factura(request, invoice_id=1):
    productos = Product.objects.filter(stock__gt=0)
    return render(
        request, "forms/crear-factura.html", {"id": invoice_id, "productos": productos}
    )


def agregar_factura(request, invoice_id=1):
    form = request.POST.copy()
    producto = Product.objects.get(pk=form.get("producto"))
    if int(producto.stock) >= int(form.get("cantidad")):
        producto.stock = int(producto.stock) - int(form.get("cantidad"))
        producto.save()
        resume = Resume.objects.create(
            invoice_id=invoice_id,
            product_id=form.get("producto"),
            quantity=form.get("cantidad"),
        )
        return render(
            request,
            "producto-agregado.html",
            {"id": invoice_id, "Mensaje": "PRODUCTO AGREGADO"},
        )
    else:
        return render(
            request,
            "producto-agregado.html",
            {"id": invoice_id, "Mensaje": "PRODUCTO NO AGREGADO: No hay stock"},
        )


def cerrar_factura(request, invoice_id=1):
    factura = Invoice.objects.get(pk=invoice_id)
    get_price(factura)
    add_points(factura)
    return redirect("farma:list.invoices")


def ver_factura(request, invoice_id=1):
    factura = Invoice.objects.get(pk=invoice_id)
    return render(request, "ver-factura.html", {"factura": factura})


def get_price(factura):
    factura.total = 0
    for entry in factura.resume_set.all():
        factura.total = factura.total + (entry.product.price * entry.quantity)
    factura.save()


def add_points(factura):
    puntos = factura.total / 10
    cliente = Client.objects.get(pk=factura.client.id)
    cliente.points = cliente.points + puntos
    cliente.save()

