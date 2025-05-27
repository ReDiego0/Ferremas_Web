from django.urls import path
from . import views

urlpatterns = [
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
]