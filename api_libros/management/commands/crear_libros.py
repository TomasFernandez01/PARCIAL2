from django.core.management.base import BaseCommand
from api_libros.models import Libro

class Command(BaseCommand):
    help = 'Crea libros de prueba para la API'
    
    def handle(self, *args, **options):
        libros = [
            {'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'anio': 1967},
            {'titulo': '1984', 'autor': 'George Orwell', 'anio': 1949},
            {'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes', 'anio': 1605},
            {'titulo': 'El Principito', 'autor': 'Antoine de Saint-Exupéry', 'anio': 1943},
            {'titulo': 'Orgullo y prejuicio', 'autor': 'Jane Austen', 'anio': 1813},
        ]
        
        for libro_data in libros:
            libro, created = Libro.objects.get_or_create(
                titulo=libro_data['titulo'],
                defaults=libro_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Libro creado: {libro.titulo}'))