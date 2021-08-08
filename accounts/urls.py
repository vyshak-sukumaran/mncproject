from django.urls import path
from .views import home, login, register


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
