from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=15, unique=True, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    points = models.FloatField(default=0)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["dni"]

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100, blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["product"]

    def __str__(self):
        return self.product


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    fecha = models.DateField(null=True, blank=True, default=timezone.now)
    products = models.ManyToManyField(Product, through="Resume")
    total = models.FloatField(default=0)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ["id"]

    def __str__(self):
        return (
            "Factura "
            + str(self.id)
            + " - "
            + self.client.name
            + " "
            + self.client.last_name
        )


class Resume(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = "Resumen"
        verbose_name_plural = "Resumenes"
        ordering = ["product"]

    def __str__(self):
        return f"Resumen {self.invoice} - {self.product} - {self.quantity} u."
