from curses import ACS_VLINE
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('index', MainPage.as_view(), name="index"),
  # path('collections', CollectionsPage.as_view(), name="collections")
]
