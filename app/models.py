from tkinter import CASCADE
from django import db
from django.db import models


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=32)
    company_image = models.ImageField(upload_to="images")

    class Meta:
        db_table = "companies"
        verbose_name = "company"
        verbose_name_plural = "companies"
    
    def __str__(self) -> str:
        return self.company_name


class ProductsModel(models.Model):
    product_name = models.CharField(max_length=64)
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to="images")
    company_name = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self) -> str:
        return self.product_name

    
