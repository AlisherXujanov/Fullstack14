from django import forms
from .models import Todos



class TodosForm(forms.ModelForm):
    
    class Meta:
        model = Todos
        fields = ['title', 'description', 'owner', 'deadline', 'background_color', 'text_color', 'done']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'owner': 'Owner',
            'deadline': 'Deadline',
            'background_color': 'Background Color',
            'text_color': 'Text Color',
            'done': 'Done'
        }
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
