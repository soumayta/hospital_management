from allauth.account.forms import SignupForm
from django import forms
from .models import User
from .models import *

class SignupForm(SignupForm):
    id = forms.UUIDField(primary_key = True, editable = False)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=10,choices=gender,null=True)
    city = forms.CharField(max_length=10)
    address = forms.CharField(max_length=40)
    mobile = forms.IntegerField()
    dob = forms.DateField('date of birth')

    def save(self, request):
        user = super(SignupForm, self).save(request)
        # import pdb;pdb.set_trace()
        user.id = self.cleaned_data['id']
        user.age = self.cleaned_data['age']
        user.address = self.cleaned_data['address']
        user.mobile = self.cleaned_data['mobile']
        user.gender = self.cleaned_data['gender']
        user.city = self.cleaned_data['city']
        user.save()
        return user

        