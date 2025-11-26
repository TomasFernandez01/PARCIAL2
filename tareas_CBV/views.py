from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Tarea
from .forms import TareaForm

# Lista todas las tareas
class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas_cbv/lista_tareas.html'
    context_object_name = 'tareas'
    ordering = ['-fecha_creacion']

# Detalle de una tarea
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas_cbv/detalle_tarea.html'
    context_object_name = 'tarea'

# Crear nueva tarea
class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas_cbv/crear_tarea.html'
    success_url = reverse_lazy('lista_tareas_cbv')

# Editar tarea existente
class TareaUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas_cbv/editar_tarea.html'
    success_url = reverse_lazy('lista_tareas_cbv')

# Eliminar tarea
class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas_cbv/eliminar_tarea.html'
    success_url = reverse_lazy('lista_tareas_cbv')
    context_object_name = 'tarea'