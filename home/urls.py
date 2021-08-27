from django.urls import path
from .views import companyDashboard, home, index, employeeProfile, companyProfile, unknownReview, openReview


urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('employee/', employeeProfile, name='employee'),
    path('company/', companyProfile, name='company'),
    path('openreview/<str:pk>/', openReview, name='openreview'),
    path('unknownreview/<str:pk>', unknownReview, name='unknownreview'),
    path('company-dashboard/', companyDashboard, name='companydashboard'),

]
