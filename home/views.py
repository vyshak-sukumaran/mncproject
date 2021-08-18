from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import AddPosts
# Create your views here.

def index(request):


    return render(request, 'home/index.html')

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
def userProfile(request):


    return render(request, 'home/userprofile.html')

def companyProfile(request):


    return render(request, 'home/companyprofile.html')

@login_required(login_url='login')
def openReview(request):


    return render(request, 'home/openreview.html')

@login_required(login_url='login')
def unknownReview(request):


    return render(request, 'home/unknownreview.html')

