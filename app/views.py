from pyexpat import model
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import CompanyModel, ProductsModel

class MainPage(ListView):
    template_name = "main_page.html"
    context_object_name = "products"
    model = ProductsModel