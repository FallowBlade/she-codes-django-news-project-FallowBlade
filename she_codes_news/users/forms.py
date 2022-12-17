from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder': 'Enter your name',}),
            'email': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder': 'test@test.com',}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder': 'test@test.com',}),
        }
