from django import forms
from .models import Producto
from .models import Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip().lower()
        if Producto.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un producto con ese nombre.")
        return nombre

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip().lower()
        if Categoria.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Esta categoría ya existe.")
        return nombre
