from django.shortcuts import render
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
