from allauth.account.forms import SignupForm
from django import forms
from .models import User
from doctor.models import Doctor
from patient.models import Patient
from .models import *

class SignupForm(SignupForm):
    profile = forms.ChoiceField(choices=PROFILE)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER)
    city = forms.CharField(max_length=10)
    address = forms.CharField(max_length=40)
    mobile = forms.IntegerField()
    dob = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateTimeInput(attrs={'placeholder':'YYYY-MM-DD'}))

    def save(self, request):
        user = super(SignupForm, self).save(request)
        user.profile=self.cleaned_data['profile']
        user.age = self.cleaned_data['age']
        user.address = self.cleaned_data['address']
        user.mobile = self.cleaned_data['mobile']
        user.gender = self.cleaned_data['gender']
        user.city = self.cleaned_data['city']
        user.dob = self.cleaned_data['dob']
        if user.profile=='Doctor':
            doctor=Doctor.objects.create(user=user)
            doctor.save()
        else:
            patient=Patient.objects.create(user=user)
            patient.save()
        return user

