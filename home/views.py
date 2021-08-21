
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User

from .models import AddPosts
# Create your views here.

def index(request):

    user = User.objects.all()
    
    context = {'user':user}
    return render(request, 'home/index.html',context)

def home(request):
    
    if request.method == 'POST':
        if request.POST.get('addpost'):
            newpost = AddPosts()
            newpost.post = request.POST.get('addpost')
            newpost.save()
    newpost = AddPosts.objects.all()



    context = {'newpost':newpost}    
    return render(request, 'home/home.html',context)

@login_required(login_url='login')
def employeeProfile(request):

    user = User.objects.all()
    
    context = {'user':user}

    return render(request, 'home/employeeprofile.html',context)

@login_required(login_url='login')
def companyProfile(request):


    user = User.objects.all()

    context = {'user':user}

    return render(request, 'home/companyprofile.html',context)

@login_required(login_url='login')
def openReview(request):


    return render(request, 'home/openreview.html')

@login_required(login_url='login')
def unknownReview(request):


    return render(request, 'home/unknownreview.html')

