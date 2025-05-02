from django import forms
from django.contrib.auth.models import User
from .models import Perfil


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['direccion', 'codigo_postal', 'telefono']