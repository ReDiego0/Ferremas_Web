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
]