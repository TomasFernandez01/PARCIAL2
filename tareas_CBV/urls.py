from django.urls import path
from . import views

urlpatterns = [
    path('tareas-cbv/', views.TareaListView.as_view(), name='lista_tareas_cbv'),
    path('tareas-cbv/<int:pk>/', views.TareaDetailView.as_view(), name='detalle_tarea_cbv'),
    path('tareas-cbv/crear/', views.TareaCreateView.as_view(), name='crear_tarea_cbv'),
    path('tareas-cbv/<int:pk>/editar/', views.TareaUpdateView.as_view(), name='editar_tarea_cbv'),
    path('tareas-cbv/<int:pk>/eliminar/', views.TareaDeleteView.as_view(), name='eliminar_tarea_cbv'),
]