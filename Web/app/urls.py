from django.urls import path
from . import views

urlpatterns = [
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.productos, name='productos'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]