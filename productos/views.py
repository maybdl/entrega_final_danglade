from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .forms import ProductoForm
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from .forms import CategoriaForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


@user_passes_test(lambda u: u.is_staff)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Producto agregado con éxito.")

            if request.POST.get('accion') == 'lista':
                return redirect('productos:lista')
            else:
                form = ProductoForm()
    else:
        form = ProductoForm()
    return render(request, 'productos/crear.html', {'form': form})

def lista_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    else:
        productos = Producto.objects.all()

    categorias = Categoria.objects.all()

    return render(request, 'productos/lista.html', {
        'productos': productos,
        'categorias': categorias
    })

def lista_productos_por_categoria(request, categoria_id):
    productos = Producto.objects.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()
    categoria_actual = Categoria.objects.get(id=categoria_id)

    return render(request, 'productos/lista.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_actual': categoria_actual,
    })

@user_passes_test(lambda u: u.is_staff)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Categoría agregada con éxito.")
            if request.POST.get('accion') == 'lista':
                return redirect('productos:lista')
            else:
                form = CategoriaForm()
    else:
        form = CategoriaForm()
    return render(request, 'productos/crear_categoria.html', {'form': form})



class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria']
    template_name = 'productos/editar_producto.html'
    success_url = reverse_lazy('productos:lista')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('productos:lista')
        return super().dispatch(request, *args, **kwargs)
    


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('productos:lista')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('productos:lista')
        return super().dispatch(request, *args, **kwargs)
    
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'productos/editar_categoria.html'
    success_url = reverse_lazy('productos:lista')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('productos:lista')
        return super().dispatch(request, *args, **kwargs)


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'productos/eliminar_categoria.html'
    success_url = reverse_lazy('productos:lista')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('productos:lista')
        return super().dispatch(request, *args, **kwargs)

