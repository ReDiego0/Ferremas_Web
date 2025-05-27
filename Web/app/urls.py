from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.productos, name='productos'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]