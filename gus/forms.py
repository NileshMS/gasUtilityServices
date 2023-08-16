from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Services, ServiceRequest

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields= ['username', 'email']
    

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = ['title', 'image', 'serviceCharge', 'content', 'is_available']

class ServiceRequestForm(forms.ModelForm):

    class Meta:
        model = ServiceRequest
        fields = ['serviceType','status']
