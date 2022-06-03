from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from api.models import customuser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = customuser
        fields = ['email','username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'confirm password'}),
        }
