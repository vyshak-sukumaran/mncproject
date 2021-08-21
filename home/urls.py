from django.urls import path
from .views import home, index, employeeProfile, companyProfile, unknownReview, openReview


urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('employee/', employeeProfile, name='employee'),
    path('company/', companyProfile, name='company'),
    path('openreview/', openReview, name='openreview'),
    path('unknownreview/', unknownReview, name='unknownreview'),

]
