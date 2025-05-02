from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar'),
    path('quitar/<int:item_id>/', views.quitar_del_carrito, name='quitar'),
    path('modificar/<int:item_id>/', views.modificar_cantidad, name='modificar'),
    path('finalizar/', views.finalizar_compra, name='finalizar'),
    path('historial/', views.historial_compras, name='historial'),


]
