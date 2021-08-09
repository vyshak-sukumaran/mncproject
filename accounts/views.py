from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Registration
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):

    return render(request, 'accounts/home.html')

def register(request):

    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def login(request):

    return render(request, 'accounts/login.html')