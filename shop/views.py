from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto

# Lista de productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'shop/lista_productos.html', {'productos': productos})

# Ver carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    
    # Calcular total
    total = 0
    items_carrito = []
    
    for producto_id, cantidad in carrito.items():
        try:
            producto = Producto.objects.get(id=producto_id)
            subtotal = producto.precio * cantidad
            total += subtotal
            items_carrito.append({
                'producto': producto,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
        except Producto.DoesNotExist:
            # Si el producto no existe, lo removemos del carrito
            del carrito[producto_id]
            request.session['carrito'] = carrito
    
    return render(request, 'shop/carrito.html', {
        'items_carrito': items_carrito,
        'total': total
    })

# Agregar al carrito
def agregar_al_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    # Inicializar carrito si no existe
    if 'carrito' not in request.session:
        request.session['carrito'] = {}
    
    carrito = request.session['carrito']
    
    # Agregar producto al carrito
    producto_id = str(producto.id)
    if producto_id in carrito:
        carrito[producto_id] += 1
    else:
        carrito[producto_id] = 1
    
    request.session['carrito'] = carrito
    request.session.modified = True
    
    messages.success(request, f'¡{producto.nombre} agregado al carrito!')
    return redirect('lista_productos')

# Quitar del carrito
def quitar_del_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    carrito = request.session.get('carrito', {})
    producto_id = str(producto.id)
    
    if producto_id in carrito:
        if carrito[producto_id] > 1:
            carrito[producto_id] -= 1
        else:
            del carrito[producto_id]
        
        request.session['carrito'] = carrito
        request.session.modified = True
        
        messages.info(request, f'¡{producto.nombre} removido del carrito!')
    
    return redirect('ver_carrito')

# Vaciar carrito
def vaciar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
        messages.info(request, '¡Carrito vaciado!')
    
    return redirect('ver_carrito')

def sumar_al_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    carrito = request.session.get('carrito', {})
    producto_id = str(producto.id)
    
    if producto_id in carrito:
        carrito[producto_id] += 1
    else:
        carrito[producto_id] = 1
    
    request.session['carrito'] = carrito
    request.session.modified = True
    
    messages.success(request, f'¡+1 {producto.nombre} en el carrito!')
    return redirect('ver_carrito')