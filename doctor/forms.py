from django import forms
from doctor.models import Doctor
from user.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['city','mobile','age']
        
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model= Doctor
        fields = ['specialisation','experience']
                