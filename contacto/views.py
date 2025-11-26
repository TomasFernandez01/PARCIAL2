from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            # Autocompletar si usuario está logueado (al guardar)
            if request.user.is_authenticated:
                mensaje.nombre = request.user.username
                mensaje.email = request.user.email
            mensaje.save()
            
            # Enviar email
            send_mail(
                subject=f'Nuevo mensaje de contacto de {mensaje.nombre}',
                message=f"""
                Nombre: {mensaje.nombre}
                Email: {mensaje.email}
                Mensaje: {mensaje.mensaje}
                
                Fecha: {mensaje.fecha_creacion}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            messages.success(request, '¡Mensaje enviado correctamente!')
            return redirect('contacto')
    else:
        # PRE-POBLAR el formulario en GET si usuario está logueado
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'nombre': request.user.username,
                'email': request.user.email
            }
        form = ContactoForm(initial=initial_data)
    
    return render(request, 'contacto/contacto.html', {'form': form})