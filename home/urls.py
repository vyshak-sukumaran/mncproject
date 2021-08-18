from django.urls import path
from .views import home, index, userProfile, companyProfile, unknownReview, openReview


urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('user/', userProfile, name='user'),
    path('company/', companyProfile, name='company'),
    path('openreview/', openReview, name='openreview'),
    path('unknownreview/', unknownReview, name='unknownreview'),

]
