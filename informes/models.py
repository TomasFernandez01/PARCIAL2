from django.db import models

class Reporte(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del reporte")
    contenido = models.TextField(verbose_name="Contenido")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        ordering = ['-fecha']