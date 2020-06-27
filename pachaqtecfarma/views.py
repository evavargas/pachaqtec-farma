from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from .models import Client, Product, Invoice, Resume
from .forms import ComentarioForm


# Create your views here.
def home(request):
    return render(request, "pachaqtecfarma/index.html", {})
