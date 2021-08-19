from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField('Is Employee', default=False)
    is_company = models.BooleanField('Is Company', default=False)