from django.db import models

# Create your models here.

class Registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(default='example@gmail.com')
    firstpassword = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)

    def __str__(self):
        return self.username