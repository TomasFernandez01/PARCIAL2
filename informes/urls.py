from django.urls import path
from . import views

urlpatterns = [
    path('informes/', views.lista_reportes, name='lista_reportes'),
    path('informes/crear/', views.crear_reporte, name='crear_reporte'),
    path('informes/<int:id>/pdf/', views.generar_pdf, name='generar_pdf'),
    path('informes/<int:id>/editar/', views.editar_reporte, name='editar_reporte'),  
    path('informes/<int:id>/eliminar/', views.eliminar_reporte, name='eliminar_reporte'), 
]