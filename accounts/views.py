from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CreateCompanyForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account has been created for"+ user)

            return redirect('login')
        


    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user')
        else:
            messages.info(request, 'Invalid credentials')
            
    
        
    return render(request, 'accounts/login.html')

def logoutUser(request):

    logout(request)
    return redirect('login')

def registerCompany(request):

    form = CreateCompanyForm()
    if request.method == 'POST':
        form = CreateCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company')

    context = {'form':form}

    return render(request, 'accounts/registercompany.html',context)