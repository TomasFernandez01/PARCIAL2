from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    imagen = models.CharField(max_length=255, blank=True, verbose_name="URL de imagen")  # Para imágenes placeholder
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"