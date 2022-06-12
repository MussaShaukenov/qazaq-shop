from django.contrib import admin
from .models import ProductsModel, CompanyModel


admin.site.register(ProductsModel)
admin.site.register(CompanyModel)