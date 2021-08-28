
from home.forms import ReviewForm,UnknownForm
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from accounts.models import Company, Employee, User
from .models import Review, Unknown
# Create your views here.

def index(request):

    company = Company.objects.all()
    
    context = {'company':company}
    return render(request, 'home/index.html',context)

def home(request):
    
    if request.method == 'POST':
        if request.POST.get('addpost'):
            newpost = Review()
            newpost.post = request.POST.get('addpost')
            newpost.save()
    newpost = Review.objects.all()



    context = {'newpost':newpost}    
    return render(request, 'home/home.html',context)

@login_required(login_url='login')
def employeeProfile(request):

    company = Company.objects.all()
    

    context = {'company':company}

    return render(request, 'home/employeeprofile.html',context)

@login_required(login_url='login')
def companyProfile(request):


    review = Review.objects.all()
    unknown = Unknown.objects.all()

    context = {'review':review,'unknown':unknown}

    return render(request, 'home/companyprofile.html',context)

@login_required(login_url='login')
def openReview(request,pk):

    company = Company.objects.get(id=pk)
    
    reviewform = ReviewForm()
    
    if request.method == 'POST':
        reviewform = ReviewForm(request.POST)
        if reviewform.is_valid():
            a = reviewform.save(commit=False)
            a.company = company
            a.employee = request.user
            a.save()
            return redirect('openreview',pk=a.company.id)
    
    showreview = Review.objects.all()


    context = {'company':company,'review':reviewform,'showreview':showreview}

    return render(request, 'home/openreview.html',context)

@login_required(login_url='login')
def unknownReview(request,pk):

    company = Company.objects.get(id=pk)
    
    if request.method == 'POST':
        unknownform = UnknownForm(request.POST)
        if unknownform.is_valid():
            a = unknownform.save(commit=False)
            a.company = company
            a.employee = request.user
            a.save()
            return redirect('unknownreview', pk=a.company.id)
    else:
        unknownform = UnknownForm()

    unknown_review = Unknown.objects.all()


    context = {'company':company,'unknownform':unknownform,'unknown_review':unknown_review}
    return render(request, 'home/unknownreview.html',context)

@login_required(login_url='login')
def companyDashboard(request):


    return render(request, 'home/companydashboard.html')
