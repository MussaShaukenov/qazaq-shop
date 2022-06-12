from django.db import models

# Create your models here.
class ProductsModel(models.Model):
    product_name = models.CharField(max_length=64)
    product_price = models.FloatField
    
