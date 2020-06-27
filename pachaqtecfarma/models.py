from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=15, unique=True, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    points = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["dni"]

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100, blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["product"]

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    fecha = models.DateField(null=True, blank=True, default=timezone.now)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ["id"]


