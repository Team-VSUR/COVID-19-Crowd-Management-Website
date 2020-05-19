from django import forms
from .models import Ticket


class CreateTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name','email','aadhar','zone','passengers']
        widgets = { 'name':forms.TextInput(attrs={'class': 'form-control'}),
                    'email':forms.TextInput(attrs={'class': 'form-control'}),
                    'aadhar':forms.TextInput(attrs={'class': 'form-control'}),
                    'zone':forms.Select(attrs={'class': 'form-control'}),
                    'passengers':forms.Textarea(attrs={'class': 'form-control'})
                }
