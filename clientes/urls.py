from django.urls import path
from . import views
from .views import (
    UserRegisterView,
    UserLoginView,
    logout_view,
)

app_name = "clientes"

urlpatterns = [
    path('', views.inicio, name='inicio_clientes'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', views.editar_perfil, name='editar_perfil'),
    path('ver/', views.ver_perfil, name='ver_perfil'),
    path('about/', views.about, name='about'),



]
