from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Registration
# Create your views here.

def index(request):
    return HttpResponse('Just an index page')

def register(request):

    form = Registration.objects.all()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        


    return render(request, 'accounts/register.html')

def login(request):
    return HttpResponse('login')