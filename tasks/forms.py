from django import forms
from .models import Task, TaskImage
from multiupload.fields import MultiFileField

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def clean(self):
        data = self.cleaned_data
        return data
    

class TaskImageForm(forms.ModelForm):
    class Meta:
        model = TaskImage
        fields = ['image']
    image = MultiFileField(min_num=1, max_num=5, max_file_size=1024*1024*10, required=False)