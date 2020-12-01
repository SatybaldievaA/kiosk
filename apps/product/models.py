from django.db import models
from django.contrib.auth import get_user_model
from apps.category.models import Category

User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    availability = models.BooleanField()
    price = models.DecimalField(
        max_digits=7, decimal_places=2
    )
    date_created = models.DateTimeField(auto_now_add=True)

    quantity = models.DecimalField(
        verbose_name="Quantity", max_digits=10, decimal_places=0
    )

    category = models.ForeignKey(
        Category, related_name='products',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, related_name='products', on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name


"""
ADD MULTIPLE IMAGE MODEL
"""