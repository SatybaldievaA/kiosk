from django.db import models
from django.contrib.auth.models import User

from apps.product.models import Item

"""
creating class for order accumulation by customer,
only registered customers may use this function
"""


class Cart(models.Model):
    user = models.ForeignKey('auth.User', related_name="carts", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    items = models.ManyToManyField(Item)


class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey('auth.User', related_name="orders", on_delete=models.CASCADE)
