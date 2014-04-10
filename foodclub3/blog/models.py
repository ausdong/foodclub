from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    dsc = models.CharField(max_length=200)
    time = models.DateTimeField()

class Post(models.Model):
    name = models.CharField(max_length=200)
    dsc = models.CharField(max_length=200)
    catID = models.ForeignKey(Category)
    time = models.DateTimeField()
    img = models.FilePathField(path="/home")
			
class Image(models.Model):
    path = models.FilePathField(path="/home")
    postID = models.ForeignKey(Post)
    time = models.DateTimeField()
