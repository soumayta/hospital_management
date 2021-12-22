from django.shortcuts import render
from .models import Patient
from django.http import HttpResponse ,response

# Create your views here.
def Report(request):
    return render(request,'base2.html')

