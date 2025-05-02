from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from .models import Orden, ItemOrden
from django.contrib import messages

@login_required
def ver_carrito(request):
    # Obtener o crear el carrito (orden no completada) del usuario
    orden, created = Orden.objects.get_or_create(user=request.user, completado=False)

    # Calcular total en pesos y total de ítems
    total = sum(item.producto.precio * item.cantidad for item in orden.items.all())
    total_items = sum(item.cantidad for item in orden.items.all())

    return render(request, 'ordenes/carrito.html', {
        'orden': orden,
        'total': total,
        'total_items': total_items
    })

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    orden, created = Orden.objects.get_or_create(user=request.user, completado=False)

    item, created = ItemOrden.objects.get_or_create(orden=orden, producto=producto)
    if not created:
        item.cantidad += 1
    item.save()

    return redirect('ordenes:ver_carrito')

@login_required
def quitar_del_carrito(request, item_id):
    item = get_object_or_404(ItemOrden, id=item_id)
    if item.orden.user == request.user:
        item.delete()
    return redirect('ordenes:ver_carrito')

@login_required
def modificar_cantidad(request, item_id):
    item = get_object_or_404(ItemOrden, id=item_id)
    if item.orden.user != request.user:
        return redirect('ordenes:ver_carrito')

    if request.method == 'POST':
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        if nueva_cantidad > 0:
            item.cantidad = nueva_cantidad
            item.save()
        else:
            item.delete()

    return redirect('ordenes:ver_carrito')


@login_required
def finalizar_compra(request):
    orden = get_object_or_404(Orden, user=request.user, completado=False)

    if orden.items.exists():
        orden.completado = True
        orden.save()
        messages.success(request, "🧾 ¡Compra finalizada con éxito!")
    else:
        messages.warning(request, "Tu carrito está vacío.")

    return redirect('ordenes:ver_carrito')

@login_required
def historial_compras(request):
    ordenes = Orden.objects.filter(user=request.user, completado=True).order_by('-creado')

    return render(request, 'ordenes/historial.html', {
        'ordenes': ordenes
    })

