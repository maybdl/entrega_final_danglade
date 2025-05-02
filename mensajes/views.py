from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Mensaje

@login_required
def bandeja(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha')
    return render(request, 'mensajes/bandeja.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    usuarios = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        destinatario_id = request.POST.get('destinatario')
        contenido = request.POST.get('contenido')
        if destinatario_id and contenido:
            destinatario = get_object_or_404(User, id=destinatario_id)
            Mensaje.objects.create(
                remitente=request.user,
                destinatario=destinatario,
                contenido=contenido
            )
            return redirect('mensajes:bandeja')
    return render(request, 'mensajes/enviar.html', {'usuarios': usuarios})
