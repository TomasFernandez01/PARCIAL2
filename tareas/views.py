from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tarea
from .forms import TareaForm

# Listar tareas
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

# Crear tarea
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            
            # Asi si quiero que se muestre quien creo la tarea
            #tarea = form.save(commit=False)
            #if request.user.is_authenticated:
            #    tarea.usuario = request.user  # ← Asignar usuario
            #tarea.save()

            form.save()
            messages.success(request, '¡Tarea creada exitosamente!')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'tareas/crear_tarea.html', {'form': form})

# Editar tarea
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tarea actualizada exitosamente!')
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})

# Eliminar tarea
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, '¡Tarea eliminada exitosamente!')
        return redirect('lista_tareas')
    
    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})