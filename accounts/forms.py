from django import forms
from accounts.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields  = ['contact', 'birth_date', 'gender', 'blood_group']
        widgets = {
            'contact': forms.TextInput(attrs={'placeholder': 'Enter contact'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'custom-select'}),
            'blood_group': forms.Select(attrs={'class': 'custom-select'}),
        }

    def clean(self):
        data = self.cleaned_data
        return data