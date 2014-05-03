from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from blog.models import Post, Category, Image
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import UploadForm, UserForm

#home page
def index(request):
	# get the blog posts that are published
	posts = Post.objects.all()
	# now return the rendered template
	return render(request, 'blog/index.html', {'posts':posts})
	
#about us page
def about(request):
	return render(request, 'blog/About.html')
	
#registration page
def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['username']
			pw = form.cleaned_data['password']
			newuser = User.objects.create_user(name, form.cleaned_data['email'], pw)
			newuser.save()
			user = authenticate(username=name, password=pw)
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = UserForm()
	return render(request, 'blog/register.html', {'form':form})
	
#individual blog post
def post(request, name):
	# get the Post object
	post = get_object_or_404(Post, name=name)
	# now return the rendered template
	return render(request, 'blog/post.html', {'post': post})

#new blog post page and upload form
def submit(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			newimg = Image(path = form.cleaned_data['image'])
			newimg.save()
			p = Post(name = form.cleaned_data['title'], dsc = form.cleaned_data['description'], time = timezone.now(), imgID = newimg)
			p.save()
			return HttpResponseRedirect('/')
	else:
		form = UploadForm()
	return render(request, 'blog/submit.html', {'form':form,})