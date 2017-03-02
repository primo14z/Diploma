from django import forms
from KmetApp.models import *
from django.contrib.auth.forms import UserCreationForm      

class OglasForm(forms.ModelForm):
    """docstring for OglasForm"""
    def __init__(self, arg):
        super(OglasForm, self).__init__()
        self.arg = arg

class UserForm(UserCreationForm):
    """User Form"""
    class Meta:
        """Class Meta defined"""
        model = User
        exclude = ['password', 'is_active']

    def save(self, commit=True):
        """Save method"""
        user = super(UserForm, self).save(commit=False)

        if commit:
            user.save()
        return user
