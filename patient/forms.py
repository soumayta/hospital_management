from django import forms
from .models import Doctor
from .models import Patient

class Report(forms.Form):
    degree = forms.ChoiceField(choice=DEGREE)
    specialisation = forms.ChoiceField(choice=SPECIALISATION)
    sickness = forms.CharField(max_length=100)


    