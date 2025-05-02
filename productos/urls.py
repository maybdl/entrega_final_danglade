from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista'),
    path('crear/', views.crear_producto, name='crear'),
    path('categoria/<int:categoria_id>/', views.lista_productos_por_categoria, name='por_categoria'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('editar/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('categoria/editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categoria/eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),





]

