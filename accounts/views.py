from accounts.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import User
from .forms import SignUpForm, CompanyProfileForm, UserForm, EmployeeProfileForm

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
            return redirect('index')

        elif user is not None and user.is_company:
            login(request, user)
            return redirect('index')
                
        else:
            messages.info(request, 'Username or Password Incorrect !')
            
    
        
    return render(request, 'accounts/login.html')

def logoutUser(request):

    logout(request)
    return redirect('index')

def editCompany(request):

    u_form = UserForm(instance = request.user)
    p_form = CompanyProfileForm(instance = request.user.company)


    if request.method == 'POST':
        u_form = UserForm(request.POST, instance = request.user)
        p_form = CompanyProfileForm(request.POST, request.FILES, instance = request.user.company)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'account has been updated')
            return redirect('company')


    context = {'u_form':u_form, 'p_form':p_form}

    return render(request, 'accounts/editcompanyprofile.html', context)

def editEmployee(request):

    u_form = UserForm(instance = request.user)
    p_form = EmployeeProfileForm()


    if request.method == 'POST':
        u_form = UserForm(request.POST, instance = request.user)
        p_form = EmployeeProfileForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'account has been updated')
            return redirect('employee')


    context = {'u_form':u_form, 'p_form':p_form}

    return render(request, 'accounts/editemployeeprofile.html', context)