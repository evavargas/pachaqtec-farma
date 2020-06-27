from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Client, Product, Invoice, Resume
<<<<<<< HEAD
=======

>>>>>>> a26aa9cd8dc08f683587785f0145dc1a731689e6


# Create your views here.
def home(request):
    return render(request, "forms/layout.html", {})
