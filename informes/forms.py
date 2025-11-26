from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['nombre', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del reporte'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido del reporte...',
                'rows': 6
            }),
        }
        labels = {
            'nombre': 'Nombre del Reporte',
            'contenido': 'Contenido'
        }