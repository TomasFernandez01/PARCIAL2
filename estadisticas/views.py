from django.shortcuts import render
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import Visita
import json

def dashboard_view(request):
    # Filtro de fecha (últimos 7 días por defecto)
    fecha_filtro = request.GET.get('dias', '7')
    dias = int(fecha_filtro)
    
    fecha_desde = timezone.now() - timedelta(days=dias)
    
    # Estadísticas generales
    total_visitas = Visita.objects.filter(fecha__gte=fecha_desde).count()
    visitas_unicas = Visita.objects.filter(fecha__gte=fecha_desde).values('ip').distinct().count()
    usuarios_registrados = Visita.objects.filter(
        fecha__gte=fecha_desde, 
        usuario__isnull=False
    ).exclude(usuario='Anónimo').count()
    
    # Visitas por día (para gráfico de líneas)
    visitas_por_dia = Visita.objects.filter(
        fecha__gte=fecha_desde
    ).extra({
        'fecha_formateada': "DATE(fecha)"
    }).values('fecha_formateada').annotate(
        total=Count('id')
    ).order_by('fecha_formateada')
    
    # Preparar datos para Chart.js
    dias_labels = [visita['fecha_formateada'] for visita in visitas_por_dia]
    dias_data = [visita['total'] for visita in visitas_por_dia]
    
    # Páginas más visitadas (para gráfico de barras)
    paginas_populares = Visita.objects.filter(
        fecha__gte=fecha_desde
    ).values('pagina').annotate(
        total=Count('id')
    ).order_by('-total')[:10]
    
    paginas_labels = [pagina['pagina'].replace('/', '').title() or 'Home' for pagina in paginas_populares]
    paginas_data = [pagina['total'] for pagina in paginas_populares]
    
    # Visitas por usuario (para gráfico de dona)
    visitas_por_usuario = Visita.objects.filter(
        fecha__gte=fecha_desde
    ).values('usuario').annotate(
        total=Count('id')
    ).order_by('-total')
    
    usuarios_labels = [user['usuario'] for user in visitas_por_usuario]
    usuarios_data = [user['total'] for user in visitas_por_usuario]
    
    context = {
        'total_visitas': total_visitas,
        'visitas_unicas': visitas_unicas,
        'usuarios_registrados': usuarios_registrados,
        'dias_filtro': dias,
        
        # Datos para gráficos
        'dias_labels': json.dumps(dias_labels),
        'dias_data': json.dumps(dias_data),
        'paginas_labels': json.dumps(paginas_labels),
        'paginas_data': json.dumps(paginas_data),
        'usuarios_labels': json.dumps(usuarios_labels),
        'usuarios_data': json.dumps(usuarios_data),
    }
    
    return render(request, 'estadisticas/dashboard.html', context)