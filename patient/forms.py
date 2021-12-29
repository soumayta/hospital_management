from django import forms
from .models import Patient
from user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['city','mobile','age']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['sickness']

    