from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Registration
# Create your views here.

def home(request):

    return render(request, 'accounts/home.html')

def register(request):

    form = Registration.objects.all()
   
        


    return render(request, 'accounts/register.html')

def login(request):

    return render(request, 'accounts/login.html')