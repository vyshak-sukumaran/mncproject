from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Registration
# Create your views here.

def index(request):
    return HttpResponse('Just an index page')

def register(request):

    form = Registration.objects.all()
   
        


    return render(request, 'accounts/register.html')

def login(request):

    return render(request, 'accounts/login.html')