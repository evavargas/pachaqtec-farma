from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
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


def home(request):
    return render(request, "base.html", {})


def dni_verification(request):
    if request.method == "POST":
        form = DNIForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            cliente=Client.objects.get(dni=dni)
            invoice=Invoice.objects.filter(client=cliente)
            return render(request, 'cliente.html', {'cliente': cliente,'facturas':invoice})

    else:
        form = DNIForm()

    return render(request, "forms/client_form.html", {"form": form})


def login(request):
    return render(request, "forms/signIn.html", {})

class CreateInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'forms/create_invoice.html'
    #success_url = reverse_lazy('farma:list.product')
    def get_success_url(self):
        #success_url = reverse_lazy("farma:llenar_factura", {"id": self.object.pk})
        #return success_url
        return reverse('farma:llenar_factura', kwargs={'invoice_id': self.object.id})


def llenar_factura(request,invoice_id=1):
    productos = Product.objects.all()
    return render(request, "crear-factura.html", {"id":invoice_id,"productos":productos})

