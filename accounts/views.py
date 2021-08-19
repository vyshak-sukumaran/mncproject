from django.shortcuts import redirect, render
from .forms import SignUpForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account has been created for "+ user)
            return redirect('login')

        
    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_employee:
            login(request, user)
            return redirect('user')

        elif user is not None and user.is_company:
            login(request, user)
            return redirect('company')
                
        else:
            messages.info(request, 'Username or Password Incorrect !')
            
    
        
    return render(request, 'accounts/login.html')

def logoutUser(request):

    logout(request)
    return redirect('login')

