from django import forms
from KmetApp.models import User, Selling, Basket
from django.contrib.auth.forms import UserCreationForm


class OglasForm(forms.ModelForm):
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


class SellingForm(forms.ModelForm):
    """Add Selling Form"""
    class Meta:
        model = Selling
        exclude = ['is_Active', 'seller']

    def save(self, commit=True):
        """Save Method"""
        selling = super(SellingForm, self).save(commit=False)

        if commit:
            selling.save()
        return selling


class UserEditForm(forms.ModelForm):
    """User Edit Form"""
    class Meta:
        model = User
        exclude = ['password', 'is_active', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """Save Method"""
        user = super(UserEditForm, self).save(commit=False)

        if commit:
            user.save()
        return user


class BasketForm(forms.ModelForm):
    """Add Basket Form"""
    class Meta:
        model = Basket
        exclude = ['is_Active', 'seller']

    def save(self, commit=True):
        """Save Method"""
        basket = super(BasketForm, self).save(commit=False)

        if commit:
            basket.save()
        return basket
