from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from blog.models import Post, Category, Image
from .forms import UploadForm
     
def index(request):
	# get the blog posts that are published
	posts = Post.objects.all()
	# now return the rendered template
	return render(request, 'blog/index.html', {'posts':posts})
	
def about(request):
	return render(request, 'blog/About.html')
 
def post(request, name):
	# get the Post object
	post = get_object_or_404(Post, name=name)
	# now return the rendered template
	return render(request, 'blog/post.html', {'post': post})

def submit(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			#img = UploadForm(request.POST, request.FILES)
			newimg = Image(path = form.cleaned_data['image'])
			newimg.save()
			p = Post(name = form.cleaned_data['name'], dsc = form.cleaned_data['description'], time = timezone.now(), imgID = newimg)
			p.save()
			return HttpResponseRedirect('/')
	else:
		form = UploadForm()
	return render(request, 'blog/submit.html', {'form':form,})