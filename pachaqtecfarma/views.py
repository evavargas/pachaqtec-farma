from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Client, Product, Invoice, Resume
from .forms import DNIForm, UserForm
from django.views.generic import ListView


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
            dni = form.cleaned_data["dni"]
            cliente = Client.objects.filter(dni=dni)
            return render(request, "cliente.html", {"cliente": cliente})

    else:
        form = DNIForm()

    return render(request, "forms/client_form.html", {"form": form})


def login(request):
    return render(request, "forms/signIn.html", {})
