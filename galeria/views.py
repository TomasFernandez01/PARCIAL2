from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Foto
from .forms import FotoForm

def galeria_view(request):
    fotos = Foto.objects.all()
    return render(request, 'galeria/galeria.html', {'fotos': fotos})

def subir_foto_view(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Foto subida exitosamente!')
            return redirect('galeria')
    else:
        form = FotoForm()
    
    return render(request, 'galeria/subir_foto.html', {'form': form})