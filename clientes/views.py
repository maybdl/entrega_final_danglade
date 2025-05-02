from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView 
#UpdateView
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from .forms import CustomUserForm, PerfilForm
from django.contrib import messages
from .forms import PerfilForm
from .models import Perfil

def about(request):
    return render(request, 'clientes/about.html')

# Página de inicio
@login_required
def inicio(request):
    return render(request, 'clientes/inicio.html')

# Registro de usuarios
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'clientes/signup.html'
    success_url = reverse_lazy('clientes:login')

# Login de usuarios
class UserLoginView(LoginView):
    template_name = 'clientes/login.html'
    authentication_form = AuthenticationForm

# Cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('clientes:login')

# Ver perfil

@login_required
def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'clientes/ver_perfil.html', {
        'usuario': request.user,
        'perfil': perfil
    })


# Edición del perfil personalizado


@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = CustomUserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "✅ Perfil actualizado con éxito.")
            return redirect('clientes:ver_perfil')
    else:
        user_form = CustomUserForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    return render(request, 'clientes/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })


