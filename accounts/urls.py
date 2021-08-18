from django.urls import path
from .views import loginPage, logoutUser, register, registerCompany


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register-company/', registerCompany, name='registercompany'),

]
