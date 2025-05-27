from django.shortcuts import render, redirect
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

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


