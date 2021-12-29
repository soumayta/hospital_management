from django.shortcuts import redirect, render

from .forms import EditProfileForm, ProfileForm
from user.models import User
from .models import Doctor
# Create your views here.
def home(request):
    return render(request,'doctor/home.html')
# Create your views here.
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        edit_form = EditProfileForm(data=request.POST, instance=request.user.doctor)
        if form.is_valid() and edit_form.is_valid():
            user_form=form.save()
            custom_form = edit_form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
        edit_form = EditProfileForm(instance=request.user.doctor)
        args = {}
        args['form'] = form
        args['edit_form'] = edit_form
        return render(request, 'doctor/profile.html', {'form': form,'edit_form':edit_form})
