from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, permissions

class LibroViewSet(viewsets.ModelViewSet):
    """
    ViewSet que provee automáticamente las acciones:
    list, create, retrieve, update, partial_update, destroy
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    # swager
    permission_classes = [permissions.AllowAny]  # ← Permitir a todos

    # ¡AGREGAR BÚSQUEDA!
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo', 'autor']  # Buscar en título y autor
    filterset_fields = ['anio']  # Filtrar por año