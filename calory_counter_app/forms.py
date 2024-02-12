from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserDetails


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['age', 'gender', 'height', 'weight']


# class UserActivityForm(forms.ModelForm):
#     class Meta:
#         model = UserActivity
#         fields = ['exercise']
