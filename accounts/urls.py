from django.urls import path
from .views import loginPage, register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
]
