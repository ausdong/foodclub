from django import forms

class UploadForm(forms.Form):
	title = forms.CharField(max_length=50)
	description = forms.CharField()
	image = forms.ImageField()