from django.db import models

from PIL import Image
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField('Is Employee', default=False)
    is_company = models.BooleanField('Is Company', default=False)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')

    image = models.ImageField(upload_to='companyprofile/', default='default.png')
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    company = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='employeeprofile/', default='default.png')
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=12, null=True)
    is_approved = models.BooleanField(default=False,null=True)
    is_rejected = models.BooleanField(default=False,null=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)