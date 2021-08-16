from django.shortcuts import render

# Create your views here.
def userDashboard(request):
    
    return render(request, 'dashboard/userdashboard.html')

def companyDashboard(request):
    
    return render(request, 'dashboard/companydashboard.html')