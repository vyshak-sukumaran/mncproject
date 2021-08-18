from django.db import models


# Create your models here.

class CompanyRegister(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    email = models.EmailField(default="example@mail.com")
    phone = models.CharField(max_length=12)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.description