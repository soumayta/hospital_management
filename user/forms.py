from allauth.account.forms import SignupForm
from django import forms
from .models import User
from .models import *

class SignupForm(SignupForm):
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=gender)
    city = forms.CharField(max_length=10)
    address = forms.CharField(max_length=40)
    mobile = forms.IntegerField()
    dob = forms.DateField()

    def save(self, request):
        user = super(SignupForm, self).save(request)
        # import pdb;pdb.set_trace()
        user.age = self.cleaned_data['age']
        user.address = self.cleaned_data['address']
        user.mobile = self.cleaned_data['mobile']
        user.gender = self.cleaned_data['gender']
        user.city = self.cleaned_data['city']
        user.dob = self.cleaned_data['dob']
        user.save()
        return user

        