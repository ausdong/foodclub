from django.db import models
from django.core.urlresolvers import reverse

#Categories group posts into logical groups, not yet implemented
class Category(models.Model):
    name = models.CharField(max_length=200)
    dsc = models.CharField(max_length=200)
    time = models.DateTimeField()
	
#images are the key to the application
class Image(models.Model):
    path = models.ImageField(upload_to='%Y/%m/%d')
	
#posts and images are inseparable, track individual blog posts
class Post(models.Model):
	name = models.CharField(max_length=200)
	dsc = models.CharField(max_length=200)
	#catID = models.ForeignKey(Category)
	time = models.DateTimeField()
	imgID = models.ForeignKey(Image)