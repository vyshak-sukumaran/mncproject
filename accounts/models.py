from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField('Is Employee', default=False)
    is_company = models.BooleanField('Is Company', default=False)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')

    image = models.ImageField(default='/default.png', upload_to='companyprofile/')
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return f'{self.user.username} profile'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')

    image = models.ImageField(default='/default.png', upload_to='employeeprofile/')
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return f'{self.user.username} profile'