from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category, Image
     
def index(request):
	# get the blog posts that are published
	posts = Post.objects.all()
	# now return the rendered template
	return render(request, 'blog/index.html', {'posts': posts})
 
def post(request, name):
	# get the Post object
	post = get_object_or_404(Post, name=name)
	# now return the rendered template
	return render(request, 'blog/post.html', {'post': post})

def submit(request):
        return render(request, 'blog/submit.html')
