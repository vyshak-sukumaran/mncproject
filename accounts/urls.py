from django.urls import path
from .views import loginPage, logoutUser, register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    

]
