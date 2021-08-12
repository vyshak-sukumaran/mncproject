from django.shortcuts import redirect, render

# Create your views here.


def register(request):

    return render(request, 'accounts/register.html')

def login(request):

    return render(request, 'accounts/login.html')

