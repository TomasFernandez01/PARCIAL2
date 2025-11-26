from django.db import models
# from django.contrib.auth.models import User

class Tarea(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    completada = models.BooleanField(default=False, verbose_name="Completada")
    
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # ← NUEVO

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-fecha_creacion']