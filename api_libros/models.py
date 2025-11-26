from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    anio = models.IntegerField(verbose_name="Año de publicación")
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio})"
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['-anio', 'titulo']