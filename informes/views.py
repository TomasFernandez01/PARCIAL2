from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from django.contrib import messages
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from .models import Reporte
from .forms import ReporteForm

# Listar reportes
def lista_reportes(request):
    reportes = Reporte.objects.all()
    return render(request, 'informes/lista_reportes.html', {'reportes': reportes})

# Crear reporte
def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Reporte creado exitosamente!')
            return redirect('lista_reportes')
    else:
        form = ReporteForm()
    
    return render(request, 'informes/crear_reporte.html', {'form': form})

# Generar PDF - ¡CON REPORTLAB!
def generar_pdf(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    
    # Crear buffer para el PDF
    buffer = io.BytesIO()
    
    # Crear el objeto PDF
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Configurar estilos
    p.setFont("Helvetica-Bold", 16)
    p.drawString(1 * inch, height - 1 * inch, f"Reporte: {reporte.nombre}")
    
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, height - 1.5 * inch, f"Fecha: {reporte.fecha.strftime('%d/%m/%Y %H:%M')}")
    
    # Línea separadora
    p.line(1 * inch, height - 1.7 * inch, 7.5 * inch, height - 1.7 * inch)
    
    # Contenido del reporte
    p.setFont("Helvetica", 11)
    y_position = height - 2 * inch
    
    # Dividir el contenido en líneas
    lines = reporte.contenido.split('\n')
    for line in lines:
        if y_position < 1 * inch:  # Si queda poco espacio, nueva página
            p.showPage()
            p.setFont("Helvetica", 11)
            y_position = height - 1 * inch
        
        # Dividir líneas largas
        words = line.split()
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            if p.stringWidth(test_line, "Helvetica", 11) < 6.5 * inch:
                current_line.append(word)
            else:
                if current_line:
                    p.drawString(1 * inch, y_position, ' '.join(current_line))
                    y_position -= 0.2 * inch
                current_line = [word]
        
        if current_line:
            p.drawString(1 * inch, y_position, ' '.join(current_line))
            y_position -= 0.2 * inch
        
        y_position -= 0.1 * inch  # Espacio entre párrafos
    
    # Finalizar PDF
    p.showPage()
    p.save()
    
    # Preparar respuesta
    buffer.seek(0)
    return FileResponse(
        buffer, 
        as_attachment=True, 
        filename=f'reporte_{reporte.nombre}_{reporte.fecha.strftime("%Y%m%d")}.pdf'
    )

def eliminar_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    if request.method == 'POST':
        reporte.delete()
        messages.success(request, '¡Reporte eliminado!')
        return redirect('lista_reportes')
    return render(request, 'informes/eliminar_reporte.html', {'reporte': reporte})

def editar_reporte(request, id):
    reporte = get_object_or_404(Reporte, id=id)
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Reporte actualizado!')
            return redirect('lista_reportes')
    else:
        form = ReporteForm(instance=reporte)
    return render(request, 'informes/editar_reporte.html', {'form': form})