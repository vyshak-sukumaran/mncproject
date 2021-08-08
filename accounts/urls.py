from django.urls import path
from .views import index, login, register


urlpatterns = [
    path('',index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
