from django import forms
from .models import Todos



class TodosForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title', 'description', 'deadline', 'background_color', 'text_color', 'done']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'deadline': 'Deadline',
            'background_color': 'Background Color',
            'text_color': 'Text Color',
            'done': 'Done'
        }
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
