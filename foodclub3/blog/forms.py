from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User


class UploadForm(forms.Form):
	title = forms.CharField(max_length=50)
	description = forms.CharField()
	image = forms.ImageField()
	
class UserForm(forms.Form):
	username = forms.CharField(max_length=20)
	email = forms.EmailField()
	password = forms.CharField(widget=PasswordInput, max_length=40)
	
	def clean_username(self):
		try:
			User.objects.get(username=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(u'Username is already in use.')