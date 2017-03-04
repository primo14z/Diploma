from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import Http404, JsonResponse
from django.db import models
from django.contrib.auth import logout
from KmetApp.models import *
from django.views.decorators import csrf 
import json
import pdb
from django.core import serializers
from django.db.models import Q
from django.shortcuts import redirect
from KmetApp.forms import *

# Create your views here.
def home(request):
    """Return Index HTML"""
    return render(request, 'index.html')

def loginview(request):
    """Return LogIn HTML"""
    return render(request, 'User/LogIn.html')

def selling(request):
    """Return Selling HTML"""
    return render(request, 'Sellings/Selling.html')

def register_user(request):
    """Registration User Handler"""
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('KmetApp:home')
        else:
            return render(request, 'User/Registration.html', {'form' : form})
    else:
        return render(request, 'User/Registration.html')

def logon(request):
    """Log In User Handler"""
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('KmetApp:home')
        else:
            return render(request, 'User/LogIn.html', {'user': username})
    return render(request, 'User/LogIn.html')

def logoff(request):
    """Log out user"""
    logout(request)
    return redirect('KmetApp:home')

def add_selling(request):
    """Add Selling"""
    form = SellingForm()
    if request.method == 'POST':
        form = SellingForm(request.POST)
        if form.is_valid():
            bbb = form.save(commit=False)
            seller = User.objects.get(id=request.user.id)
            bbb.seller = seller
            bbb.save()
            return redirect('KmetApp:selling')
        else:
            return render(request, 'Sellings/Add_Selling.html', {'form' : form})
    else:
        return render(request, 'Sellings/Add_Selling.html')

def edit_user(request):
    """"Edit User"""
    form = UserEditForm()
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('KmetApp:home')
        else:
            return render(request, 'User/Edit.html', {'form' : form})
    else:
        return render(request, 'User/Edit.html')
