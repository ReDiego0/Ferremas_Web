from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
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

@require_POST
def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})  # Cambiado a dict

    if str(producto_id) in carrito:
        carrito[str(producto_id)] += 1  # Incrementa la cantidad si ya está en el carrito
    else:
        carrito[str(producto_id)] = 1  # Agrega el producto al carrito
    
    request.session['carrito'] = carrito  # Guarda el carrito en la sesión
    request.session.modified = True
    return redirect('productos')  # Redirige a la lista de productos o a otra vista deseada

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())
    carrito_items = []

    for producto in productos:
        cantidad = carrito[str(producto.id)]
        subtotal = producto.precio * cantidad
        carrito_items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    total = sum(item['subtotal'] for item in carrito_items)
    
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        del carrito[str(producto_id)]  # Elimina el producto del carrito
    
    request.session['carrito'] = carrito  # Guarda el carrito actualizado en la sesión
    return redirect('ver_carrito')  # Redirige a la vista del carrito
