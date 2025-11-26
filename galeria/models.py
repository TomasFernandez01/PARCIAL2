from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    imagen = models.ImageField(upload_to='fotos/', verbose_name="Imagen")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        ordering = ['-fecha_subida']