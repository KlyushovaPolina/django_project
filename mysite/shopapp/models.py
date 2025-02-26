from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default = 0, max_digits=8, decimal_places = 2) #поле для работы с деньгами (дробная часть считается отдельно, нет погрешности)
    discount = models.SmallIntegerField (default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

class Order(models.Model):
    delivery_address = models.TextField(null=False, blank = True)
    promocode = models.CharField(max_length=20, null = False, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, "orders")