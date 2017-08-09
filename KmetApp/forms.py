from django import forms
from KmetApp.models import User, Product, Basket
from django.contrib.auth.forms import UserCreationForm


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


class ProductForm(forms.ModelForm):
    """Add Selling Form"""
    class Meta:
        model = Product
        exclude = ['is_active', 'seller']

    def save(self, commit=True):
        """Save Method"""
        selling = super(ProductForm, self).save(commit=False)

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
        exclude = ['is_active', 'seller']

    def save(self, commit=True):
        """Save Method"""
        basket = super(BasketForm, self).save(commit=False)

        if commit:
            basket.save()
        return basket
