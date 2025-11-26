from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'anio']  # Campos que se exponen en la API
        read_only_fields = ['id']  # ID se genera automáticamente