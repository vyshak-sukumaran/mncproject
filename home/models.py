from django.db import models

from accounts.models import Company, Employee, User
# Create your models here.

CHOICES = (
    (1,'⭐'),
    (2,'⭐⭐'),
    (3,'⭐⭐⭐'),
    (4,'⭐⭐⭐⭐'),
    (5,'⭐⭐⭐⭐⭐'),
)


class Review(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    post = models.CharField(max_length=500)
    posted_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=CHOICES,default=0, null=True)

    def __str__(self):
        return self.post

class Unknown(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    post = models.CharField(max_length=500)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post