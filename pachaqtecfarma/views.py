from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Client, Product, Invoice, Resume
<<<<<<< HEAD
from django.views.generic import (
    ListView, TemplateView
)


# Create your views here.

def home(request):
<<<<<<< HEAD
    return render(request, "pachaqtecfarma/index.html", {})

class ListProducts(ListView):
    model = Product
    template_name = ''
    queryset = Product.objects.all()
    context_object_name= 'products'


=======
    return render(request, "forms/layout.html", {})
>>>>>>> 9c2677d12784f07d3fd868ede72b77b6c13cdeb2
