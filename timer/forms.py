from django import forms
from .models import Timer

class TimeForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = ['time']
        widgets = {'time': forms.NumberInput(attrs={'step': '0.01'})}
