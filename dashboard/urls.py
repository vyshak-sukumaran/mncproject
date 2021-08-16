from django.urls import path
from .views import userDashboard, companyDashboard
urlpatterns = [

    path('user', userDashboard, name='userdashboard'),
    path('company', companyDashboard, name='companydashboard'),

]
