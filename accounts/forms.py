from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import User, Company, Employee


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2', 'is_employee','is_company']

class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    ) 
    class Meta:
        model = User
        fields = ['first_name','email']

class CompanyProfileForm(forms.ModelForm):

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 'rows': 5, 'cols': 100
            }
        )
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 'rows': 3, 'cols': 100
            }
        )
    )
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Company
        fields = ['image', 'description', 'address', 'phone']


class EmployeeProfileForm(forms.ModelForm):
    company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id":"company"
            }
        )
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    age = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 'rows': 3, 'cols': 100
            }
        )
    )
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    

    class Meta:
        model = Employee
        fields = ['image', 'age','company', 'address', 'phone']