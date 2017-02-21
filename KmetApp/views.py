from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import Http404, JsonResponse
from django.db import models
from django.contrib.auth import logout
from KmetApp.models import *
from django.views.decorators import csrf 
import json
from django.core import serializers
from django.db.models import Q
from KmetApp.forms import *

# Create your views here.
def home(request):
	return render(request, 'index.html')

def logIn(request):
	return render(request, 'User/LogIn.html')

def registration(request):
	return render(request , 'User/Registration.html')

def testView(request):
	return render(request, 'test.html')

def register_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		#print(form)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('index.html')
	args={}
	args['form'] = UserForm()
	return render (request , 'User/Registration.html' , args)

def test(request):
	
	form = TestForm(request.POST)

	if form.is_valid():
		form.save
		return HttpResponseRedirect('index.html')
	args={}
	args['form'] = TestForm()	
	return render (request , 'User/Registration.html')
