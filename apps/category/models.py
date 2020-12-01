from django.db import models

""" 
Creating class of categories for online shop: 
Piano => Digital pianos, Stage pianos, Classical pianos => Yamaha P series
"""


class Category(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(
        max_length=255, blank=True
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='child'
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        if self.parent:
            return f"{self.parent} --> {self.title}"
        return self.title
