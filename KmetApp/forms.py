from django import forms
from KmetApp.models import *
from django.contrib.auth.forms import UserCreationForm      

class OglasForm(forms.ModelForm):
	"""docstring for OglasForm"""
	def __init__(self, arg):
		super(OglasForm, self).__init__()
		self.arg = arg
		
class UserForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = '__all__'

	
	def save(self, commit= True):		
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.last_name = self.cleaned_data['last_name']
		user.adress = self.cleaned_data['adress']
		user.zip_code = self.cleaned_data['zip_code']
		user.city= self.cleaned_data['city']
		user.phone_number = self.cleaned_data['phone_number']

		if commit:
			user.save()
		return user

class TestForm(forms.ModelForm):

	class Meta:
		model = Test
		fields = '__all__'

	def save(self, commit = True):
		test = super(TestForm, self).save(commit=False)
		test.test = self.cleaned_data['test']

		if commit:
			test.save()
		return test