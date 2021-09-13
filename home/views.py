
from django.http.response import Http404, JsonResponse
from home.forms import ReviewForm,UnknownForm
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Avg
import json

from accounts.models import Company, Employee, User
from .models import Review, Unknown
# Create your views here.

def index(request):
    
    showreview = Review.objects.all()
    company = Company.objects.all()
    
    context = {'company':company,'showreview':showreview}
    return render(request, 'home/index.html',context)

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
def companyDashboard(request,pk):
    
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist:
        company = None
    
    emp_id = None
    if request.method == 'POST':
        emp_id = request.POST['employee_id']
        if emp_id:
            data = {
                "id":emp_id
            }
            get_employee = Employee.objects.get(id=int(emp_id))
            if "approve" in request.POST['action'] and get_employee.is_approved == False:
                get_employee.is_approved = True
                get_employee.save()
            elif "reject" in request.POST['action'] and get_employee.is_rejected == False:
                get_employee.is_rejected = True
                get_employee.save()
            else:
                return Http404()
            return JsonResponse(data, safe=False)

    employee = Employee.objects.all()      
    context = {'company':company,'employee':employee}
    return render(request, 'home/companydashboard.html',context)

@login_required(login_url='login')
def editReview(request,pk):

    showreview = Review.objects.get(id=pk)
    reviewform = ReviewForm(instance=showreview)
    
    if request.method == 'POST':
        reviewform = ReviewForm(request.POST,instance=showreview)
        if reviewform.is_valid():
            reviewform.save()
            return redirect('employee')
    
    context = {'reviewform':reviewform}
    return render(request, 'home/editreview.html',context)

@login_required(login_url='login')
def deleteReview(request,pk):

    showreview = Review.objects.get(id=pk)
    
    if request.method == 'POST':
        showreview.delete()
        return redirect('employee')

    
    
    context = {'showreview':showreview}
    return render(request, 'home/deletereview.html',context)
