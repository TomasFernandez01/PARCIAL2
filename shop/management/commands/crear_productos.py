from django.core.management.base import BaseCommand
from shop.models import Producto

class Command(BaseCommand):
    help = 'Crea productos de prueba para la tienda'
    
    def handle(self, *args, **options):
        productos = [
            {'nombre': 'Laptop Gaming', 'precio': 1200.00, 'descripcion': 'Laptop para gaming de alta gama'},
            {'nombre': 'Smartphone', 'precio': 800.00, 'descripcion': 'Teléfono inteligente último modelo'},
            {'nombre': 'Auriculares Bluetooth', 'precio': 150.00, 'descripcion': 'Auriculares inalámbricos con cancelación de ruido'},
            {'nombre': 'Tablet', 'precio': 400.00, 'descripcion': 'Tablet para trabajo y entretenimiento'},
            {'nombre': 'Smartwatch', 'precio': 250.00, 'descripcion': 'Reloj inteligente con monitor de salud'},
            {'nombre': 'Teclado Mecánico', 'precio': 120.00, 'descripcion': 'Teclado mecánico para gamers'},
        ]
        
        for producto_data in productos:
            producto, created = Producto.objects.get_or_create(
                nombre=producto_data['nombre'],
                defaults=producto_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Producto creado: {producto.nombre}'))