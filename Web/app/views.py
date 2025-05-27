from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductoForm
from .models import Producto

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregar_producto')  # Redirige a la misma página o a otra vista
    else:
        form = ProductoForm()
    
    return render(request, 'agregar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        producto.delete()
        return redirect('productos')  # Redirige a la lista de productos
    except Producto.DoesNotExist:
        return redirect('productos')  # Redirige a la lista de productos si no se encuentra el producto

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})
