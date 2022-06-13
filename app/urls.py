from django.urls import path
from .views import *

urlpatterns = [
  path('index', MainPage.as_view(), name="index"),
]
