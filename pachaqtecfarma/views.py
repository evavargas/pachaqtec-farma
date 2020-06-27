from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Client, Product, Invoice, Resume
from django.views.generic import (
    ListView, TemplateView
)


# Create your views here.

def home(request):
    return render(request, "pachaqtecfarma/index.html", {})

class ListProducts(ListView):
    model = Product
    template_name = ''
    queryset = Product.objects.all()
    context_object_name= 'products'


