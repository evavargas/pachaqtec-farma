from django import forms
from .models import Client, Product, Invoice, Resume


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["dni", "name", "last_name", "points"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product", "stock", "price"]


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ["client", "fecha", "products"]


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["product", "invoice", "quantity"]

class DNIForm(forms.Form):
    dni = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','id':'dni','placeholder':'Ingresa tu DNI'}))
