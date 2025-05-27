from django.shortcuts import render, redirect
from app.models import Producto

def homepage(request):
    productos_carousel = Producto.objects.all()[:5]
    productos_destacados = Producto.objects.order_by('-id')[:6]

    return render(request, 'homepage.html', {
        'productos_carousel': productos_carousel,
        'productos_destacados': productos_destacados,
    })

def about(request):
    return render(request, 'about.html')

def redirect_homepage(request):
    return redirect('homepage')
