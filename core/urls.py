from django.urls import path
from .views import *

urlpatterns = [
    path('', catalogo),
    path('carro', carro),
    path('login', login),
]
