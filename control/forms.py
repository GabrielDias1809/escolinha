from django import forms
from .models import Aula

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'hora' : forms.TimeInput(attrs={'class':'form-control'}),
            'instrutor': forms.Select(attrs={'class': 'form-control'}),
        }