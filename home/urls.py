from django.urls import path
from .views import companyDashboard, deleteReview, editReview, index, employeeProfile, companyProfile, unknownReview, openReview


urlpatterns = [
    path('', index, name='index'),
    path('employee/', employeeProfile, name='employee'),
    path('employee/editreview/<str:pk>', editReview, name='editreview'),
    path('employee/deletereview/<str:pk>', deleteReview, name='deletereview'),
    path('company/', companyProfile, name='company'),
    path('openreview/<str:pk>', openReview, name='openreview'),
    path('unknownreview/<str:pk>', unknownReview, name='unknownreview'),
    path('company-dashboard/<str:pk>', companyDashboard, name='companydashboard'),

]
