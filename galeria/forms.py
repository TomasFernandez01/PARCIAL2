from django import forms
from .models import Foto

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['titulo', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la foto'
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }