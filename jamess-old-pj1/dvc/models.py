from django.db import models


# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    create_time = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
    
    
class Warcategory(models.Model):
    category_name = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    
    challenger = models.ForeignKey(Fighter, related_name='challenger')
    challenged = models.ForeignKey(Fighter, related_name='challenged')
    
    
    def __str__(self):
        return self.category_name
    
    
    
class Prompt(models.Model):
    category = models.ForeignKey(Warcategory)
    prompt_text = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    
    def __str__(self):
        return self.prompt_text
    
    
    
class Battle(models.Model):
    prompt = models.ForeignKey(Prompt)
    winner = models.ForeignKey(Fighter, related_name='winner')
    warcategory = models.ForeignKey(Warcategory)
    
    create_time = models.DateTimeField()
    
    def __str__(self):
        return self.winner.name + " in " + self.warcategory.category_name
    
    
    
class Face(models.Model):
    fighter = models.ForeignKey(Fighter)
    path = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    
    def __str__(self):
        return self.path
    
    
    
    