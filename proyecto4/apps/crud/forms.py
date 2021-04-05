from django import forms
from .models import tareas
class tareaForm(forms.ModelForm):
    class Meta:
        model = tareas

        fields = [
            'tarea'
        ]