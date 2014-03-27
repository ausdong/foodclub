from django.db import models

# Create your models here.
class Category(models.Model):
    catID = models.IntegerField()
    name = models.CharField(max_length=200)
    dsc = models.CharField(max_length=200)
    time = models.DateTimeField()

class Post(models.Model):
    postID = models.IntegerField()
    name = models.CharField(max_length=200)
    dsc = models.CharField(max_length=200)
    catID = models.ForeignKey(Category)
    time = models.DateTimeField()

class Image(models.Model):
    imgID = models.IntegerField()
    path = models.FilePathField(path="/home")
    postID = models.ForeignKey(Post)
    time = models.DateTimeField()

