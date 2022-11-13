from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SigninForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=False)
    first_name = forms.CharField(
        label='First name', max_length=200, min_length=3, required=False)
    last_name = forms.CharField(
        label='Last name', max_length=200, min_length=3, required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'email', 'first_name', 'last_name']
