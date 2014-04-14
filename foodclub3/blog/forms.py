from django import forms

class UploadForm(forms.Form):
	name = forms.CharField(max_length=50)
	description = forms.CharField()
	image = forms.ImageField()