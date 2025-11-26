from django.db import models

class Visita(models.Model):
    pagina = models.CharField(max_length=200, verbose_name="Página visitada")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de visita")
    usuario = models.CharField(max_length=100, blank=True, verbose_name="Usuario")
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="Dirección IP")
    
    def __str__(self):
        return f"{self.pagina} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        ordering = ['-fecha']