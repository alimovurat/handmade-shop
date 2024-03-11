from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    count = models.IntegerField(default=0)
    attributes = models.JSONField()

